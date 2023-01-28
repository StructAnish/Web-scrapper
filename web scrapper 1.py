import requests
from bs4 import BeautifulSoup
import webbrowser


req = requests.get ("https://www.geeksforgeeks.org/")
soup =  BeautifulSoup(req.content ,  "html.parser")
webpage = input("enetr the link for visting the webpage")

# print(soup.prettify())

# print("\n\n\n\n\n\n\n\n\n")

# print (soup.get_text())

# length = len (soup.contents)
# print("\n\n\n\n\n\n\n\n\n")
# print(length)

for link in soup.find_all('a'):
    print(link.get('href'))

