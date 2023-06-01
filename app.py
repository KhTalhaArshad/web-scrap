import requests
from bs4 import BeautifulSoup
import streamlit as st


def scrape_wikipedia(url):
    # Send a GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract the desired information from the HTML
        title = soup.title.string

        # Display the results using Streamlit
        st.write(f"Title: {title}")
    else:
        st.write(f"Error: Unable to retrieve data from {url}")


def main():
    # Define the URL to scrape
    url = "https://www.wikipedia.org/"

    # Set up Streamlit
    st.title("Wikipedia Web Scraper")
    st.write("Scraping data from Wikipedia...")

    # Call the web scraping function
    scrape_wikipedia(url)


if __name__ == "__main__":
    main()
