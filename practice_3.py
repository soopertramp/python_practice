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
    
