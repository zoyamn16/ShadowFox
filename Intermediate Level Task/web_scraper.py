import requests
from bs4 import BeautifulSoup

# Website to scrape
url = "https://quotes.toscrape.com/"

try:
    # Send request
    response = requests.get(url)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract data
    title = soup.title.text.strip()
    headings = soup.find_all(["h1", "h2"])
    links = soup.find_all("a")

    # Save data to file
    with open("scraped_data.txt", "w", encoding="utf-8") as file:
        file.write("WEBSITE TITLE:\n")
        file.write(title + "\n\n")

        file.write("HEADINGS:\n")
        for h in headings:
            file.write(h.text.strip() + "\n")

        file.write("\nLINKS:\n")
        for link in links:
            href = link.get("href")
            if href:
                file.write(href + "\n")

    print("Scraping completed successfully!")

except Exception as e:
    print("Error occurred:", e)
