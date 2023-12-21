"""This program plays connect four on the terminal."""

__author__ = "Ayaan Adrito"

MAX_COLUMNS = 35
MAX_ROWS = 30

board = []

def intialize_board():
    """Initialize the default board of 7x6"""

    for i in range(6):
        row = []

        for j in range(7):
            row.append("O")
        
        board.append(row)

def print_board():
    """Print board in formatted manner."""

    first_row = True

    for i in range(len(board)):
        if first_row == True:
            print()
            pass

        # print(len(board[i])*"-"*2)
        first_column = True

        for j in range(len(board[i])):
            if first_column == True:
                first_column = False
                print("|", end="")

            print(f"{board[i][j]}|", end="")

def main():
    intialize_board()
    print_board()

if __name__ == "__main__":
    main()