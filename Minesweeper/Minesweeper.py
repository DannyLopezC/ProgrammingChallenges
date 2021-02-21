height = 1
length = 1
square = '.'
mine = "*"
#fields made counter
counter = 0
SolvedBoards = []

#constructs the board
def constructBoard(h):
    for _ in range(h):
        x = list(map(str, input().split()))
        board.append(x)


def constructBoardSolved(h, l):
    for i in range(h):
        boardSolved.append([])
        for _ in range(l):
            boardSolved[i].append(0)


def sumAround(i, j):
    if(i <= 0):
        if(j <= 0):
            if boardSolved[i + 1][j + 1] != "*": boardSolved[i + 1][j + 1] += 1
            if boardSolved[i + 1][j] != "*": boardSolved[i + 1][j] += 1
            if boardSolved[i][j + 1] != "*": boardSolved[i][j + 1] += 1
        elif(j >= len(boardSolved[i]) - 1):
            if boardSolved[i + 1][j - 1] != "*": boardSolved[i + 1][j - 1] += 1
            if boardSolved[i + 1][j] != "*": boardSolved[i + 1][j] += 1
            if boardSolved[i][j - 1] != "*": boardSolved[i][j - 1] += 1
        else:
            if boardSolved[i + 1][j - 1] != "*": boardSolved[i + 1][j - 1] += 1
            if boardSolved[i + 1][j + 1] != "*": boardSolved[i + 1][j + 1] += 1
            if boardSolved[i][j - 1] != "*": boardSolved[i][j - 1] += 1
            if boardSolved[i][j + 1] != "*": boardSolved[i][j + 1] += 1
    elif(i >= len(boardSolved) - 1):
        if(j <= 0):
            if boardSolved[i - 1][j + 1] != "*": boardSolved[i - 1][j + 1] += 1
            if boardSolved[i - 1][j] != "*": boardSolved[i - 1][j] += 1
            if boardSolved[i][j + 1] != "*": boardSolved[i][j + 1] += 1
        elif(j >= len(boardSolved[i]) - 1):
            if boardSolved[i - 1][j - 1] != "*": boardSolved[i - 1][j - 1] += 1
            if boardSolved[i - 1][j] != "*": boardSolved[i - 1][j] += 1
            if boardSolved[i][j - 1] != "*": boardSolved[i][j - 1] += 1
        else:
            if boardSolved[i - 1][j - 1] != "*": boardSolved[i - 1][j - 1] += 1
            if boardSolved[i - 1][j + 1] != "*": boardSolved[i - 1][j + 1] += 1
            if boardSolved[i][j - 1] != "*": boardSolved[i][j - 1] += 1
            if boardSolved[i][j + 1] != "*": boardSolved[i][j + 1] += 1
    else:
        if(j <= 0):
            if boardSolved[i + 1][j + 1] != "*": boardSolved[i + 1][j + 1] += 1
            if boardSolved[i + 1][j] != "*": boardSolved[i + 1][j] += 1
            if boardSolved[i - 1][j + 1] != "*": boardSolved[i - 1][j + 1] += 1
            if boardSolved[i - 1][j] != "*": boardSolved[i - 1][j] += 1
            if boardSolved[i][j + 1] != "*": boardSolved[i][j + 1] += 1
        elif(j >= len(boardSolved[i]) - 1):
            if boardSolved[i + 1][j - 1] != "*": boardSolved[i + 1][j - 1] += 1
            if boardSolved[i + 1][j] != "*": boardSolved[i + 1][j] += 1
            if boardSolved[i - 1][j - 1] != "*": boardSolved[i - 1][j - 1] += 1
            if boardSolved[i - 1][j] != "*": boardSolved[i - 1][j] += 1
            if boardSolved[i][j - 1] != "*": boardSolved[i][j - 1] += 1
        else:
            if boardSolved[i + 1][j + 1] != "*": boardSolved[i + 1][j + 1] += 1
            if boardSolved[i + 1][j - 1] != "*": boardSolved[i + 1][j - 1] += 1
            if boardSolved[i][j + 1] != "*": boardSolved[i][j + 1] += 1
            if boardSolved[i][j - 1] != "*": boardSolved[i][j - 1] += 1
            if boardSolved[i + 1][j] != "*": boardSolved[i + 1][j] += 1
            if boardSolved[i - 1][j] != "*": boardSolved[i - 1][j] += 1
            if boardSolved[i - 1][j + 1] != "*": boardSolved[i - 1][j + 1] += 1
            if boardSolved[i - 1][j - 1] != "*": boardSolved[i - 1][j - 1] += 1


def solveMinesweeper():
    for i in range(height):
        for j in range(length):
            if board[i][j] == mine:
                sumAround(i, j)
                boardSolved[i][j] = "*"


def printMinesweeperSolved(k):
    print(" ")
    print(f'Field # {counter}')
    for i in range(len(SolvedBoards[k])):
        if i > 0:
            print(" ")
        for j in range(len(SolvedBoards[k][i])):
            print(SolvedBoards[k][i][j], end='')


#it finish when height and lenght are 0
while height != 0 and length != 0:
    counter += 1
    board = []
    boardSolved = []
    height, length = map(int, input().split())

    constructBoard(height)
    constructBoardSolved(height, length)
    solveMinesweeper()
    SolvedBoards.append(boardSolved)


for i in range(len(SolvedBoards) - 1):
    printMinesweeperSolved(i)

print(" ")
