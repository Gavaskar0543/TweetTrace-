import time
import logging

logging.basicConfig(filename='data/logs/tweettrace.log', level=logging.INFO)

def handle_rate_limit():
    print("Rate limit exceeded. Waiting for 15 minutes...")
    time.sleep(15 * 60)  # Wait for 15 minutes
