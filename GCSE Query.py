import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import requests

#------------------------------- PROCESS QUERY ----------------------------------------
def keywords(query):
    new_query = ""

    # checks each word in 'query' if it's a stopword -> if not, adds it to new_query
    for words in query.split(" "):
        if words not in stopwords.words('english'):
            new_query += words + " "

    # gets rid of whitespace at the end of new_query
    new_query = new_query.strip()

    # tokenizes the query into words
    tokenized = nltk.word_tokenize(new_query)

    # replaces list with all alphanumeric words within the original list
    tokenized = [word + " " for word in tokenized if word.isalpha() or word.isalnum()]

    # # resets new_query
    # new_query = ""
    #
    # # replaces new_query with original query - stop words - punctuation
    # for word in tokenized:
    #     new_query += word
    #
    # # gets rid of whitespace at the end of new_query
    # new_query = new_query.strip()

    return tokenized

# -------------------------------- GCSE ----------------------------------
links = []

def get_links(query):
    api_key = "AIzaSyBc7i0k1FQaor4nUcAamdNdkRdLBlXQCy4"
    search_engine_id = "b33f7cf76aca9467d"

    url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}'

    subject_html = requests.get(url)
    data = subject_html.json()

    # adds each link generated by the search from gcse to be added to 'links' (a global variable)
    for x in data['items']:
        links.append(x['link'])

# ----------------- RETURN RELEVANT INFO ------------------------------

def relevant_information(query, url):

    # print(url)

    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")

    # container_div = soup.find('div', class_='introContainer col-lg-4 col-md-4 col-sm-12 col-xs-12')

    container_div = soup.find_all("div", attrs={"class":"container"})

    relevant = []

    # print(container_div[4].text)

    for c in container_div:
        # print(c.text)
        for q in query:
            if q in c.text.lower():
                relevant.append(c.text)
                break # added break to prevent looping for each word in query

    return relevant

# made a function out of loop which prints relevant information
def get_more_relevant_information(rel_list):
    for r in rel_list:

        # added further filtering (first letter of a sentence is uppercase and sentence ends with a period)
        sentences = nltk.sent_tokenize(r)
        for sentence in sentences:
            if sentence[0:1].upper() == sentence[0:1] and sentence[-1:] == ".":
                print(sentence.strip())
        print('------------------------------------------------')
# ----------------- EXECUTION ------------------------------

query = "computer science"
get_links(query)
tokenized = keywords(query)

for url in links:
    relevant_list = relevant_information(tokenized, url)
    get_more_relevant_information(relevant_list)