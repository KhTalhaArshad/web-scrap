pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

# Specify the URL of the website you want to scrape
url = 'https://example.com'

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find specific elements on the page using CSS selectors
# For example, let's extract all the links from the page
links = soup.select('a')

# Loop through the extracted links and print their text and href attributes
for link in links:
    print('Text:', link.text)
    print('URL:', link['href'])
    print('---')
