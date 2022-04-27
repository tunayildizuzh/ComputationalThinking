import numpy as np
import random
ROW_COUNT = 6
COLUMN_COUNT = 7
board = np.full((ROW_COUNT,COLUMN_COUNT), ' ')
#board = np.zeros((ROW_COUNT, COLUMN_COUNT))


# board[4][4] = 'X'
# board[4][5] = 'X'
# board[4][6] = 'X'



def space_is_free(position):
    for row in range(5, -1, -1):
        if board[row][position] == ' ':
            return True

    return False


def draw():
    for row in range(5,-1,-1):
        for col in range(7):
            if board[row][col] == ' ':
                return False

    return True

def wincheck():
    boardHeight = len(board[0])
    boardWidth = len(board)

    # check horizontal spaces
    for y in range(boardHeight):
        for x in range(boardWidth - 3):
            if board[x][y] ==  board[x + 1][y] and board[x][y] == board[x + 2][y] and board[x][y] == board[x + 3][y] and board[x][y] != ' ':
                return True

    # check vertical spaces
    for x in range(boardWidth):
        for y in range(boardHeight - 3):
            if board[x][y] == board[x][y + 1] and board[x][y] == board[x][y + 2] and board[x][y] == board[x][y + 3] and board[x][y] != ' ':
                return True

    # check / diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
            if board[x][y] == board[x + 1][y - 1] and board[x][y] == board[x + 2][y - 2] and board[x][y] == board[x + 3][y - 3] and board[x][y] != ' ':
                return True

    # check \ diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
            if board[x][y] == board[x + 1][y + 1] and board[x][y] == board[x + 2][y + 2] and board[x][y] == board[x + 3][y + 3] and board[x][y] != ' ':
                return True

    return False

def wincheckmark(mark):
    boardHeight = len(board[0])
    boardWidth = len(board)

    # check horizontal spaces
    for y in range(boardHeight):
        for x in range(boardWidth - 3):
            if board[x][y] == mark and board[x + 1][y] == mark and board[x + 2][y] == mark and board[x + 3][y] == mark:
                return True

    # check vertical spaces
    for x in range(boardWidth):
        for y in range(boardHeight - 3):
            if board[x][y] == mark and board[x][y + 1] == mark and board[x][y + 2] == mark and board[x][y + 3] == mark:
                return True

    # check / diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
            if board[x][y] == mark and board[x + 1][y - 1] == mark and board[x + 2][y - 2] == mark and board[x + 3][y - 3] == mark:
                return True

    # check \ diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
            if board[x][y] == mark and board[x + 1][y + 1] == mark and board[x + 2][y + 2] == mark and board[x + 3][y + 3] == mark:
                return True

    return False

def wincheck3(mark):
    boardHeight = len(board[0])
    boardWidth = len(board)

    # check horizontal spaces
    for y in range(boardHeight):
        for x in range(boardWidth - 3):
            if board[x][y] == mark and board[x + 1][y] == mark and board[x + 2][y] == mark:
                return True

    # check vertical spaces
    for x in range(boardWidth):
        for y in range(boardHeight - 3):
            if board[x][y] == mark and board[x][y + 1] == mark and board[x][y + 2] == mark:
                return True

    # check / diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
            if board[x][y] == mark and board[x + 1][y - 1] == mark and board[x + 2][y - 2] == mark:
                return True

    # check \ diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
            if board[x][y] == mark and board[x + 1][y + 1] == mark and board[x + 2][y + 2] == mark:
                return True

    return False

def wincheck2(mark):
    boardHeight = len(board[0])
    boardWidth = len(board)

    # check horizontal spaces
    for y in range(boardHeight):
        for x in range(boardWidth - 3):
            if board[x][y] == board[x + 1][y] and board[x][y] == mark:
                return True

    # check vertical spaces
    for x in range(boardWidth):
        for y in range(boardHeight - 3):
            if board[x][y] == board[x][y + 1] and board[x][y] == mark:
                return True

    # check / diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
            if board[x][y] == mark and board[x + 1][y - 1] == mark:
                return True

    # check \ diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
            if board[x][y] == mark and board[x + 1][y + 1] == mark:
                return True

    return False

def winning_move(mark):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == board[r][c + 1] and board[r][c] == board[r][c + 2] and board[r][c] == board[r][c + 3] and \
                    board[r][c] == mark:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == board[r + 1][c] and board[r][c] == board[r + 2][c] and board[r][c] == board[r + 3][c] and \
                    board[r][c] == mark:
                return True

    # Check positively sloped diagonals.
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == board[r + 1][c + 1] and board[r][c] == board[r + 2][c + 2] and board[r][c] == \
                    board[r + 3][c + 3] and board[r][c] == mark:
                return True

    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == board[r - 1][c + 1] and board[r][c] == board[r - 2][c + 2] and board[r][c] == board[r - 3][c + 3] and board[r][c] == mark:
                return True

