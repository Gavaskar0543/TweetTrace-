from config.settings import AUTHOR_USERNAME
from tweet_fetcher import fetch_followers, api  # Import 'api' for OAuth1 check

def main():
    # Test API connection
    try:
        # Verify the OAuth1 connection
        user = api.verify_credentials()
        if user:
            print(f"Connection established successfully! Authenticated as: {user.screen_name}")
        
        # Fetch followers of the specified user
        followers = fetch_followers(AUTHOR_USERNAME)
        if followers:
            print(f"Total Followers Found: {len(followers)}")

    except Exception as e:
        print(f"Error establishing connection: {e}")

if __name__ == "__main__":
    main()
