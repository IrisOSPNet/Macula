import os
import time
import random
import requests
from bs4 import BeautifulSoup

# List of school info websites (ensure you have permission to scrape these)
websites = [
    'https://example-school1.com',
    'https://example-school2.com',
    'https://example-school3.com',
    'https://en.wikipedia.org/wiki/Mathematics',
    'https://en.wikipedia.org/wiki/List_of_mathematical_symbols',
    'https://en.wikipedia.org/wiki/Mathematical_notation',
    'https://en.wikipedia.org/wiki/History_of_mathematics',
    'https://en.wikipedia.org/wiki/Mathematical_constant',
    'https://en.wikipedia.org/wiki/List_of_formulas_in_elementary_mathematics',
    'https://en.wikipedia.org/wiki/Glossary_of_mathematics',
    'https://en.wikipedia.org/wiki/Outline_of_mathematics',
    'https://en.wikipedia.org/wiki/Category:Mathematics',
    'https://en.wikipedia.org/wiki/Mathematical_logic'
]

# Folder to save scraped data
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "ScrapedSchoolInfo")
os.makedirs(desktop_path, exist_ok=True)

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Extracting the title of the page
        title = soup.title.string if soup.title else 'No Title'
        
        # Save the scraped data to a file
        filename = os.path.join(desktop_path, f"{title}.txt")
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
        
        print(f"Scraped and saved data from {url}")
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")

while True:
    random_website = random.choice(websites)
    scrape_website(random_website)
    time.sleep(1)  # Wait for 1 second before the next iteration
