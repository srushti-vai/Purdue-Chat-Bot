import requests

api_key = "AIzaSyBc7i0k1FQaor4nUcAamdNdkRdLBlXQCy4"
search_engine_id = "b33f7cf76aca9467d"
query = "history of computer science"

url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}'

subject_html = requests.get(url)
data = subject_html.json()

for i in data['items']:
    print(i['link'])