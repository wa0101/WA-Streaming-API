# ===========================================
# WA STREAMING API | Arabic Version
# ===========================================
# 
# This script is a Python example using the `requests` library to interact 
# with the WA Streaming API, which provides access to streaming content, 
# including searching, navigating, and retrieving information for movies, 
# series, anime, and other items.
# 
# This example covers:
# 1. Fetching a list of items from the homepage.
# 2. Retrieving detailed info about a specific item.
# 3. Searching for items using a search query.
# 4. Fetching watch links and episode lists.
# 5. Navigating through paginated search results.
# Each function will demonstrate how to interact with the API and process
# ===========================================

import requests

BASE_URL = "https://wa-watch-api.onrender.com"

# ===========================================
# Function: get_list
# ===========================================
# this function fetches the list of items from the homepage
# it makes a GET request to the /list/ endpoint
# if successful, it prints out each item found on the homepage
# otherwise, it prints out the error status code
def get_list():
    response = requests.get(f"{BASE_URL}/list/")
    if response.status_code == 200:
        data = response.json()
        print("List of Items:")
        for item in data.get('list', []):
            print(f"Title: {item['title']}, Category: {item['category']}, Label: {item['label']}, URL: {item['href']}")
    else:
        print(f"Failed to fetch list: {response.status_code}")

# ===========================================
# Function: get_item_info
# ===========================================
# this function fetches detailed information about a specific item
# it takes a URL as input and sends a GET request to the /iteminfo endpoint with the URL as a parameter
# if successful, it prints out details like the title, thumbnail, story, extra content, and left box details
# otherwise, it prints out an error message
def get_item_info(url):
    response = requests.get(f"{BASE_URL}/iteminfo", params={'url': url})
    if response.status_code == 200:
        data = response.json()
        print("Item Info:")
        print(f"Title: {data['title']}")
        print(f"Thumbnail: {data['thumbnail']}")
        print(f"Story: {data['story']}")
        print("Extra Content:", data.get('extraContent'))
        print("Left Box:", data.get('leftBox'))
    else:
        print(f"Failed to fetch item info: {response.status_code}")

# ===========================================
# Function: search_items
# ===========================================
# this function searches for items based on a query provided by the user
# it sends a GET request to the /search endpoint with the search term as a parameter
# if successful, it prints out the search results including the title, category, label, and URL for each item
# otherwise, it prints an error status code
def search_items(query):
    response = requests.get(f"{BASE_URL}/search", params={'q': query})
    if response.status_code == 200:
        data = response.json()
        print("Search Results:")
        for item in data.get('list', []):
            print(f"Title: {item['title']}, Category: {item['category']}, Label: {item['label']}, URL: {item['href']}")
    else:
        print(f"Failed to search items: {response.status_code}")

# ===========================================
# Function: watch_item
# ===========================================
# this function fetches the iframe source and episodes for a specific watch URL
# it takes a URL as input and sends a GET request to the /watch endpoint with the URL as a parameter
# if successful, it prints out the iframe source and the list of episodes with their names and URLs
# otherwise, it prints out an error message
def watch_item(url):
    response = requests.get(f"{BASE_URL}/watch", params={'url': url})
    if response.status_code == 200:
        data = response.json()
        print("Watch Info:")
        print(f"Iframe Source: {data['iframeSrc']}")
        print("Episodes:")
        for episode in data.get('episodes', []):
            print(f"Name: {episode['name']}, URL: {episode['href']}")
    else:
        print(f"Failed to fetch watch info: {response.status_code}")

# ===========================================
# Function: navigate_pages
# ===========================================
# this function helps in navigating through the search results pages
# it takes a search term and a page number as inputs and sends a GET request to the /navigation endpoint
# if successful, it prints out the items found on that particular page
# otherwise, it prints an error status code
def navigate_pages(query, page):
    response = requests.get(f"{BASE_URL}/navigation", params={'q': query, 'page': page})
    if response.status_code == 200:
        data = response.json()
        print("Navigation Results:")
        for item in data.get('list', []):
            print(f"Title: {item['title']}, Category: {item['category']}, Label: {item['label']}, URL: {item['href']}")
    else:
        print(f"Failed to navigate pages: {response.status_code}")

# ===========================================
# Main Section: Running Examples
# ===========================================
if __name__ == "__main__":
    # example: fetch list of items from the homepage
    print("Fetching list of items...")
    get_list()

    # example: search for 'Naruto'
    print("\nSearching for 'Naruto'...")
    search_items("Naruto")

    # example: navigate search results pages for 'Naruto', page 2
    print("\nNavigating search results pages for 'Naruto', page 2...")
    navigate_pages("Naruto", 2)
