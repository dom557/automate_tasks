import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_html(html, element, class_name=None):
    soup = BeautifulSoup(html, 'html.parser')
    if class_name:
        return soup.find_all(element, class_=class_name)
    return soup.find_all(element)
