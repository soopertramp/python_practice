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

# pemdas

x = 10
y = 1
z = 1
a = 4

c = (x ** 2) / y + (z/a)

print(c)

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

list3 = [0]*3
print(list3)

# Method 2:

list_2 = [0 for i in range(3)]

list_2

# Reassign 'hello' in this nested list to say 'goodbye' instead:

list3 = [1,2,[3,4,'hello']]

list3[2][2] = "goodbye"

list3

# Sort the list below:

list4 = [5,3,4,6,1]

list5 = list4.sort()

list4

list5 = [5,3,4,6,1]

print(list5)

s = sorted(list5)

sorted([5, 2, 3, 1, 4])

print(list5)

#Dictionaries¶
# Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}
# Grab 'hello'

d['simple_key']

d = {'k1':{'k2':'hello'}}
# Grab 'hello'

d['k1']['k2']

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello

d['k1'][0]['nest_key'][1][0]

# This will be hard and annoying!

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

d['k1'][2]['k2'][1]['tough'][2][0]

tupl = (1,2,'pradeep')

# Use a set to find the unique values of the list below:

list5 = [1,2,2,33,4,4,11,22,3,3,2]

set(list5)

2 > 3

3 <= 2

3 == 2.0

3.0 == 3

4**0.5 != 2

# What is the boolean output of the cell block below?

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']