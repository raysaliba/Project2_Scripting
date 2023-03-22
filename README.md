First of all I started by taking the first argument which should be the website and created a variable called link to save it in it and created a function that checks if the website is working. Then I started working on getting the subdomains, directories, and files of this website.
1)	Check subdomains:
For checking the subdomains, I created a function that will enter the list of subdomains given in the subdomain_dictionary.bat file and will try them all with the link. Those who will work will be added in another file called subdomain_output.bat. I checked if they were working by getting a response from the server every time I was trying a new subdomain, if the response was 200 that means that it is working so we add it to the file.
2)	Check directories:
All I did was almost the same as the check subdomains but was getting the directories from a different file and was adding them after the link instead of before it. The ones that worked were added to directories_output.bat.
3)	Check files:
For checking the files, I used those command that I got from chatGBT:


html_content = response.content
html_string = html_content.decode('utf-8')

all they do is they get the html code and decode it to make it readable so I can work on them. Then I used regular expression to search for all the files that are available on the website and add them in a file called files_output.bat


At the end I run the check_website and if it returned true it will check for the subdomains, directories and the files of this website, if it returned false it will tell the user that the website given is not working.
