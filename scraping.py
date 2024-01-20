from bs4 import BeautifulSoup
import requests

# search = input("What would you like to search?\n")
# search = search.replace(" ", "+")

url = 'https://www.purdue.edu/orientation/bgr/'

print(url)

page = requests.get(url).text
soup = BeautifulSoup(page, "html.parser")

# container_div = soup.find('div', class_='introContainer col-lg-4 col-md-4 col-sm-12 col-xs-12')

container_div = soup.find_all("div", attrs={"class":"container"})

for c in container_div:
    print(c.text)

# if (container_div):

#     paragraphs = container_div.find_all('p')

#     if paragraphs:

#         for p in paragraphs:
#             print(p.text)

#     else:
#         print("no p found")

# else:
#     print('no container div found')

# search_url = soup.findall("a", attrs={"class":"gs-title"})

# for s in search_url:
#     print(s)