import os

with open('product-names.txt') as pr:
    product_list = [line.rstrip('\n') for line in pr]

with open('subfolder-names.txt') as sub:
    subfolder_list = [line.rstrip('\n') for line in sub]

for products in product_list:
    os.mkdir(products)
    
for subfolders in subfolder_list:
    os.mkdir(products + '/' + subfolders)
