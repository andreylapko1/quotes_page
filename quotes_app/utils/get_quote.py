import os
import requests
from quotes_app.models import Quote

# URL='https://quoteapi.pythonanywhere.com/random'
URL='https://api.api-ninjas.com/v1/quotes'

def get_quote():
    attempts = 5
    for _ in range(attempts):
        response = requests.get(URL, headers={'X-Api-Key': os.getenv('API_KEY')})
        data = response.json()
        if response.status_code == 200:
            quote_data = {
                    'quote_text': data[0].get('quote'),
                    'quote_author': None if data[0].get('author') == 'Null' else data[0].get('author'),
                    'category': None if data[0].get('category') == 'Null' else data[0].get('category'),
                }
            if not Quote.objects.filter(quote_text=quote_data.get('quote_text')).exists():
                if Quote.objects.filter(quote_author=quote_data.get('quote_author')).count() <= 3:
                    quote = Quote(**quote_data)
                    quote.save()
                    return True
        return False
    return False