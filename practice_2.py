# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'

st.split()

for word in st.split():
    if word[0] == 's':
        print(word)
        
# Use range() to print all the even numbers from 0 to 10

list(range(0,10,2))
    
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

for i in range(1,51):
    if i % 3 == 0:
        print(i) 
        
a = [i for i in range(1,51) if i % 3 == 0]
a

# Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word) % 2 == 0:
        print(word)
        
""" Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" 
instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of 
both three and five print "FizzBuzz"."""

lst = list(range(1,101))
lst

for number in lst:
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)
        
for number in lst:
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)

# Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'

for word in st.split():
    print(word[0])
    
[word[0] for word in st.split()] 