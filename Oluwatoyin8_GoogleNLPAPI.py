## task 1
# importing the library
import pandas as pd

# reading the file as dataframe adjusting to show all the columns and first 5 rows
pd.set_option('display.max_columns', None)
proreviews1 = pd.read_csv('C:\\Users\HP\OneDrive\Desktop\Ty  - Fall 2023\Programming\Datasets\productreviews.csv')
print(proreviews1.head())
## task 2
# importing google libraries for the sentiment analysis
from google.cloud import language
from google.oauth2 import service_account

# creating new columns to store the sentiment score and magnitude
proreviews1['sentiment_score'] = None
proreviews1['sentiment_magnitude'] = None
# iterating through the dataframe
for index, row in proreviews1.head(5000).iterrows():
    review_text = row['Review']
    if pd.isnull(review_text) or review_text.strip() == '':
        proreviews1.at[index, 'sentiment_score'] = 'No review found'
        proreviews1.at[index, 'sentiment_magnitude'] = 'No review found'
    else:
        # loading the key file
        creds = service_account.Credentials.from_service_account_file('C:\\Users\HP\Downloads\proven-system-406313-5a6b51fa9904.json')
        # initializing a client using the key file
        client = language.LanguageServiceClient(credentials=creds)
        # converting the text into a document type
        document = language.Document(content=review_text, type_=language.Document.Type.PLAIN_TEXT)
        # calling function to analysis the sentiment of the text
        response = client.analyze_sentiment(document=document)
        # geting the results in variable sentiment
        sentiment = response.document_sentiment
        proreviews1.at[index, 'sentiment_score'] = sentiment.score
        proreviews1.at[index, 'sentiment_magnitude'] = sentiment.magnitude
        # printing each review sentiment score
        print(review_text)
        print("Score", sentiment.score)
        print("Magnitude", sentiment.magnitude)
## Task 3
# printing the updated dataframe
print(proreviews1.head())
# saving the csv file for the first 5000 reviews as productreviewssentiment.csv
proreviews1.head(5000).to_csv("C:\\Users\HP\OneDrive\Desktop\Ty  - Fall 2023\Programming\Datasets\Previewssentiment.csv", index=False)


