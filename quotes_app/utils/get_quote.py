import os

import requests

# URL='https://quoteapi.pythonanywhere.com/random'
URL='https://api.api-ninjas.com/v1/quotes'

def get_quote():
    response = requests.get(URL, headers={'X-Api-Key': os.getenv('API_KEY')})
    data = response.json()
    if response.status_code == 200:
        quote_data = {
                'quote_text': data[0].get('quote'),
                'quote_author': None if data[0].get('author') == 'Null' else data[0].get('author'),
                'category': None if data[0].get('category') == 'Null' else data[0].get('category'),
            }
        return quote_data
    return None