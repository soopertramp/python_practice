""" Write a function that computes the volume of a sphere given its radius.

The volume of a sphere is given as 4/3 pi r cube """

def vol(rad):
    
    """Write a function that computes the volume of a sphere

    Returns:
        Computes the volume of a sphere given its radius.
    """
    
    return (4/3) * 3.14 * (rad * rad * rad)

vol(2)

""" Write a function that checks whether a number is in a given 
range (inclusive of high and low) """

def ran_check(num,low,high):
    
    """Write a function that checks whether a number is in a given 
       range (inclusive of high and low)
    
    Returns:
        Write a function that checks whether a number is in a given 
        range (inclusive of high and low)
    """
    
    if num >= low and num <= high:
        print(f'{num} is in the range {low} and {high}')
    else:
        print(f'{num} is not in the range {low} and {high}')
    
ran_check(5,2,7)

ran_check(100,2,7)

# If you only wanted to return a boolean:

def ran_check(num,low,high):
    if num >= low and num <= high:
        return True
    else:
        return False
    
ran_check(5,2,7)

ran_check(100,2,7)

""" Write a Python function that accepts a string and calculates the number of upper case letters 
and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33
HINT: Two string methods that might prove useful: .isupper() and .islower()

If you feel ambitious, explore the Collections module to solve this problem! """

def up_low(s):
    
    """Write a Python function that accepts a string

    Returns:
        Calculates the number of upper case letters 
        and lower case letters.
    """
    
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return (f"No. of Upper case characters : {upper_count}\n" 
            f"No. of Lower case Characters : {lower_count}")

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

""" Write a Python function that takes a list and returns a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5] """

def unique_list(lst):
    
    """Write a Python function that takes a list
    
    Returns:
        Returns a new list with unique elements of the first list.
         
    """
    
    lst1 = set(lst)
    lst2 = list(lst1)
    print(lst2)
    
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

""" Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24 """

def multiply (numbers):
    product = 1
    for i in numbers:
        product = product * i
        print(product)
        
multiply([1,2,3,-4])

def multiply (numbers):
    product = 1
    for i in numbers:
        product = product * i
    return product
        
multiply([1,2,3,-4])

""" Write a Python function that checks whether a word or phrase is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, 
e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() 
method in a string to help out with dealing with spaces. Also google search how to reverse a string
in Python, there are some clever ways to do it with slicing notation. """

def palindrome(s):
    if s[::-1] == s[::]:
        print(s)
    else:
        print('Invalid')
        
palindrome('helleh')

palindrome('pradeep')

def palindrome(s):
    return s[::-1] == s[::]

palindrome('helleh')

palindrome('pradeep')

""" Write a Python function to check whether a string is pangram or not. 
(Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
Hint: You may want to use .replace() method to get rid of spaces.

Hint: Look at the (string method)[https://stackoverflow.com/questions/16060899/alphabet-range-in-python]

Hint: In case you want to use (set comparisons)[https://betterprogramming.pub/a-visual-guide-to-set-comparisons-in-python-6ab7edb9ec41] """



