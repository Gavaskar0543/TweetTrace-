import tweepy
from config.settings import BEARER_TOKEN

client = tweepy.Client(bearer_token=BEARER_TOKEN)

def fetch_replies(tweet_id, author_username):
    query = f"conversation_id:{tweet_id} to:{author_username}"
    try:
        replies = client.search_recent_tweets(query=query, tweet_fields=["author_id", "created_at", "public_metrics", "text"])
        return replies.data if replies.data else []
    except tweepy.TweepyException as e:
        print("Error fetching replies:", e)
        return []
