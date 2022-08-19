from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import os

# This example allows for two implementations. One with a provided token 
# another with a fetched token. Be sure to comment out the option not 
# being used.

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
token = os.getenv('TOKEN')

redirect_url = 'https://tekksparrow-programs.github.io/website'
authorization_endpoint = 'https://api.shutterstock.com/v2/oauth/authorize'
token_exchange_url = 'https://api.shutterstock.com/v2/oauth/access_token'

session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url)

# OPTION 1: Fetch Token
auth_link = session.authorization_url(authorization_endpoint)
print(f"Please go authenticate with the shutterstock id server... {auth_link[0]}")
redirect_response = input("Paste the redirect url with params here:")
session.fetch_token(
    authorization_response=redirect_response,
    client_id=client_id,
    client_secret=client_secret,
    token_url=token_exchange_url,
    include_client_id=True
)
# OPTION 2: Provided Token
# session.headers['Authorization'] = f"Bearer {token}"

search_endpoint_url = 'https://api.shutterstock.com/v2/images/search'
params = {
    "query": "Paris",
    "orientation": "horizontal",
    "sort": "popular",
}
response = session.get(search_endpoint_url, params=params)

print(f"STATUS CODE : {response.status_code}")
print(f"STATUS TEXT : {response.text}")