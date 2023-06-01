import requests

from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com/"

# Send a GET request to the website

response = requests.get(url)

# Check if the request was successful (status code 200)

if response.status_code == 200:

    # Parse the HTML content using BeautifulSoup

    soup = BeautifulSoup(response.content, "html.parser")

    # Find all quote containers on the page

    quote_containers = soup.find_all("div", {"class": "quote"})

    # Extract the quote and author from each container

    for container in quote_containers:

        quote = container.find("span", {"class": "text"}).text

        author = container.find("small", {"class": "author"}).text

        print("Quote:", quote)

        print("Author:", author)

        print()

else:

    print("Failed to retrieve the website content.")

 from each row

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
