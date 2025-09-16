import tweepy

# API keys that yous saved earlier please change to your own keys
api_key = "hZxWAfejY1oOI2lb1RNJW8VtW"
api_secrets = "yMSBtTACY8m1YmR9c38AWvkpbbe6LCkaiVyyCCQlaFYnWUOn2U"
access_token = "1686562579978543104-CXXuJBKnTb1jqDZsqeJflpKEDW9TKA"
access_secret = "j6Lpe1zFH0J9aEAk53QW5Us5ddtqjhAt2O7mz5nSfce0F"


# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secrets)
auth.set_access_token(access_token, access_secret)

# initialize API
api = tweepy.API(auth, wait_on_rate_limit=True)

# get user information
user = api.get_user(screen_name='BillGates')

# show user information
print(f"user.name: {user.name}")
print(f"user.screen_name: {user.screen_name}")
print(f"user.location: {user.location}")
print(f"user.description: {user.description}")
print(f"user.followers_count: {user.followers_count}")
print(f"user.listed_count: {user.listed_count}")
print(f"user.statuses_count: {user.statuses_count}")
print(f"user.id: {user.id}")


