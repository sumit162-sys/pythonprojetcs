'''
Create a BMI calculator, BMI which stands for Body Mass Index can be calculated using the formula:



 BMI = (weight in Kg)/(Height in Meters)^2.


Write python code which can accept the weight and height of a person and calculate his BMI.

note: Make sure to use a function which accepts the height and weight values and returns the BMI value.
'''

def BMC(w, h):
    BMI= w/pow(h, 2)
    return BMI


w = float(input('Enter the weight of the person'))
h = float(input('Enter the height of the person'))

#print(type(w))
#print(type(h))

c = BMC(w, h)

print('The BMI value='+str(c))