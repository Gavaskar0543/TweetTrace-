import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twitter API credentials
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Username for fetching followers
AUTHOR_USERNAME = os.getenv("AUTHOR_USERNAME")

# Print to verify values are loaded (Remove these in production)
print("API_KEY:", API_KEY)
print("API_SECRET_KEY:", API_SECRET_KEY)
print("BEARER_TOKEN:", BEARER_TOKEN)
print("ACCESS_TOKEN:", ACCESS_TOKEN)
print("ACCESS_TOKEN_SECRET:", ACCESS_TOKEN_SECRET)
print("AUTHOR_USERNAME:", AUTHOR_USERNAME)
