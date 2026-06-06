import requests
import os
import json
import hashlib
import time
import csv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Product Hunt API V2 GraphQL Endpoint
API_URL = "https://api.producthunt.com/v2/api/graphql"

# File Configuration
CACHE_FILE = "cache.json"
CSV_FILE = "products.csv"
CACHE_EXPIRY = 24 * 60 * 60  # 24 hours in seconds

# Retrieve Developer Token from environment variable
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# GraphQL queries
TRENDING_QUERY = """
query FetchTrendingApps {
  posts(order: VOTES, first: 20) {
    edges {
      node {
        id
        name
        tagline
        votesCount
        url
        createdAt
        topics {
          nodes {
            id
            name
          }
        }
      }
    }
  }
}
"""

SIMILAR_QUERY = """
query GetSimilar($topicIds: [ID!]) {
  posts(topicIds: $topicIds, first: 5) {
    nodes {
      name
    }
  }
}
"""

def get_cache_key(query_str):
    """Generate a unique key for the query."""
    return hashlib.md5(query_str.encode('utf-8')).hexdigest()

def load_cache():
    """Load the cache from the file."""
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}

def save_to_cache(key, data):
    """Save the API response to the cache with a timestamp."""
    cache = load_cache()
    cache[key] = {
        "timestamp": time.time(),
        "data": data
    }
    try:
        with open(CACHE_FILE, 'w') as f:
            json.dump(cache, f, indent=4)
    except IOError as e:
        print(f"Warning: Could not save to cache: {e}")

def clean_text(text):
    """Replace all commas with semicolons as per requirements."""
    if not text:
        return ""
    return str(text).replace(",", ";")

def get_existing_product_names():
    """Read existing names from the CSV to avoid duplicates."""
    names = set()
    if os.path.exists(CSV_FILE):
        try:
            with open(CSV_FILE, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader, None)  # Skip header
                for row in reader:
                    if row:
                        names.add(row[0])
        except Exception as e:
            print(f"Warning: Could not read existing CSV: {e}")
    return names

def fetch_similar_products(topic_ids, current_name):
    """Fetch similar products based on topics and exclude the current one."""
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    try:
        variables = {"topicIds": topic_ids}
        response = requests.post(API_URL, json={"query": SIMILAR_QUERY, "variables": variables}, headers=headers)
        response.raise_for_status()
        data = response.json()
        nodes = data.get("data", {}).get("posts", {}).get("nodes", [])
        
        # Extract names, filter out current product, and join with semicolons
        similar_names = [n["name"] for n in nodes if n["name"] != current_name]
        return "; ".join(similar_names[:3])
    except Exception as e:
        print(f"Warning: Failed to fetch similar products for {current_name}: {e}")
        return ""

def display_posts(posts):
    """Utility to print post information."""
    print(f"--- Top {len(posts)} Trending Apps on Product Hunt ---\n")
    for index, edge in enumerate(posts, 1):
        app = edge["node"]
        topics = [topic["name"] for topic in app.get("topics", {}).get("nodes", [])]
        
        print(f"{index}. {app['name']} (▲ {app['votesCount']} votes)")
        print(f"   Tagline: {app['tagline']}")
        print(f"   Topics:  {', '.join(topics)}")
        print(f"   Link:    {app['url']}")
        print("-" * 50)

def append_to_csv(new_posts):
    """Clean and append new posts to the CSV file."""
    if not new_posts:
        return

    file_exists = os.path.exists(CSV_FILE)
    
    try:
        with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
            # We use a custom writer or simple string formatting to ensure strict comma control
            # But csv.writer with default settings works if we clean data first
            writer = csv.writer(f)
            
            if not file_exists:
                writer.writerow(["name", "tagline", "similar_products"])
            
            for post in new_posts:
                name = clean_text(post["name"])
                tagline = clean_text(post["tagline"])
                
                print(f"   Fetching similar products for: {post['name']}...")
                topic_ids = [t["id"] for t in post.get("topics", {}).get("nodes", [])]
                similar = clean_text(fetch_similar_products(topic_ids, post["name"]))
                
                writer.writerow([name, tagline, similar])
                print(f"   ✅ Appended {post['name']} to {CSV_FILE}")
                
    except Exception as e:
        print(f"Error writing to CSV: {e}")

def fetch_trending_apps():
    cache_key = get_cache_key(TRENDING_QUERY)
    cache = load_cache()
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    posts = []
    from_cache = False

    # Check if we have a valid cache entry
    if cache_key in cache:
        entry = cache[cache_key]
        if time.time() - entry["timestamp"] < CACHE_EXPIRY:
            print("--- Loading results from cache (Last 24 hours) ---\n")
            posts = entry["data"]
            from_cache = True

    if not from_cache:
        try:
            print("--- Fetching fresh data from Product Hunt API ---\n")
            response = requests.post(API_URL, json={"query": TRENDING_QUERY}, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            if "errors" in data:
                print("GraphQL Error occurred:")
                for error in data["errors"]:
                    print(f"- {error.get('message')}")
                return

            posts = data.get("data", {}).get("posts", {}).get("edges", [])
            save_to_cache(cache_key, posts)
        except requests.exceptions.RequestException as e:
            print(f"An HTTP error occurred: {e}")
            return

    display_posts(posts)

    # Handle CSV Export
    existing_names = get_existing_product_names()
    new_to_export = []
    
    for edge in posts:
        post = edge["node"]
        if post["name"] not in existing_names:
            new_to_export.append(post)
    
    if new_to_export:
        print(f"\n--- Found {len(new_to_export)} new products to add to CSV ---")
        append_to_csv(new_to_export)
    else:
        print("\n--- No new products to add to CSV ---")

if __name__ == "__main__":
    if not ACCESS_TOKEN:
        print("Error: ACCESS_TOKEN not found. Please ensure it is set in your .env file.")
    else:
        fetch_trending_apps()
