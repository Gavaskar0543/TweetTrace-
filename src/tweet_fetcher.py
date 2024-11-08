import tweepy
from config.settings import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Authentication with OAuth 1.0a (User context)
auth = tweepy.OAuth1UserHandler(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Creating the Tweepy API object
api = tweepy.API(auth)

def fetch_followers(username):
    try:
        # Get the user by username
        user = api.get_user(screen_name=username)
        
        # Fetch the followers
        followers = api.followers(user.id)
        
        print(f"Followers of {username}:")
        for follower in followers:
            print(f"- {follower.screen_name}")
        return followers

    except tweepy.TweepyException as e:
        print(f"Error fetching followers: {e}")
        return []
