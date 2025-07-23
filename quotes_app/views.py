import random

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Quote, UserQuoteFeedback
from quotes_app.utils.get_quote import get_quote


class BaseView(View):
    def get(self, request):
        quotes = Quote.objects.all()
        if get_quote:
            weighted_quotes = []
            for quote in quotes:
                weight = quote.weight
                weighted_quotes.extend( [quote] * weight)
            random_quote = random.choice(weighted_quotes)
            random_quote.views += 1
            random_quote.save()
            context = {
                'quote': random_quote
            }
            return render(request, 'quotes_app/base.html', context=context)
        return render(request, 'quotes_app/base.html', context={'quote_text': 'Error'})

    def post(self, request, quote_id, action):
        quote = get_object_or_404(Quote, pk=quote_id)
        if action == 'like':
            quote.likes += 1
        elif action == 'dislike':
            quote.dislikes += 1
        elif action == 'unlike':
            if quote.likes > 0:
                quote.likes -= 1
        elif action == 'undislike':
            if quote.dislikes > 0:
                quote.dislikes -= 1
        else:
            return JsonResponse({'error': 'Invalid action'})
        quote.save()
        return JsonResponse({'status': 'success', 'likes': quote.likes, 'dislikes': quote.dislikes})



class PopularQuotesView(View):
    def get(self, request):
        quotes = Quote.objects.all()[:10]
        return render(request, 'quotes_app/popular_quotes.html', context={'quotes': quotes})



# Create your views here.
