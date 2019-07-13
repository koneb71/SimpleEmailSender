import requests

from simple_email.settings import MAILGUN_API_URL, MAILGUN_API_KEY


def get_logs(url):
    if not url:
        url = MAILGUN_API_URL + "/events"
        return requests.get(
            url,
            auth=("api", MAILGUN_API_KEY),
            params={
                "limit": 10}).json()
    return requests.get(
        url,
        auth=("api", MAILGUN_API_KEY)).json()
