import tweepy

# API keys that yous saved earlier please change to your own keys
api_key = "hZxWAfejY1oOI2lb1RNJW8VtW"
api_secrets = "yMSBtTACY8m1YmR9c38AWvkpbbe6LCkaiVyyCCQlaFYnWUOn2U"
access_token = "1686562579978543104-CXXuJBKnTb1jqDZsqeJflpKEDW9TKA"
access_secret = "j6Lpe1zFH0J9aEAk53QW5Us5ddtqjhAt2O7mz5nSfce0F"
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAL%2BlpAEAAAAAuYJUYnG5Rt9Z16tUobtOPlDEV2U%3D5fhiGfhCfdpEeat0fNadN8a1wWiGOhmsqgeFytUiEwRJqjmN7p'


# V2 Twitter API Authentication
client = tweepy.Client(
    bearer_token,
    api_key,
    api_secrets,
    access_token,
    access_secret,
    wait_on_rate_limit=True,
)


client.create_tweet(text="It is Monday again!")

