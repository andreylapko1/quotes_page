from django.shortcuts import render
from django.views import View
import requests


class BaseView(View):
    def get(self, request):
        response = requests.get('https://quoteapi.pythonanywhere.com/random')
        data = response.json()
        context = {
            'quote': data.get('Quotes')[0].get('quote'),
        }
        return render(request, 'quotes_app/base.html', context=context)


# Create your views here.
