import tweepy

# API keys that yous saved earlier please change to your own keys
api_key = "hZxWAfejY1oOI2lb1RNJW8VtW"
api_secrets = "yMSBtTACY8m1YmR9c38AWvkpbbe6LCkaiVyyCCQlaFYnWUOn2U"
access_token = "1686562579978543104-CXXuJBKnTb1jqDZsqeJflpKEDW9TKA"
access_secret = "j6Lpe1zFH0J9aEAk53QW5Us5ddtqjhAt2O7mz5nSfce0F"
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAL%2BlpAEAAAAAuYJUYnG5Rt9Z16tUobtOPlDEV2U%3D5fhiGfhCfdpEeat0fNadN8a1wWiGOhmsqgeFytUiEwRJqjmN7p'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secrets)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')


