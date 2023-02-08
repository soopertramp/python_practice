""" Some suggested tools before you get started:
To take input from a user:

player1 = input("Please pick a marker 'X' or 'O'")
Note that input() takes in a string. If you need an integer value, use

position = int(input('Please enter a number'))

To clear the screen between moves:

from IPython.display import clear_output
clear_output()
Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:

print('\n'*100)
This scrolls the previous board up out of view. Now on to the program!

Step 1: Write a function that can print out a board. Set up your board as a list, where each 
index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation. """

def display_board(board):
    
    """
    This function takes a list representing a tic-tac-toe board as input, and 
    prints it out in a 3x3 format, where each index 1-9 corresponds with a 
    number on a number pad.
    
    Args:
    board: A list of length 9 representing the tic-tac-toe board, where each 
           index 1-9 corresponds with a number on a number pad.
           For example: board = ['X', 'O', 'X', 'O', 'O', 'X', 'X', 'O', 'X']
    
    Returns:
    None
    """
    
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

""" Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. 
Think about using while loops to continually ask until you get a correct answer."""

def player_input():
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, choose X or O: ").upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
player_input()


