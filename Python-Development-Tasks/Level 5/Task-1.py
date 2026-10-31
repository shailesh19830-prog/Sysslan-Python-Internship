import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Fetch the HTML content
        response = requests.get(url)
        response.raise_for_status() # Check for errors
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract data (Example: Getting the title)
        page_title = soup.title.string if soup.title else "No Title Found"
        print(f"Website: {url}")
        print(f"Page Title: {page_title}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Example site
scrape_website("http://example.com")