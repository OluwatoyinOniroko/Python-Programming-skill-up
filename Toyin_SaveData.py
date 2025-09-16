import json
import pandas as pd
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

# Flatten data
df_nested_list = pd.json_normalize(user._json)

# show results
print(df_nested_list)

# export dataframe to CSV file
df_nested_list.to_csv("twitteruser.csv")