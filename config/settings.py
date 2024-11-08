import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twitter API credentials
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Tweet and user settings
TWEET_ID = os.getenv("TWEET_ID")            # Tweet ID to fetch
AUTHOR_USERNAME = os.getenv("AUTHOR_USERNAME")  # Username of the tweet's author
