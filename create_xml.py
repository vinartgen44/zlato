import os
import re
from datetime import datetime

from services import total_price, price_free_tax
from time import sleep
from get_products import get_products
from decimal import Decimal


def create_xml(file_name):
    os.makedirs('results', exist_ok=True)
    products: list[dict] = []
    product = {}
    total_tax = []
    with open('template.xml', 'r', encoding='windows-1251') as f:
        template_str = f.read()
    notices = re.search(r'\d{10}', file_name).group()
    date = datetime.strptime(re.search(r'\d{4}-\d{2}-\d{2}', str(file_name)).group(), '%Y-%m-%d')
    new_date = date.strftime('%d.%m.%Y')
    template_content = ''
    total_price_not_tax = []
    total = []
    cols = get_products(f'{file_name}')
    for col in cols:
        product.update({

           'line_number': int(col[0]),
           'article': col[1],
           'name': col[2],
           'quantity': col[3],
           'price': Decimal(str(col[4]).replace(',', '.')),
           'tax': col[5],
           'tax_price': str(col[6]).replace(',', '.'),
           'price_free_tax': price_free_tax(float(col[4].replace(',', '.'))),

           'file_name': file_name,
       })

        template_content += f'<СведТов НомСтр=\'{product['line_number']}\' НаимТов=\'{product['name']}\' ОКЕИ_Тов=\'796\' КолТов=\'{product['quantity']}\' ЦенаТов=\'{product['price']}\' СтТовБезНДС=\'{product['price_free_tax']}\' НалСт=\'20%\' СтТовУчНал=\'{product['price']}\'><Акциз><БезАкциз>без акциза</БезАкциз></Акциз><СумНал><СумНал>{product["tax_price"]}</СумНал></СумНал><ДопСведТов НаимЕдИзм="шт"/><ИнфПолФХЖ2 Идентиф="Артикул" Значен="{product["article"]}"/></СведТов>\n'
        total.append(float(col[4].replace(',', '.')))
        total_tax.append(float(col[6].replace(',', '.')))
        total_price_not_tax.append(float(price_free_tax(float(col[4].replace(',', '.')))))
    products.append(product)
    for product in products:
        with open(f'results/{product['file_name'][5:-5]}.xml', 'w', encoding='windows-1251') as f:
            template_str = template_str.replace('{{notices}}', notices)
            template_str = template_str.replace('{{date}}', new_date)
            template_str = template_str.replace('{{total}}', str(total_price(total)),)
            template_str = template_str.replace('{{total_price_not_tax}}', total_price(total_price_not_tax))
            template_str = template_str.replace('{{total_tax}}', total_price(total_tax))
            template_str = template_str.replace('{{content}}', template_content)
            f.write(template_str)
            sleep(3)

