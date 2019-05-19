import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Collection(models.Model):
    '''
    A collection of cards.
    '''
    name = models.CharField(max_length=250)


class Card(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    team = models.CharField(max_length=100)
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1887),  # first produced baseball card (source?)
            MaxValueValidator(datetime.datetime.now().year),
        ],
        help_text='Use the following format: <YYYY>',
    )
    company = models.CharField(max_length=250)
    value = models.DecimalField(
        decimal_places=2,
        max_digits=50,
        default=0,
    )

    collection = models.ManyToManyField(Collection)
