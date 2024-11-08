from config.settings import BEARER_TOKEN, TWEET_ID, AUTHOR_USERNAME
from tweet_fetcher import fetch_tweet
from reply_fetcher import fetch_replies

def main():
    # Fetch the main tweet
    tweet = fetch_tweet(TWEET_ID)
    if tweet:
        print("Tweet Content:", tweet['text'])
        
        # Fetch replies to the main tweet
        replies = fetch_replies(TWEET_ID, AUTHOR_USERNAME)
        for reply in replies:
            print("Reply:", reply['text'], "| Author ID:", reply['author_id'])

if __name__ == "__main__":
    main()
