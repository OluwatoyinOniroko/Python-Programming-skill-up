import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

#Task 1: Get the title of the webpage

r = requests.get('https://dbworld.sigmod.org/browse.html')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Get title
print(soup.title)

#Task 2. Get the list of tags on the webpage

for child in soup.descendants: # loop through the extracted elements
    if child.name: #if the name of the element exists, print it out
        print(child.name)

#Task 3: Count the number of posts in October

posts_in_october = soup.select('div.date:-soup-contains("Oct")')
october_count = len(posts_in_october)
print(f"\nTask 3: Number of posts in October: {october_count}")

#Task 4: Find all the urls in the href attributes of a tag a, and save to a csv file

# initialize an empty email list
urls_list = list()

# get all tag a
for tag in soup.find_all('a'):
    # see if tag a has the href  attribute
    if tag.has_attr('href'):
#Get the content of the href attribute
        reference = tag['href']

#Confirm if it is an external link using regex
if re.search('(http)', reference):
    # Append the URL to the list
    urls_list.append(reference)
    
#Generate a df from the list
attribute = pd.DataFrame({'URLs' : urls_list})

#file the output from the list
attribute.to_csv('urls.csv', index=False, encoding='utf-8')
#print file
print(attribute)



