from django.core.management import BaseCommand
import datetime
class Command(BaseCommand):

    def handle(self, *args, **options):
        product_name = input('Название продукта: ')
        desc = input('Описание продукта: ')
        cat = input('Категория продукта: ')
        price = input('Цена продукта: ')
        create_data = datetime.date
        edit_data = datetime.date

        product_data = {
                'product_name':product_name,
                'product_desc':desc,
                'product_pic':'Null',
                'product_cat':cat,
                'product_price':price,
                'product_mk':create_data,
                'product_ed':edit_data
            }
        Product.objects.create(**product_data)
