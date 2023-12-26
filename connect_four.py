"""This program plays connect four on the terminal."""

__author__ = "Ayaan Adrito"

MAX_COLUMNS = 35
MAX_ROWS = 30

PLAYER_ONE = "🟡"
PLAYER_TWO = "🔴"
BLANK = "⚪"

game_over = False

def change_board(rows: int, columns: int):
    """Change the board's dimensions to rows x columns."""

    result = []

    for i in range(rows):
        row = []

        for j in range(columns):
            row.append(BLANK)
        
        result.append(row)

    return result

def print_menu():
    """Print the game menu."""

    print("\nPlease choose from one of the following options:")
    print("1. Play game")
    print("2. Change dimensions")
    print("3. How to play & Rules")
    print("4. Exit")

def validate_input(min: int, max: int, msg: str) -> int:
    """Return a valid integer between min and max."""

    while True:
        try:
            number = int(input(msg))

            if min <= number <= max:
                return number
            else:
                print(f"Number {number} is out of range. Input must be between {min} and {max}")
        except:
            print("Invalid input. You must enter an integer.")

def print_board(board: list):
    """Print board in a formatted manner."""

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

def print_rules():
    """Print the rules of connect four."""

    print("\nConnect four rules:")
    print("Each player places a different colored coin on the board.")
    print("The coins stack and cannot be placed if a column is full.")
    print("The first player to stack four coins wins.")
    print("The four coins may be stacked horizontaly, vertically, or diagonally.")
    print("If the board is full and there are not four coins stacked, it is a tie.")
    input("> ")

def is_full(board: list) -> bool:
    """Returns whether if board is full"""

    for row in board:
        for column in row:
            if column == BLANK:
                return False

    return True

def player_turn(player: str, current_columns: int, board: list):
    """Do the player's turn on board."""

    print(f"Player {player}, select a column (1 - {current_columns})")
    choice = validate_input(1, current_columns, "> ")
    if place_coin(choice, player, board) == False:
        print(f"\nColumn {choice} is full. Select another column.")

    print_board(board)
    print()

def place_coin(column: int, player: str, board: list):
    """Place coin in desired column of board. If column is full, return False."""
    column -= 1

    length = len(board)
    for i in range(length - 1, -1, -1):
        if board[i][column] == BLANK:
            board[i][column] = player
            return True
        
    return False


def main():

    print("="*12)
    print("CONNECT FOUR")
    print("="*12)

    board = change_board(6, 7)

    current_rows = 6
    current_columns = 7

    running = True

    for i in range(len(board) - 1, -1, -1):
        print(i)

    while running == True:
        print_menu()
        num = validate_input(1, 4, "> ")

        # Game loop
        if num == 1:
            game_over = False
            winner = "⚪"

            while game_over == False:
                # Player one turn
                player_turn(PLAYER_ONE, current_columns, board)
                game_over = is_full(board)

                if is_full(board) == False:
                    # Player two turn
                    player_turn(PLAYER_TWO, current_columns, board)
        
                game_over = is_full(board)
        
        # Change board dimensions
        elif num == 2:
            print(f"\nPlease enter the desired rows (less than {MAX_ROWS + 1}): ")
            rows = validate_input(1, MAX_ROWS, "> ")

            print(f"Please enter the desired columns (less than {MAX_COLUMNS + 1}): ")
            columns = validate_input(1, MAX_COLUMNS, "> ")

            board = change_board(rows, columns)
            current_rows = rows
            current_columns = columns
        # Print the rules
        elif num == 3:
            print_rules()
        # Quit program
        elif num == 4:
            running = False
    

if __name__ == "__main__":
    main()