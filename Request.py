import requests as R

def data():
    url = input('Please paste Jsonplaceholderlink here: ')
    if not url.startswith('http://jsonplaceholder.typicode.com/todos'):
        print(f'Error:{url} is not jsonplaceholder link')
    else:
        response = R.get(url)
        url_data = response.json()
        print(url_data)

data()
