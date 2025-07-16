from django.db import models


class Quote(models.Model):
    quote_text = models.CharField(verbose_name='Quote Text', null=False, blank=False, max_length=500)
    quote_author = models.CharField(verbose_name='Quote Author',null=True, blank=True ,max_length=200)
    category = models.CharField(verbose_name='Quote Category',null=True, blank=True ,max_length=200)


    class Meta:
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'
        ordering = ['quote_author']


    def __str__(self):
        return f'{self.quote_text} - {self.quote_author}'


# Create your models here.
