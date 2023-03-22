import re
import requests



available = False;

def check_website(link):
    response = requests.get(link)

    if response.status_code == 200:
        available = True