from bs4 import BeautifulSoup
import requests

search = input("What would you like to search?\n")

search = search.replace(" ", "+")

url = 'https://www.purdue.edu/home/search/?q=' + search

print(url)

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

doc = open("temp scraping", "w")
doc.write(str(soup))
doc.close

# search_url = soup.findall("a", attrs={"class":"gs-title"})

# for s in search_url:
#     print(s)