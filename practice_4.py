""" Write a function that computes the volume of a sphere given its radius.

The volume of a sphere is given as 4/3 pi r cube """

def vol(rad):
    return (4/3) * 3.14 * (rad * rad * rad)

vol(2)

""" Write a function that checks whether a number is in a given 
range (inclusive of high and low) """

def ran_check(num,low,high):
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

