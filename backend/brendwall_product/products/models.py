from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from products.constants import MAX_PRODUCT_PRICE, MIN_PRODUCT_PRICE
from products.validators import TextValidator, TitleValidator


class Product(models.Model):
    '''Database model for the Product entity.'''

    title = models.CharField(
        verbose_name='Название',
        max_length=128,
        blank=False,
        null=False,
        validators=(TitleValidator(), )
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=512,
        blank=False,
        null=False,
        validators=(TextValidator(), )
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        verbose_name='Цена',
        blank=False,
        null=False,
        validators=(MinValueValidator(MIN_PRODUCT_PRICE),
                    MaxValueValidator(MAX_PRODUCT_PRICE))
    )
