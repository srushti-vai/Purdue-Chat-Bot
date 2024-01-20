import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# api_key = "AIzaSyBc7i0k1FQaor4nUcAamdNdkRdLBlXQCy4"
# search_engine_id = "b33f7cf76aca9467d"

query = "what is boiler gold rush?"
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

print(new_query)

# url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}'
#
# subject_html = requests.get(url)
# data = subject_html.json()
#
# for x in data['items']:
#     print(x['title'])
#     print(x['link'])
#     print()
