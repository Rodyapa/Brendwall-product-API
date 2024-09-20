from django.test import TestCase
from django.urls import reverse
from products.models import Product
from products.constants import MIN_PRODUCT_PRICE, MAX_PRODUCT_PRICE


'''
These tests do not check the internal workings of the ORM model.

We aim to write tests that are stable and not fragile to code refactoring
or implementation details.

The tests should verify the expected behavior of the system.
'''


class ProductAPITestCase(TestCase):
    """
    Test suite related to the Product API.
    """

    def test_creation_product_instance_with_valid_data(self):
        '''Test that a product with valid data can be created.'''

        # Arrange
        valid_data = {
            'title': 'Maccaroni',
            'description': 'Awesome pasta Maccaroni',
            'price': MIN_PRODUCT_PRICE
        }
        url = reverse('products:product-create')
        counter_before_creation = Product.objects.filter(**valid_data).count()

        # Act
        response = self.client.post(url, valid_data)

        # Assert
        counter_after_creation = Product.objects.filter(**valid_data).count()
        self.assertEqual(response.status_code, 201,
                         f'{response.data}, {MIN_PRODUCT_PRICE} '
                         'Backend should respond with a 201 code')
        self.assertEqual(
            (counter_after_creation - counter_before_creation), 1,
            "There should be exactly one more product after creation. \n"
            f"Products before creation: {counter_before_creation} \n"
            f"Products after creation: {counter_after_creation}"
        )

    def test_creation_instance_with_invalid_data(self):
        '''Test that a product with invalid data cannot be created.'''

        # Arrange
        counter_before_creation = Product.objects.all().count()
        url = reverse('products:product-create')
        test_cases = [
            ('missing title', {
                'description': 'Awesome pasta Maccaroni',
                'price': MIN_PRODUCT_PRICE
            }),
            ('missing description', {
                'title': 'Maccaroni',
                'price': MIN_PRODUCT_PRICE
            }),
            ('missing price', {
                'title': 'Maccaroni',
                'description': 'Awesome pasta Maccaroni',
            }),
            ('unacceptable title symbols', {
                'title': '<Maccaroni></Maccaroni>',
                'description': 'Awesome pasta Maccaroni',
                'price': MIN_PRODUCT_PRICE
            }),
            ('unacceptable description symbols', {
                'title': 'Maccaroni',
                'description': '<script>scam</script>',
                'price': MIN_PRODUCT_PRICE
            }),
            ('unacceptable price type', {
                'title': 'Maccaroni',
                'description': 'Awesome pasta Maccaroni',
                'price': 'a lot'
            }),
            ('unacceptable small price', {
                'title': 'Maccaroni',
                'description': 'Awesome pasta Maccaroni',
                'price': (MIN_PRODUCT_PRICE - 1)
            }),
            ('unacceptable large price', {
                'title': 'Maccaroni',
                'description': 'Awesome pasta Maccaroni',
                'price': (MAX_PRODUCT_PRICE + 1)
            }),
        ]

        # Act
        for expected_failure_cause, invalid_data in test_cases:
            with self.subTest(expected_failure_cause=expected_failure_cause,
                              invalid_data=invalid_data):
                response = self.client.post(url, invalid_data)

                # Assert
                counter_after_creation = Product.objects.all().count()
                self.assertEqual(response.status_code, 400,
                                 f'Backend should respond with a 400 code '
                                 'because the data passed had '
                                 f'{expected_failure_cause}')
                self.assertEqual(
                    counter_before_creation,
                    counter_after_creation,
                    'The number of products should not change after a '
                    'failed attempt to create a new product. \n'
                    f'Before attempt: {counter_before_creation} \n'
                    f'After attempt: {counter_after_creation}')

    def test_getting_product_list(self):
        '''Test the ability to retrieve the product list.'''
        # Arrange
        url = reverse('products:product-list')
        Product.objects.bulk_create(
            [
                Product(title='Papaya', description='fruit',
                        price=MIN_PRODUCT_PRICE),
                Product(title='Blender', description='software',
                        price=MIN_PRODUCT_PRICE),
                Product(title='Toyota', description='auto',
                        price=MAX_PRODUCT_PRICE)
            ]
        )
        # Act
        response = self.client.get(url)
        # Assert
        self.assertEqual(response.status_code, 200,
                         'User should get a response with a 200 status code.')
        self.assertEqual(response.headers['Content-Type'],
                         'application/json',
                         'The response should be in JSON format.')
