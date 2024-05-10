#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}  # Set a custom User-Agent header
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful and contains valid JSON data
    if response.status_code == 200:
        try:
            data = response.json()
            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']
        except ValueError:
            pass  # Invalid JSON, fall through to return 0
    
    return 0

if __name__ == "__main__":
    subreddit = input("Enter subreddit: ")
    print(number_of_subscribers(subreddit))
