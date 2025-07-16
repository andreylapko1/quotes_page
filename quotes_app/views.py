from django.shortcuts import render
from django.views import View
import requests
from .models import Quote
from quotes_app.utils.get_quote import get_quote


class BaseView(View):
    def get(self, request):
        attempts = 10
        for _ in range(attempts):
            context = get_quote()
            if not context:
                return render(request, 'base.html', context={'quote_text':'Error. The service is temporarily unavailable'})
            text = context.get('quote_text')
            author = context.get('quote_author')
            if not text:
                return render(request, 'base.html', context={'quote_text':'Error. The quote text is empty'})

            if not Quote.objects.filter(quote_text=text).exists():
                if Quote.objects.filter(quote_author=author).count() <= 3:
                    quote = Quote(**context)
                    quote.save()
                    return render(request, 'quotes_app/base.html', context=context)
        return render(request, 'quotes_app/base.html', context={'quote_text':'Error. Not found'}, status=404)






# Create your views here.
