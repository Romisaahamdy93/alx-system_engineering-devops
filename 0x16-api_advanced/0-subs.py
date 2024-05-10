import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}  # Set a custom User-Agent header
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return 0
        else:
            raise  # Re-raise the exception if it's not a 404 error
    except Exception as e:
        print("An error occurred:", e)
    return 0

if __name__ == "__main__":
    subreddit = input("Enter subreddit: ")
    print(number_of_subscribers(subreddit))
