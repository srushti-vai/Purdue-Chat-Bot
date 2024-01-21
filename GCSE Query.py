import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
import requests

#------------------------------- GET QUERY ----------------------------------------

# search = input("What would you like to search?\n")
# search = search.replace(" ", "+")

query = "boiler gold rush"
new_query = ""

for words in query.split(" "):
    if words not in stopwords.words('english'):
        new_query += words + " "
new_query = new_query.strip()

tokenized = nltk.word_tokenize(new_query)

tokenized = [word for word in tokenized if word.isalpha() or word.isalnum()]

new_query = ""

for word in tokenized:
    new_query += word + " "

new_query = new_query.strip()

print(tokenized)

# -------------------------------- GCSE ----------------------------------

# api_key = "AIzaSyBc7i0k1FQaor4nUcAamdNdkRdLBlXQCy4"
# search_engine_id = "b33f7cf76aca9467d"

# url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}'
#
# subject_html = requests.get(url)
# data = subject_html.json()
#
# for x in data['items']:
#     print(x['title'])
#     print(x['link'])
#     print()

# ----------------- RETURN RELAVENT INFO ------------------------------

def relavent_information(query, url):

    # print(url)

    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")

    # container_div = soup.find('div', class_='introContainer col-lg-4 col-md-4 col-sm-12 col-xs-12')

    container_div = soup.find_all("div", attrs={"class":"container"})

    relavent = []

    # print(container_div[4].text)

    for c in container_div:
        # print(c.text)
        for q in query:
            if q in c.text.lower():
                relavent.append(c.text)

    return relavent

url = 'https://www.purdue.edu/orientation/bgr/'

relavent_list = relavent_information(tokenized, url)

for r in relavent_list:
    print(r)
    print('------------------------------------------------')