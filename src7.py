'''
Assume you want to build two functions for discounting products on a website.
Function number 1 is for student discount which discounts the current price to 10%.
Function number 2 is for additional discount for regular buyers which discounts an additional 5% on the current student discounted price.
Depending on the situation, we want to be able to apply both the discounts on the products.

Design the above two mentioned functions and apply them both simultaneously on the price.
'''

def st(p1):
    cp1 = 0.9*p1
    return cp1



def reg(func, arg):
    x = func(arg)
    s = 0.95*x
    return s

a= input("Are you a Student or Regular Customer, type S or R accordingly")
b = int(input("Enter the product cost"))

if a == 'S':
    print("The discounted price for student is " + str(st(b)))


if a == 'R':
    print("The discounted price for Regular Customer is " + str(reg(st, b)))


'''
def student_discount(price):
    price = price - (price * 10) / 100
    return price
 
def additional_discount(newprice):
    newprice = newprice - (newprice * 5) / 100
    return newprice
 
selling_price = 100
 
#applying both discounts simultaneously
 
print(additional_discount(student_discount(selling_price)))
'''














