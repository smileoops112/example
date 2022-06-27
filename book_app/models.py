from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify as django_slugify
from django.core.validators import MinValueValidator, MaxValueValidator

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):
    """
    Overriding django slugify that allows to use russian words as well.
    """
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


class Writer(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):

    HRN = 'грн'
    USD = 'дол'
    EUR = 'евр'
    CHOICE_PRICE = [
        (HRN, 'грн'),
        (EUR, 'евро'),
        (USD, 'доллары')
    ]

    title = models.CharField(max_length=70)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    is_best_selling = models.BooleanField()
    author = models.CharField(max_length=40, null=True)
    choice = models.CharField(max_length=3, choices=CHOICE_PRICE, default=HRN)
    slug = models.SlugField(default='', null=False, db_index=True)

    def get_url(self):
        return reverse('book-info', args=[self.slug, ])

    def __str__(self):
        return f'{self.title} - {self.rating}'
