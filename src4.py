'''
1. Write Python code to open a file named demo.txt and write some random data into it.

2. Open the file, read the contents and display them as output.

3. Write python code to add additional text to the existing file on a new line without deleting the previous contents.
'''

# writing data to the file

f = open('demo.txt', 'w')
f.write("hello there")
f.close()

# reading data from the file

f = open('demo.txt', 'r')
print(f.read())
f.close()