import requests
from bs4 import BeautifulSoup

def fetch_web_page(url):
    """
    Fetches the content of a web page.

    Args:
        url (str): The URL of the web page to fetch.

    Returns:
        str: The content of the web page.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.text

def parse_html(content):
    """
    Parses the HTML content of a web page.

    Args:
        content (str): The HTML content of the web page.

    Returns:
        BeautifulSoup: The parsed HTML content.
    """
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def extract_information(soup):
    """
    Extracts information from the parsed HTML content.

    Args:
        soup (BeautifulSoup): The parsed HTML content.

    Returns:
        dict: A dictionary containing the extracted information.
    """
    # Example: Extract the title of the web page
    title = soup.title.string if soup.title else 'No title found'

    # Add more extraction logic as needed
    return {'title': title}

if __name__ == "__main__":
    url = "https://example.com"  # Replace with the URL you want to scrape
    content = fetch_web_page(url)
    soup = parse_html(content)
    info = extract_information(soup)
    print(info)
