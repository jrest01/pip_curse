import requests

def get_categories():
    r = requests.get('http://127.0.0.1:8000/contact')
    print(r.status_code)
    # print(r.text)
    print(type(r.text))
    categories = r.json()
    for category in categories:
        print (category['name'])
