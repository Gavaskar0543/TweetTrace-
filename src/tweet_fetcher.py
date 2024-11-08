import tweepy
from config.settings import BEARER_TOKEN

client = tweepy.Client(bearer_token=BEARER_TOKEN)

def fetch_tweet(tweet_id):
    try:
        tweet = client.get_tweet(tweet_id, tweet_fields=["author_id", "created_at", "public_metrics", "text"])
        return tweet.data
    except tweepy.TweepyException as e:
        print("Error fetching tweet:", e)
        return None
