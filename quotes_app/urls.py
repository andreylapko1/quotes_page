from django.urls import path

from .views import BaseView, PopularQuotesView

urlpatterns = [
    path('', BaseView.as_view(), name='base_view'),
    path('popular/', PopularQuotesView.as_view(), name='popular_quotes_view'),
    path('feedback/<int:quote_id>/<str:action>/', BaseView.as_view(), name='feedback'),
]