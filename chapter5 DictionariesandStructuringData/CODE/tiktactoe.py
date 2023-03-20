def boardPrinter(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print('-+-+-')


def winnerCheck(board):
    # checking Diagonal
    if (board['top-L'] == board['mid-M'] == board['low-R'] != ' ') or (board['top-R'] == board['mid-M'] == board['low-L'] != ' '):
        print(board['mid-M'] + ' wins the game')
        return True
    # checking rows
    for row in ['top-', 'mid-', 'low-']:
        if board[row + 'L'] == board[row + 'M'] == board[row + 'R'] != ' ':
            print(board[row + 'L'] + ' wins the game')
            return True
    # checking columns
    for col in ['-L', '-M', '-R']:
        if board['top' + col] == board['mid' + col] == board['low' + col] != ' ':
            print(board['top' + col] + ' wins the game')
            return True
    return False


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

turn = 'X'

for i in range(9):
    boardPrinter(theBoard)
    print(f"\nIt's {turn} turn")
    move = input("Enter your move: ")
    theBoard[move] = turn

    if winnerCheck(theBoard):
        break

    # Switch turn
    turn = 'O' if turn == 'X' else 'X'
