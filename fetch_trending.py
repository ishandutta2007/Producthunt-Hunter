import requests
import os
import json
import hashlib
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Product Hunt API V2 GraphQL Endpoint
API_URL = "https://api.producthunt.com/v2/api/graphql"

# Cache Configuration
CACHE_FILE = "cache.json"
CACHE_EXPIRY = 24 * 60 * 60  # 24 hours in seconds

# Retrieve Developer Token from environment variable
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# GraphQL query to pull trending/top voted posts
query = """
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
            name
          }
        }
      }
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

def fetch_trending_apps():
    cache_key = get_cache_key(query)
    cache = load_cache()
    
    # Check if we have a valid cache entry
    if cache_key in cache:
        entry = cache[cache_key]
        if time.time() - entry["timestamp"] < CACHE_EXPIRY:
            print("--- Loading results from cache (Last 24 hours) ---\n")
            display_posts(entry["data"])
            return

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    
    try:
        print("--- Fetching fresh data from Product Hunt API ---\n")
        # Product Hunt V2 API handles all queries via POST requests
        response = requests.post(API_URL, json={"query": query}, headers=headers)
        
        # Check for HTTP errors
        response.raise_for_status()
        
        data = response.json()
        
        # Check if the API returned GraphQL errors
        if "errors" in data:
            print("GraphQL Error occurred:")
            for error in data["errors"]:
                print(f"- {error.get('message')}")
            return

        posts = data.get("data", {}).get("posts", {}).get("edges", [])
        
        # Save successful response to cache
        save_to_cache(cache_key, posts)
        
        display_posts(posts)
            
    except requests.exceptions.RequestException as e:
        print(f"An HTTP error occurred: {e}")

if __name__ == "__main__":
    if not ACCESS_TOKEN:
        print("Error: ACCESS_TOKEN not found. Please ensure it is set in your .env file.")
    else:
        fetch_trending_apps()
