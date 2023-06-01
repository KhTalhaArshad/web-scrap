import requests
from bs4 import BeautifulSoup
import streamlit as st

# Define the URL to scrape
url = "https://en.wikipedia.org/wiki/Neymar"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the relevant data on the page
title = soup.find("h1", id="firstHeading").text
paragraphs = soup.find_all("p")

# Streamlit app
st.title(title)

for paragraph in paragraphs:
    st.write(paragraph.text)
