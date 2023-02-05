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