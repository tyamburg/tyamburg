##########################################################################
#                                                                        #
#                           Name: Tyler Amburgey                         #
#                          Date: 3/11/2021                               #
#                   This program creates an AI, with which the user      #
#                   can play a game of Tic Tac Toe.                      #
#                                                                        #
#                                                                        #
#                                                                        #
# ########################################################################

#import packages
import datetime
import getpass
import random

#create a variable that contains the date and time
t = datetime.datetime.now()   
#display the month, day, and year in format
print(str(t.month) + '/' + str(t.day) + '/' + str(t.year))
#display username
print(getpass.getuser())
print()
#create a function that displays the board from the strings created below
def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


#create a function that lets the player choose their letter and then creates a list of the player's letter and the computer's
def inputPlayerLetter():


    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
#uses random to choose wh will go first the player of the computer
def whoGoesFirst():

    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
#create a function that determines, whether or not the player wants to play again
def playAgain():

    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter
#create the function that determines whether or not the computer or player has won
def isWinner(bo, le):


    return ((bo[7] == le and bo[8] == le and bo[9] == le)) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[7] == le and bo[4] == le and bo[1] == le) or(bo[8] == le and bo[5] == le and bo[2] == le) or(bo[9] == le and bo[6] == le and bo[3] == le) or(bo[7] == le and bo[5] == le and bo[3] == le) or(bo[9] == le and bo[5] == le and bo[1] == le)

def getBoardCopy(board):
    #make duplicate of board
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    #returns true if the move is free on the board
    return board[move] == ' '

def getPlayerMove(board):
    #lets player type in move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    #returns the move if it is available, or returns none if there is no valid move

    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    #creates computer's move
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    #creates algorithm for computer's move
    #check if player can win with next move or block them
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    #block player's next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    #take corners if free
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    #take center if open
    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    #return true if board is full or false if not
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe!')

while True:

    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            #player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        #computer's turn
        else:

            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else: 
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break


                
            

