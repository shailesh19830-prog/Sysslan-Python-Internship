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
 
import shutil
import os

def backup_folder(source_folder, backup_folder):
    try:
        # Check if source exists
        if not os.path.exists(source_folder):
            print("Source folder does not exist.")
            return

        # If backup exists, remove it to create a fresh one
        if os.path.exists(backup_folder):
            shutil.rmtree(backup_folder)
            
        # Copy the entire directory
        shutil.copytree(source_folder, backup_folder)
        print(f"Successfully backed up '{source_folder}' to '{backup_folder}'.")
        
    except Exception as e:
        print(f"Backup failed: {e}")

# To test: Create a folder named "MyProject" in your directory.
# backup_folder("MyProject", "MyProject_Backup")