def winning_move3(mark):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == board[r][c + 1] and board[r][c] == board[r][c + 2] and board[r][c] == mark:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == board[r + 1][c] and board[r][c] == board[r + 2][c] and board[r][c] == mark:
                return True

    # Check positively sloped diagonals.
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == board[r + 1][c + 1] and board[r][c] == board[r + 2][c + 2] and board[r][c] == mark:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == board[r - 1][c + 1] and board[r][c] == board[r - 2][c + 2] and board[r][c] == mark:
                return True

def winning_move2(mark):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == board[r][c + 1] and board[r][c] == mark:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == board[r + 1][c] and board[r][c] == mark:
                return True

    # Check positively sloped diagonals.
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == board[r + 1][c + 1] and board[r][c] == mark:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == board[r - 1][c + 1] and board[r][c] == mark:
                return True

def winning_move_all():
        # Check horizontal locations for win
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if board[r][c] == board[r][c + 1] and board[r][c] == board[r][c + 2] and board[r][c] == board[r][c + 3] and board[r][c] != ' ':
                    return True

        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == board[r + 1][c] and board[r][c] == board[r + 2][c] and board[r][c] == board[r + 3][c] and board[r][c] != ' ':
                    return True

        # Check positively sloped diagonals.
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == board[r + 1][c + 1] and board[r][c] == board[r + 2][c + 2]and board[r][c] == board[r + 3][c + 3] and board[r][c] != ' ':
                    return True

        # Check negatively sloped diaganols
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == board[r - 1][c + 1] and board[r][c] == board[r - 2][c + 2] and board[r][c] == board[r - 3][c + 3] and board[r][c] != ' ':
                    return True

def insertLetter(letter,position):

    if space_is_free(position):
        for itt in range(5,-1,-1):
            if board[itt][position] == ' ':
                board[itt][position] = letter
                print(board)
                return


            if draw():
                print("Draw!")
                exit()

            if wincheck():
                if letter == 'O':
                    print("Player1 wins!")
                    exit()
                else:
                    print("Player2 wins!")
                    exit()

    else:
        print("Slot is not available.")
        position = int(input("Enter new position: "))
        insertLetter(letter, position)
        return

computer = 'X'
player = 'O'

def player_move():
    position = int(input("Please enter a position for 'O': "))
    insertLetter(player,position)
    return


def computer_move():
    best_score = -1000    #maximizing player
    best_move = 0

    for row in range(5, -1, -1):
        for col in range(7):
            if board[row][col] == ' ':
                board[row][col] = computer
                print('COMPUTER MOVE',row,col)
                score = minimax(board,20, False)
                #print("Computer", score)
                print('Computer turn.')
                board[row][col] = ' '
                print(board[row][col])
                if score > best_score:
                    best_score = score
                    best_move = col
    insertLetter(computer, best_move)
    return


def evaluate():
    score = 0
    if draw():
        score = 0
        return

    elif wincheckmark(computer):
        score += 100
        return score

    elif wincheckmark(player):
        score += -100
        return score

    elif wincheck3(computer):
        score += 50
        return score

    elif wincheck3(player):
        score += -50
        return score

    elif wincheck2(computer):
        score += 30
        return score

    elif wincheck2(player):
        score += -30
        return score



def minimax(board,depth, isMaximizing):
    if depth == 0:
        evaluate()

    if isMaximizing:
        best_score = -100000

        for row in range(5, -1, -1):
            for col in range(7):
                if board[row][col] == ' ':
                    board[row][col] = computer
                    score = minimax(board,depth-1, False)
                    #print("COMPUTER:", score)
                    board[row][col] = ' '
                    if score > best_score:
                        best_score = score
                        print("COMPUTER  BEST SCORE: ", best_score)
                    # alpha = max(alpha,score)
                    #
                    # if beta <= alpha:
                    #     break
        print("COMPUTER BEST SCORE", best_score)
        return best_score

    else:
        best_score = 100000
        for row in range(5, -1, -1):
            for col in range(7):
                if board[row][col] == ' ':
                    board[row][col] = player
                    #print('P COL ', col)
                    score = minimax(board, depth-1, True)
                    #print('PLAYER',score)
                    board[row][col] = ' '
                    if score < best_score:
                        best_score = score
                        print("BEST SCORE PLAYER", best_score)
                    # beta = min(beta,score)
                    # if beta <= alpha:
                    #     break
        #print('PLAYER BEST SCORE',best_score)
        return best_score


print(board)
while not wincheck():
    computer_move()
    player_move()

# print(board)
# print(winning_move('X'))
# print(winning_move3('X'))
# print(winning_move_all())
# print(winning_move2('X'))









