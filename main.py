import os

with open('product-names.txt') as pr:
    product_list = [line.rstrip('\n') for line in pr]

for products in product_list:
    os.mkdir(products)
    
