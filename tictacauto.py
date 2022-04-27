board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' ',}

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


def spaceIsFree(position):
    if (board[position] == ' '):
        return True
    else:
        return False

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def wincheck():
    # Horizontal Check.
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    # Vertical Check.
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    # Diagonal Check.
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[3] == board[5] and board[3] == board[7] and board[3] != ' '):
        return True
    else:
        return False

def wincheckmark(mark):
    # Horizontal Check.
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    # Vertical Check.
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    # Diagonal Check.
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[3] == board[5] and board[3] == board[7] and board[3] == mark):
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Draw!")
            exit()

        if wincheck():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()

    else:
        print("Slot is not available.")
        position = int(input("Enter new position: "))
        insertLetter(letter, position)
        return

player = 'O'
bot = 'X'
def playerMove():
    position = int(input("Enter a position for 'O': "))
    insertLetter(player, position)
    return


def computerMove():
    bestScore = -1000
    bestMove = 0

    for key in board.keys():
        if(board[key] == ' '):
            board[key] = bot
            score = minimax(board,0,False)
            print('COMPUTER SCORE: ', score)
            board[key] = ' '
            if(score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot,bestMove)
    return

def minimax(board, depth, isMaximizing):

    if wincheckmark(bot):
        return 100

    elif wincheckmark(player):
        return -100

    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -1000

        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, 0, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score

        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, 0, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore





while not wincheck():
    computerMove()
    playerMove()


