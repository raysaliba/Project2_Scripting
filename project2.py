import re
import requests
import sys


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
                with open('subdomains_output.bat', 'a') as j:
                        j.write(line)

def check_directories(link):
    with open('dirs_dictionary.bat') as f:
        for line in f:
            new_url= link+"/"+line+"/"
            response = requests.get(new_url)

            if response.status_code == 200:
                with open('directories_output.bat', 'a') as j:
                        j.write(line)



def check_files(link):
    response = requests.get(link)
    html_content = response.content

    html_string = html_content.decode('utf-8')
    pattern = r"(?:href:(.*\..*))"
    list = re.findall(pattern,html_string)
    for line in list:
        with open('files_output.bat', 'a') as j:
                        j.write(line)


if check_website(link):
    check_subdomain(link)
    check_directories(link)
    check_files(link)
else:
    print("the website entered is not valid")


