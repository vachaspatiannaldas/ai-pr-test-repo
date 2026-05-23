import requests


def fetch_payment():

    response = requests.get(
        "https://example.com"
    )

    return response.json()