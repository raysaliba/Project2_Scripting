import re
import requests
import sys



available = False;
link = sys.argv[1]

def check_website(link):
    response = requests.get(link)

    if response.status_code == 200:
        available = True
def check_subdomain(link):
    with open('subdomain_dictionary.bat') as f:
        for line in f:
            new_url= line+"."+link
            response = requests.get(new_url)

            if response.status_code == 200:
                with open('sundomains_output.bat', 'a') as f:
                        f.write(line)

def check_directories(link):




def check_files(link):
   
