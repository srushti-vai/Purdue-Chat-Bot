import requests

api_key = "AIzaSyBc7i0k1FQaor4nUcAamdNdkRdLBlXQCy4"
search_engine_id = "b33f7cf76aca9467d"
query = "what is bgr?"

url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}'

subject_html = requests.get(url).text
print(subject_html)