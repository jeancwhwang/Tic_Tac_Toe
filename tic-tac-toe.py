print('Let\'s play Tic-Tac-Toe with your friend!')
print('Use your computer keypad as a reference for a three-by-three grid as below.')
print()
print('7' + '|' + '8' + '|' + '9')
print('-+-+-')
print('4' + '|' + '5' + '|' + '6')
print('-+-+-')
print('1' + '|' + '2' + '|' + '3')
print()
print('Please enter a number from 1-9.')
# Create the board-as-a-dictionary in a variable
theBoard = {'7': ' ', '8': ' ', '9':' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3':' '}

# Create a function to print the board dictionary
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Tic-tac-toe game
turn = 'X'
for i in range (9):
    printBoard(theBoard)
    print('Turn for' + ' '+ '"' +turn +'"'+ '. Move on which place?')
    move = input('Position:')
    count = i + 1
    print('Round:' + str(count) )

    # Constraint: cannot fill in the same place
    if theBoard[move] == ' ':
        theBoard[move] = turn
    else:
        print("Please choose another place. This place has been filled.")
        i = i - 1 # Do not increment i to keep the same 'X' or 'O'
        continue

    # Victory conditions
    if theBoard['7'] == theBoard['8'] == theBoard['9'] !=' ': # Top row connected
        printBoard(theBoard)
        print('Game Over!' + ' ' +'"'+ turn +'"' + ' ' + 'Won! Congradulations!')
        break

    elif theBoard['4'] == theBoard['5'] == theBoard['6'] !=' ': # Middle row connected
        printBoard(theBoard)
        print('Game Over!' + ' ' +'"'+ turn +'"' + ' ' + 'Won! Congradulations!')
        break

    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # Bottom row connected
        printBoard(theBoard)
        print('Game Over!' + ' ' +'"'+ turn +'"' + ' ' + 'Won! Congradulations!')
        break

    elif theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ': # Left column connected
        printBoard(theBoard)
        print('Game Over!' + ' ' +'"'+ turn +'"' + ' ' + 'Won! Congradulations!')
        break
    elif theBoard['8'] == theBoard['5'] == theBoard['2'] != ' ': # Middle column connected
        printBoard(theBoard)
        print('Game Over!' + ' ' +'"'+ turn +'"' + ' ' + 'Won! Congradulations!')
        break

    elif theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ': # Right column connected
        printBoard(theBoard)
        print('Game Over!' + ' ' +'"'+ turn +'"' + ' ' + 'Won! Congradulations!')
        break

    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # Left diagonal line connected
        printBoard(theBoard)
        print('Game Over!' + ' ' +'"'+ turn +'"' + ' ' + 'Won! Congradulations!')
        break

    elif theBoard['9'] == theBoard['5'] == theBoard['1'] != ' ': # Right diagonal line connected
        printBoard(theBoard)
        print('Game Over!' + ' ' +'"'+ turn +'"' + ' ' + 'Won! Congradulations!')
        break

    # Change the plaer - either 'X' or 'O'
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

    # Show if there is no winner
    if i == 9:
        print('It is a tie! Good game!')
