from django.contrib.auth.models import User
from django.db import models


class Quote(models.Model):
    quote_text = models.CharField(verbose_name='Quote Text', null=False, blank=False, max_length=500)
    quote_author = models.CharField(verbose_name='Quote Author',null=True, blank=True ,max_length=200)
    category = models.CharField(verbose_name='Quote Category',null=True, blank=True ,max_length=200)
    likes = models.IntegerField(verbose_name='Quote Likes', null=False, blank=False, default=0)
    dislikes = models.IntegerField(verbose_name='Quote Dislikes', null=False, blank=False, default=0)
    views = models.IntegerField(verbose_name='Quote Views', null=False, blank=False, default=0)

    @property
    def weight(self):
        BASE_WEIGHT = 5
        return max(1, BASE_WEIGHT + (self.likes - self.dislikes))


    class Meta:
        ordering = ['-likes']
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'


    def __str__(self):
        return f'{self.quote_text} - {self.quote_author}'



class UserQuoteFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, verbose_name='Quote')
    type = models.CharField(verbose_name='Feedback type', choices=[('like', 'Like'), ('dislike', 'Dislike')],)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')

    class Meta:
        unique_together = ('user', 'quote')
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return f'{self.user.username} - {self.quote}'

# Create your models here.
