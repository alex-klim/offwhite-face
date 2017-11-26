from celery import shared_task
from .models import Product, Price


@shared_task(name='add_product')
def add_product(item):
#    for item in items:
    product = Product(
        site_product_id=item.get('site_product_id'),
        name=item.get('name'),
        categories=item.get('categories'),
        description=item.get('description'),
        material=item.get('material'),
        url=item.get('url'),
        images=item.get('images'),
        site=item.get('site')
    )
    product.save()


@shared_task(name='add_price')
def add_price(item):
#    for item in items:
    price = Price(
        site_product_id = item.get('site_product_id'),
        price = item['params']['price'],
        size = item['params']['size'],
        color = item['params']['color'],
        stock_level = item.get('stock_level'),
        currency = item.get('currency')
    )
    price.save()
