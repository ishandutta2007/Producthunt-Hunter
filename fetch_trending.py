import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Product Hunt API V2 GraphQL Endpoint
API_URL = "https://api.producthunt.com/v2/api/graphql"

# Retrieve Developer Token from environment variable
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# GraphQL query to pull trending/top voted posts
# By default, Product Hunt filters to the last month if postedAfter is omitted,
# but we explicitly ask for the first 20 posts ordered by votes.
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

def fetch_trending_apps():
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    
    try:
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
        
        print(f"--- Top {len(posts)} Trending Apps on Product Hunt ---\n")
        for index, edge in enumerate(posts, 1):
            app = edge["node"]
            topics = [topic["name"] for topic in app.get("topics", {}).get("nodes", [])]
            
            print(f"{index}. {app['name']} (▲ {app['votesCount']} votes)")
            print(f"   Tagline: {app['tagline']}")
            print(f"   Topics:  {', '.join(topics)}")
            print(f"   Link:    {app['url']}")
            print("-" * 50)
            
    except requests.exceptions.RequestException as e:
        print(f"An HTTP error occurred: {e}")

if __name__ == "__main__":
    if not ACCESS_TOKEN:
        print("Error: ACCESS_TOKEN not found. Please ensure it is set in your .env file.")
    else:
        fetch_trending_apps()
