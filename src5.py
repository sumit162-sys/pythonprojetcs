'''
Write Python code which accepts name of a product and in turn returns their respective prices.



Make sure to use dictionaries to store products and their respective prices.


The dictionary should include at least 5 elements.
'''

product = {"milk": 200, "potato": 40, "orange": 22, "leafy": 30, "ticket": 3000}

newproduct = input("PLease enter the name of the product")

#print("The price of the product is: " + str(pr[sd]))

if(newproduct in product):
    print(product.get(newproduct))
else:
    print('Product Not Found')


