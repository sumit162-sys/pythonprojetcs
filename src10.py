'''
Using the concept of object oriented programming and inheritance, create a super class named Computer, which has two sub classes named Desktop and Laptop.


Define two methods in the Computer class named getspecs and displayspecs, to get the specifications and display the specifications of the computer.


You can use any specifications which you want.
The Desktop class and the Laptop class should have one specification which is exclusive to them for example laptop can have weight as a special specification.


Make sure that the sub classes have their own methods to get and display their special specification.

Create an object of laptop/ desktop and make sure to call all the methods from the computer class as well as the methods from the own class
'''

class Computer:
    def __init__(self,type):
        self.type = type

    def getspecs(self):
        self.type = input("Enter the type of computer")

    def displayspecs(self):
        print(self.type)

class laptop(Computer):
    def lapi(self):
        print("The laptop weight is 4kg")

class Desktop(Computer):
    def deski(self):
        print("The desktop weigth is 7kg")

lap1 = laptop(" ")
lap1.getspecs()
lap1.displayspecs()
lap1.lapi()

dek1=Desktop(" ")
dek1.getspecs()
dek1.displayspecs()
dek1.deski()