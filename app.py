import requests

from bs4 import BeautifulSoup

# URL of the Wikipedia page for Asif Ali Zardari

url = "https://en.m.wikipedia.org/wiki/Asif_Ali_Zardari"

# Send a GET request to the website

response = requests.get(url)

# Check if the request was successful (status code 200)

if response.status_code == 200:

    # Parse the HTML content using BeautifulSoup

    soup = BeautifulSoup(response.content, "html.parser")

    # Get the page title

    title = soup.find("h1", {"id": "firstHeading"}).text

    print("Page Title:", title)

    # Find the infobox table on the page

    infobox = soup.find("table", {"class": "infobox"})

    # Find all the rows in the infobox

    rows = infobox.find_all("tr")

    # Extract the information from each row

    print("Information:")

    for row in rows:

        header = row.find("th")

        if header:

            header_text = header.text.strip()

            data_cell = row.find("td")

            if data_cell:

                data = data_cell.text.strip()

                print(header_text + ":", data)

else:

    print("Failed to retrieve the website content.")
