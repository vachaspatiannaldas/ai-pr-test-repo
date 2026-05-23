import requests


def fetch_payment():

    response = requests.get(
        "http://payment-api.com",
        verify=False
    )

    return response.json()