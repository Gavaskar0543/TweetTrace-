from config.settings import AUTHOR_USERNAME
from tweet_fetcher import fetch_followers

def main():
    # Fetch followers of the specified user
    followers = fetch_followers(AUTHOR_USERNAME)
    if followers:
        print(f"Total Followers Found: {len(followers)}")

if __name__ == "__main__":
    main()
