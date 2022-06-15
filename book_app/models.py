from django.db import models
from django.urls import reverse


class Book(models.Model):

    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField()
    author = models.CharField(max_length=40, null=True)

    def get_url(self):
        return reverse('book-info', args=[self.id])

    def __str__(self):
        return f'{self.title} - {self.rating}'
