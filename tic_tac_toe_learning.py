import random
import operator
import numpy as np

#features:
#corner center num_of_win_me num_win_else
# x1 = corner 
# X2 = center
# x3 = # of instances where there are 2 x's in a row with an open subsequent square.
# x4 = # of instances where there is an x in a completely open row.
# x5 = # of instances of 3 x's in a row (value of 1 signifies end game)
# x6 = # of instances where there are 2 o's in a row with an open subsequent square.
# x7 = # of instances where there is an o in a completely open row.
# x8 = # of instances of 3 o's in a row (value of 1 signifies end game)

def initializeFirstTime():
    w = np.zeros(8)
    for i in range (8):
        w[i] = random.uniform(0,.5)
    return w

def isSpaceFree(board, i):
    return board[i] == ' '

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
    '''if flag == 0:
        counter_1 *= -1
        counter_2 *= -1'''
    return counter_2, counter_1

def valuePerMove(x, W_):
    value = dict()
    count = 0
    for action in list(x.keys()):
        current_x = x[action]
        V = np.dot(W_,current_x)
        value[action] = V
        count +=1
    return value, count-1

def getAgentMove(board, letter, W_):
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
            action[2], action[3]= twoSame(copy, letter, flag)
            if isWinner(copy,letter):
                action[4] = 1   
        x[i] = action
    value, count = valuePerMove(x, W_)
    sorted_value = sorted(value.items(),key=lambda kv: kv[1])
    return sorted_value[count][0], sorted_value[count][1], x[sorted_value[count][0]]

def updateW(w, value_move, x_move, current_V, le, theBoard):
    learning_rate = 0.02
    if isWinner(theBoard, le):
        current_V = 100
    elif isBoardFull(theBoard):
        current_V =  0
    else:
        if le == 'X':
            le2 = 'O'
        else:
            le2 = 'X'
        if isWinner(theBoard,le2):
            current_V = -100
    w += learning_rate*(current_V - value_move)*x_move
    return w

itter = 1
W_A = initializeFirstTime()
W_B = initializeFirstTime()
current_V_A = 0
current_V_B = 0
while itter < 10
0:
    print(itter)

    theBoard = [' '] * 10
    agent_A = 'X'
    agent_B = 'O'

    turn = 'agent_A'
    gameIsPlaying = True

    while gameIsPlaying:
        move, value_move, x_move =  0, 0, 0
        if turn == 'agent_A':
            move, value_move, x_move = getAgentMove(theBoard, agent_A, W_A)
            makeMove(theBoard,agent_A,move)
            W_A = updateW(W_A, value_move, x_move, current_V_A, agent_A, theBoard)
            current_V_A = value_move
            if isWinner(theBoard,agent_A):
                gameIsPlaying= False
                print('     X win')
            else:
                if isBoardFull(theBoard):
                    print('     tie')
                    break
                else: 
                    turn = 'agent_B'
        else:
            move, value_move, x_move = getAgentMove(theBoard, agent_B, W_B)
            makeMove(theBoard,agent_B,move)
            W_B = updateW(W_B, value_move, x_move, current_V_B, agent_B, theBoard)
            current_V_B = value_move
            if isWinner(theBoard,agent_B):
                gameIsPlaying= False
                print('     O win')
            else:
                if isBoardFull(theBoard):
                    print('tie')
                    break
                else: 
                    turn = 'agent_A'
    itter += 1
print(W_A)
print(W_B)