import random
import operator
import numpy as np

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

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.uniform(0, 1) < 0.5:
        return 'computer'
    else:
        return 'player'

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def checkCorner(i):
    return i in '1 3 7 9'.split()

def twoSame(board, le, flag):
    counter_2 = 0
    counter_1 = 0
    i = 1
    if board[i] == le and isSpaceFree(board,i+1) and isSpaceFree(board,i+2):
        counter_1 += 1
    if board[i] == le and isSpaceFree(board,i+3) and isSpaceFree(board,i+6):
        counter_1 += 1
    if board[i] == le and isSpaceFree(board,i+4) and isSpaceFree(board,i+8):
        counter_1 += 1
    if board[i] == le and (isSpaceFree(board,i+1) and board[i+2] == le) \
        or(isSpaceFree(board,i+2) and board[i+1] == le):
        counter_2 += 1
    if board[i] == le and (isSpaceFree(board,i+3) and board[i+6] == le) \
        or(isSpaceFree(board,i+6) and board[i+3] == le):
        counter_2 += 1
    if board[i] == le and (isSpaceFree(board,i+4) and board[i+8] == le) \
        or(isSpaceFree(board,i+8) and board[i+4] == le):
        counter_2 += 1
    i = 2
    if board[i] == le and isSpaceFree(board,i+3) and isSpaceFree(board,i+6):
        counter_1 += 1
    if board[i] == le and (isSpaceFree(board,i+3) and board[i+6] == le) \
        or(isSpaceFree(board,i+6) and board[i+3] == le):
        counter_2 += 1
    i = 3
    if board[i] == le and isSpaceFree(board,i+2) and isSpaceFree(board,i+4):
        counter_1 += 1
    if board[i] == le and isSpaceFree(board,i+3) and isSpaceFree(board,i+6):
        counter_1 += 1
    if board[i] == le and (isSpaceFree(board,i+2) and board[i+4] == le) \
        or(isSpaceFree(board,i+4) and board[i+2] == le):
        counter_2 += 1
    if board[i] == le and (isSpaceFree(board,i+3) and board[i+6] == le) \
        or(isSpaceFree(board,i+6) and board[i+3] == le):
        counter_2 += 1
    i = 4
    if board[i] == le and isSpaceFree(board,i+1) and isSpaceFree(board,i+2):
        counter_1 += 1
    if board[i] == le and (isSpaceFree(board,i+1) and board[i+2] == le) \
        or(isSpaceFree(board,i+2) and board[i+1] == le):
        counter_2 += 1
    i = 7
    if board[i] == le and isSpaceFree(board,i+1) and isSpaceFree(board,i+2):
        counter_1 += 1
    if board[i] == le and (isSpaceFree(board,i+1) and board[i+2] == le) \
        or(isSpaceFree(board,i+2) and board[i+1] == le):
        counter_2 += 1
    if flag == 0:
        counter_1 *= -1
        counter_2 *= -1
    return counter_2, counter_1

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def valuePerMove(x, W_):
    value = dict()
    count = 0
    for action in list(x.keys()):
        current_x = x[action]
        V = np.dot(W_,current_x)
        value[action] = V
        count +=1
    return value, count-1

def getComputerMove(board, letter, W_):
    x = dict()
    le_2 = ' '
    if letter == 'X':
        le_2 = 'O'
    else:
        le_2 = 'X'
    for i in range(1, 10):
        action = np.zeros(8)
        copy = getBoardCopy(board)
        if isSpaceFree(board, i):
            flag = 0
            action[5], action[6]= twoSame(board, le_2,flag)
            if isWinner(board,le_2):
                action[7] = -1
            flag = 1
            makeMove(copy, letter, i)
            if checkCorner(i): #x1
                action[0] = 1
            elif i == 5: #x2
                action[1] = 1
            action[2], action[3]= twoSame (copy, letter,flag)
            if isWinner(copy,letter):
                action[4] = 1
            x[i] = action
    value, count = valuePerMove(x, W_)
    sorted_value = sorted(value.items(),key=lambda kv: kv[1])
    return sorted_value[count][0]

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    w_ = np.zeros(8)
    if turn == 'player':
        w_ = np.array([0.02227454, 19.85128151, 18.35634497,  0.02104893, 12.7009537, 0.40323984, 16.21561339, 0.0334978])
    else:
        w_ = np.array([0.18317548, 0.23648715, 0.15609095, 0., 0.4703796, 0.10005051, 0.41351731, 0.41262119])
    #--------------------- start -----------------------------
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            # Player’s turn.
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
        else:
            # Computer’s turn.
            move = getComputerMove(theBoard, computerLetter, w_)
            makeMove(theBoard,computerLetter,move)
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