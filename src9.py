'''
Consider a list in Python which includes prices of all the items in a store.

Build a function to discount the price of all the products by 10%.

Use map to apply the function to all the elements of the list so that all the product prices are discounted.
'''

price_list = [10, 20, 30, 40, 50]

result = list(map(lambda x: x*0.9, price_list))
print(result)

'''
def discount(price):
    price = price - (price * 10) / 100
    return price
 
product_prices = [100, 200, 300, 400, 500]
 
updated_prices = list(map(discount,product_prices))
 
print(updated_prices)
'''