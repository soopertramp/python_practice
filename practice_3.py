""" Function Practice Exercises
Problems are arranged in increasing difficulty:

Warmup - these can be solved using basic comparisons and methods
Level 1 - these may involve if/then conditional statements and simple methods
Level 2 - these may require iterating over sequences, usually with some kind of loop
Challenging - these will take some creativity to solve 

WARMUP SECTION:
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5 """

def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)

lesser_of_two_evens(2,4)

lesser_of_two_evens(2,5)

""" ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with 
same letter

animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False """

def animal_crackers(text):
    texts = text.split()
    return texts[0][0] == texts[1][0]
        
animal_crackers('Levelheaded Llama')

animal_crackers('Crazy Kangaroo')

""" MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the 
integers is 20. If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False """

def makes_twenty(n1,n2):
    return n1 + n2 == 20
        
    
makes_twenty(20,10)

makes_twenty(12,8)

makes_twenty(2,3)

makes_twenty(20,0)

""" LEVEL 1 PROBLEMS
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald
Note: 'macdonald'.capitalize() returns 'Macdonald' """

def old_macdonald(name):
    if len(name) < 4:
        return name.capitalize()
    else:
        return name[:3].capitalize() + name[3:].capitalize()
    
old_macdonald('macdonald')

old_macdonald('pradeep')    

""" MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
Note: The .join() method may be useful here. The .join() method allows you to join together strings 
in a list with some connector string. For example, some uses of the .join() method:

>>> "--".join(['a','b','c'])
>>> 'a--b--c'
This means if you had a list of words you wanted to turn back into a sentence, you could just join them 
with a single space string:

>>> " ".join(['Hello','world'])
>>> "Hello world" """

def master_yoda(text):
    words = text.split()
    return " ".join(words[::-1])
    
master_yoda('I am home')

master_yoda('We are ready')

""" ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True
NOTE: abs(num) returns the absolute value of a number """

def almost_there(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

almost_there(90)

almost_there(104)

almost_there(150)

almost_there(209)

""" LEVEL 2 PROBLEMS
FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False """

## Doubts

def has_33(nums):
    for num in range(len(nums) - 1):
        if nums[num] == 3 and nums[num + 1] == 3:
            return True
    return False
    
has_33([1, 3, 3])

has_33([1, 3, 1, 3])

has_33([3, 1, 3])

""" PAPER DOLL: Given a string, return a string where for every character in the original 
there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii' """

def paper_doll(text):
    for char in text.split():
        for char in text:
            print(char*3)

paper_doll('Hello')

paper_doll('Mississippi')

""" BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, 
return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19 """

def blackjack(a,b,c):
    #for i in a,b,c:
        if (a+b+c) <= 21:
            return (a+b+c)
        elif (a+b+c) > 21 and (a+b+c) == 11:
            return (a+b+c) - 10
        elif (a+b+c) > 21:
            return "Bust"
 
blackjack(5,6,7)   

blackjack(9,9,9)  

blackjack(9,9,11) 

# Doubt 1 - For loop and last condition 
# Doubt 2 - 

def blackjack(a,b,c):
    total = a + b + c
    if total <= 21:
        return total
    elif 11 in [a,b,c] and total <= 31:
        return total - 10
    else:
        return "Bust"     
    
blackjack(5,6,7)   

blackjack(9,9,9)  

blackjack(9,9,11)

""" SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting 
with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14 """

# def summer_of_69(arr):
#     sum = 0
#     add = True
#     for num in arr:
#         if num == 6:
#             add = False
#         if add:
#             sum += num
#         if num == 9:
#             add = True
#     return sum
    
# summer_69([1, 3, 5])

""" CHALLENGING PROBLEMS
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False """
 
# def spy_game(nums):
#     for num in nums:
#         if [0,0,7] in nums:
#             return True

def spy_game(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
        
spy_game([1,2,4,0,0,7,5])

spy_game([1,0,2,4,0,5,7])

spy_game([1,7,2,0,4,5,0])

""" COUNT PRIMES: Write a function that returns the number of prime numbers 
that exist up to and including a given number
count_primes(100) --> 25
By convention, 0 and 1 are not prime. """

def count_primes(num):
    if num < 2:
        return 0
    primes = [True] * (num + 1)
    p = 2
    while p ** 2 <= num:
        if primes[p]:
            for i in range(p ** 2, num + 1, p):
                primes[i] = False
        p = p + 1
    return sum(primes[2:])

count_primes(100)

count_primes(1000)

""" Just for fun:
PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation 
of that letter print_big('a')

out:   *  
      * *
     *****
     *   *
     *   *
HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
For purposes of this exercise, it's ok if your dictionary stops at "E". """

def print_big(letter):
    patterns = {
        'a': ['  *  ', ' * * ', '*****', '*   *', '*   *'],
        'b': ['**** ', '*   *', '**** ', '*   *', '**** '],
        'c': [' *** ', '*    ', '*    ', '*    ', ' *** '],
        'd': ['**** ', '*   *', '*   *', '*   *', '**** '],
        'e': ['*****', '*    ', '*****', '*    ', '*****'],
    }
    alphabet = 'abcde'
    letter = letter.lower()
    if letter in alphabet:
        for pattern in patterns[letter]:
            print(pattern)
    else:
        print('This letter is not supported.')
        
print_big('b')

s = {'a': ['  *  ', ' * * ', '*****', '*   *', '*   *']}

for a in s:
    print(s["a"])