# Test your knowledge. 
# Answer the following Questions

# Numbers: 1, 5, 20

# Strings: "Pradeep"

# Lists: [1, 2, "pradeep", 3.4]

# Tuples: (1, 2, "pradeep", 3.4)

# Dictionaries: {"a" : "pradeep", "b" : "chandra", "c" : 10}

# Numbers
#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

#Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

x = 100
y = 10
z = 1
a = 4

c = (x ** 2) / y + (z/a)

# Answer these 3 questions without typing code. Then type code to check your answer.

# What is the value of the expression 4 * (6 + 5) = 44

# What is the value of the expression 4 * 6 + 5 = 29

# What is the value of the expression 4 + 6 * 5 = 34

4 * (6 + 5)

4 * 6 + 5

4 + 6 * 5

# What is the type of the result of the expression 3 + 1.5 + 4? = float

a = 3 + 1.5 + 4
type(a)

# What would you use to find a number’s square root, as well as its square?

10 ** 2 #square

import math

number = 121

square_root = math.sqrt(number)
print(square_root)

# Strings
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

s = 'hello'
# Print out 'e' using indexing

s[1]

# Reverse the string 'hello' using slicing:

s ='hello'
# Reverse the string using slicing

s[::-1]

# Given the string hello, give two methods of producing the letter 'o' using indexing.

s ='hello'
# Print out the 'o'
# Method 1:

s[4]

# Method 2:

s[-1]

# Lists
#Build this list [0,0,0] two separate ways.

# Method 1:

list1 = []

for i in range(3):
    list1.append(0)
    
list1

# Method 2:

list_2 = [0 for i in range(3)]

list_2