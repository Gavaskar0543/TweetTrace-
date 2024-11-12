import tweepy
from config.settings import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Use OAuth1 (User-based Authentication)
auth = tweepy.OAuth1UserHandler(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# OAuth1 client for user-based requests
api = tweepy.API(auth)

# OAuth2 (Application-only Authentication) using Bearer Token
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def fetch_followers(username):
    try:
        # Fetch user data to get user ID
        user = api.get_user(screen_name=username)
        user_id = user.id

        # Fetch the followers of the user by their user ID
        followers = api.followers(user_id=user_id)

        print(f"Followers of {username}:")
        for follower in followers:
            print(f"- {follower.screen_name}")

        return followers

    except tweepy.TweepyException as e:
        print(f"Error fetching followers: {e}")
        return []
