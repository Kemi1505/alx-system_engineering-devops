#!/usr/bin/python3
"""Function to check total subscribers for a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returns the numbers of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "0x16.api.advanced:v1.0.0"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
