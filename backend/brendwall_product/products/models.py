from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from products.validators import TitleValidator, TextValidator
from products.constants import MIN_PRODUCT_PRICE, MAX_PRODUCT_PRICE


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
