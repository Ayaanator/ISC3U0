"""This program plays connect four on the terminal.

The goal of the game is to connect four of the same coins in a row.
This can be done vertically, horizontally, and diagonally.
Coins are placed on top of previously placed coins.
If a column is full, you cannot place a coin there.
If all columns are full and there isn't four in a row, it is a tie.
"""

__author__ = "Ayaan Adrito"

# Maximum amount of connects the win condition can be set to
MIN_CONNECTS = 3
MAX_CONNECTS = 6

# Maximum amount of columns the board can be changed to
MAX_COLUMNS = 20
MAX_ROWS = 20

# Original constants for resetting game settings
ORIG_CONNECTS_TO_WIN = 4
ORIG_ROWS = 6
ORIG_COLUMNS = 7

# Graphical constants
PLAYER_ONE = "🟡"
PLAYER_TWO = "🔴"
BLANK = "🔘"

# Other blank emojis to use if display isn't compatible with other systems
# ◯
# ⚪
# 〄
# ⭕
# 🔘

game_over = False

def make_board(rows: int, columns: int):
    """Make a new board that is rows x columns.
    
    >>> make_board(6, 7)

    [["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
     ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
     ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
     ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
     ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
     ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"]]

     >>> make_board(4, 4)

    [["🔘", "🔘", "🔘", "🔘"],
     ["🔘", "🔘", "🔘", "🔘"],
     ["🔘", "🔘", "🔘", "🔘"],
     ["🔘", "🔘", "🔘", "🔘"]]
    """

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
    print("2. Change settings")
    print("3. How to play & Rules")
    print("4. Exit")


def validate_input(min: int, max: int, msg: str) -> int:
    """Return a valid integer between min and max.
    
    >>> validate_input(1, 10, '> ')
    > 352325
    Number 352325 is out of range. Input must be between 1 and 10
    > -234
    Number -234 is out of range. Input must be between 1 and 10
    > 0
    Number 0 is out of range. Input must be between 1 and 10
    > 3
    3
    """

    while True:
        try:
            number = int(input(msg))

            if min <= number <= max:
                return number
            else:
                print(f"Number {number} is out of range. Input must be between {min} and {max}.")
        except:
            print("Invalid input. You must enter an integer.")


def print_board(board: list):
    """Print board in a formatted manner."""

    first_row = True

    for i in range(len(board)):
        if first_row == True:
            print()

        first_column = True

        for j in range(len(board[i])):
            if first_column == True:
                first_column = False
                print("|", end="")

            print(f"{board[i][j]} |", end="")
    
    # Print the column numbers under the board
    first_row = True

    print()
    for k in range(len(board[0])):
        if first_row == True:
            print(f"  {k + 1}", end="")
            first_row = False
        else:
            if k < 10:
                print(f"   {k + 1}", end="")
            else:
                print(f"  {k + 1}", end="")


def print_rules():
    """Print the rules of connect four."""

    print("\nConnect four rules:")
    print("Each player places a different colored coin on the board.")
    print("The coins stack and cannot be placed if a column is full.")
    print("The first player to stack four coins wins.")
    print("The four coins may be stacked horizontaly, vertically, or diagonally.")
    print("If the board is full and there are not four coins stacked, it is a tie.")
    input("Press enter to continue >>> ")


def is_full(board: list) -> bool:
    """Returns whether if board is full."""

    for row in board:
        for column in row:
            if column == BLANK:
                return False

    return True


def player_turn(player: str, current_columns: int, board: list):
    """Do the player's turn on board."""

    while  True:
        print(f"Player {player}, select a column (1 - {current_columns})")
        choice = validate_input(1, current_columns, "> ")
        if place_coin(choice, player, board) == False:
            print(f"\nColumn {choice} is full. Select another column.")
            print_board(board)
            print()
        else:
            print_board(board)
            print()
            break


def place_coin(column: int, player: str, board: list):
    """Place coin in desired column of board. If column is full, return False.
    
    >>> place_coin(4, 🔴, 
                   [["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🔘", "🟡", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🟡", "🔴", "🔘", "🔘", "🔘"]])

                   [["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🔘", "🔴", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🔘", "🟡", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🟡", "🔴", "🔘", "🔘", "🔘"]]

                    True

    >>> place_coin(53, 🟡, 
                   [["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🔘", "🟡", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🟡", "🔴", "🔘", "🔘", "🔘"]])

                   [["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🔘", "🔴", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🔘", "🟡", "🔘", "🔘", "🔘"],
                    ["🔘", "🔘", "🟡", "🔴", "🔘", "🔘", "🔘"]]

                    False
                    Number 53 is out of range. Input must be between 1 and 7.
    """

    # Input is between 1 and length of board[0], 
    # -1 is needed to set column to the correct index
    column -= 1

    length = len(board)
    for i in range(length - 1, -1, -1):
        if board[i][column] == BLANK:
            board[i][column] = player
            return True
        
    return False


def check_horizontal(board: list, player: str, connects_to_win: int) -> str:
    """Check for four in a row horizontally."""

    counter = 0
    for row in board:
        counter = 0
        for item in row:
            if item == player:
                counter += 1
                if counter == connects_to_win:
                    return player
            else:
                counter = 0

    return "⚪"


def check_vertical(board: list, player: str, connects_to_win: int) -> str:
    """Check for four in a row vertically"""

    counter = 0
    for i in range(len(board[0])):
        counter = 0
        for j in range(len(board)):
            if board[j][i] == player:
                counter += 1
                if counter == connects_to_win:
                    return player
            else:
                counter = 0

    return "⚪"


def check_left_diagonal(board: list, player: str, connects_to_win: int) -> str:
    """Check for four in a row diagonally left to right"""

    # Search diagonally left to right
    while len(board[0]) > 3:
        counter = 0
        main_counter = 0

        # Move down the leftmost column in a loop
        while main_counter < len(board):
            y_counter = main_counter
            x_counter = 0

            # Move left-right diagonally
            while x_counter < main_counter + 1 and y_counter > -1 and x_counter < len(board[0]):
                test = board[y_counter][x_counter]
                if test == player:
                    counter += 1
                    if counter == connects_to_win:
                        # Four in a row
                        return player
                else:
                    counter = 0
                
                # Move up and right
                y_counter -= 1
                x_counter += 1

            main_counter += 1
            counter = 0

        # Split board from left to reiterate search loop over next column
        board = split_board(board, True)
        counter = 0

    return "⚪"


def check_right_diagonal(board: list, player: str, connects_to_win) -> str:
    """Check for four in a row diagonally right to left"""

    # Search diagonally right to left
    while len(board[0]) > 3:
        counter = 0
        main_counter = 0

        # Move down the rightmost column in a loop
        while main_counter < len(board):
            y_counter = main_counter
            x_counter = len(board[0]) - 1

            # Move right-left diagonally
            while x_counter > -1 and y_counter > -1:
                test = board[y_counter][x_counter]
                if test == player:
                    counter += 1
                    if counter == connects_to_win:
                        # Four in a row
                        return player
                else:
                    counter = 0
                
                # Move up and left
                y_counter -= 1
                x_counter -= 1

            main_counter += 1
            counter = 0
            
        # Split board from right to reiterate search loop over next column
        board = split_board(board, False)
        counter = 0

    return "⚪" 


def find_winner(board: list, player: str, connects_to_win: int) -> str:
    """Determine if player has won by getting connects_to_win connects in board. If not, return ⚪.
    
    >>> find_winner([["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                     ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                     ["🔘", "🔘", "🔘", "🔘", "🔘", "🟡", "🔘"],
                     ["🔘", "🔘", "🔘", "🔘", "🟡", "🔴", "🔘"],
                     ["🔘", "🔘", "🟡", "🟡", "🔴", "🟡", "🔘"],
                     ["🔘", "🔘", "🟡", "🔴", "🔴", "🔴", "🔘"]], 🟡)
    "🟡"

    >>> find_winner([["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                     ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                     ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                     ["🔘", "🔘", "🔘", "🔘", "🟡", "🔴", "🔘"],
                     ["🔘", "🔘", "🟡", "🟡", "🔴", "🟡", "🔘"],
                     ["🟡", "🔘", "🟡", "🔴", "🔴", "🔴", "🔘"]], 🟡)
    "🔘"
    """

    # Check all directions (up, down, left, right, and all four diagonals)
    if check_horizontal(board, player, connects_to_win) == player or \
            check_vertical(board, player, connects_to_win) == player or \
            check_left_diagonal(board, player, connects_to_win) == player or \
            check_right_diagonal(board, player, connects_to_win) == player:
        return player
    
    return "⚪"


def split_board(board: list, left: bool) -> list:
    """Split one column from the left or right side of board and return it.
    
    >>> split_board([["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                     ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                     ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                     ["🔘", "🔘", "🔘", "🔘", "🟡", "🔴", "🔘"],
                     ["🔘", "🔘", "🟡", "🟡", "🔴", "🟡", "🔘"],
                     ["🟡", "🔘", "🟡", "🔴", "🔴", "🔴", "🔘"]], True)

    [["🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
     ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
     ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
     ["🔘", "🔘", "🔘", "🟡", "🔴", "🔘"],
     ["🔘", "🟡", "🟡", "🔴", "🟡", "🔘"],
     ["🔘", "🟡", "🔴", "🔴", "🔴", "🔘"]]

    >>> split_board([["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                     ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                     ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
                     ["🔘", "🔘", "🔘", "🔘", "🟡", "🔴", "🔘"],
                     ["🔘", "🔘", "🟡", "🟡", "🔴", "🟡", "🔘"],
                     ["🟡", "🔘", "🟡", "🔴", "🔴", "🔴", "🔘"]], False)

    [["🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
     ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
     ["🔘", "🔘", "🔘", "🔘", "🔘", "🔘"],
     ["🔘", "🔘", "🔘", "🔘", "🟡", "🔴"],
     ["🔘", "🔘", "🟡", "🟡", "🔴", "🟡"],
     ["🟡", "🔘", "🟡", "🔴", "🔴", "🔴"]]
    """
    
    result = []
    
    # Strip left column
    if left == True:
        for row in board:
            new_row = []

            for i in range(1, len(board[0]), 1):
                new_row += [row[i]]

            result += [new_row]
    else:
        # Strip right column
        for row in board:
            new_row = []

            for i in range(0, len(board[0]) - 1, 1):
                new_row += [row[i]]

            result += [new_row]

    return result


def main():
    print("="*150)
    print("""
  /$$$$$$   /$$$$$$  /$$   /$$ /$$   /$$ /$$$$$$$$  /$$$$$$  /$$$$$$$$       /$$$$$$$$ /$$$$$$  /$$   /$$ /$$$$$$$ 
 /$$__  $$ /$$__  $$| $$$ | $$| $$$ | $$| $$_____/ /$$__  $$|__  $$__/      | $$_____//$$__  $$| $$  | $$| $$__  $$
| $$  \__/| $$  \ $$| $$$$| $$| $$$$| $$| $$      | $$  \__/   | $$         | $$     | $$  \ $$| $$  | $$| $$  \ $$
| $$      | $$  | $$| $$ $$ $$| $$ $$ $$| $$$$$   | $$         | $$         | $$$$$  | $$  | $$| $$  | $$| $$$$$$$/
| $$      | $$  | $$| $$  $$$$| $$  $$$$| $$__/   | $$         | $$         | $$__/  | $$  | $$| $$  | $$| $$__  $$
| $$    $$| $$  | $$| $$\  $$$| $$\  $$$| $$      | $$    $$   | $$         | $$     | $$  | $$| $$  | $$| $$  \ $$
|  $$$$$$/|  $$$$$$/| $$ \  $$| $$ \  $$| $$$$$$$$|  $$$$$$/   | $$         | $$     |  $$$$$$/|  $$$$$$/| $$  | $$
 \______/  \______/ |__/  \__/|__/  \__/|________/ \______/    |__/         |__/      \______/  \______/ |__/  |__/
""")
    print("="*150)

    # Initialize 6 x 7 board and default win condition
    current_rows = 6
    current_columns = 7
    connects_to_win = 4
    board = make_board(current_rows, current_columns)

    running = True

    # Main loop
    while running == True:
        print_menu()
        num = validate_input(1, 4, "> ")

        # Game loop
        if num == 1:
            board = make_board(current_rows, current_columns)
            print_board(board)
            print("\n")

            game_over = False
            winner = "⚪"
            
            while game_over == False:
                # Player one turn
                player_turn(PLAYER_ONE, current_columns, board)
                winner = find_winner(board, PLAYER_ONE, connects_to_win)
                game_over = True if winner != "⚪" else is_full(board)

                # Check if game is over before letting player 🔴 go
                if game_over == False:
                    # Player two turn
                    player_turn(PLAYER_TWO, current_columns, board)
                    winner = find_winner(board, PLAYER_TWO, connects_to_win)
                    game_over = True if winner != "⚪" else is_full(board)
            # Tie
            if winner == "⚪":
                print("\nGame over! It's a tie!")
            else:
                # Win
                print(f"\nGame over! Player {winner}  won!")

            # Reset board for next round
            board = make_board(current_columns, current_columns)
        
        # Change settings
        elif num == 2:
            print("\n1. Change amount of connects for win condition")
            print("2. Change board dimensions")
            print("3. Reset to default")
            num = validate_input(1, 3, "> ")

            # Change win condition
            if num == 1:
                print(f"\nPlease enter the desired win condtion {MIN_CONNECTS} and {MAX_CONNECTS}: ")
                desired_connects = validate_input(MIN_CONNECTS, MAX_CONNECTS, "> ")
                connects_to_win  = desired_connects

                # Change dimensions if desired_connects is too high
                if connects_to_win > current_rows and desired_connects > current_columns:
                    print("Your board is too small. Changing dimensions...")
                    current_rows = connects_to_win
                    current_columns = connects_to_win
                elif connects_to_win > current_rows:
                    print("Your board is too small. Changing dimensions...")
                    current_rows = connects_to_win
                elif connects_to_win > current_columns:
                    print("Your board is too small. Changing dimensions...")
                    current_columns = connects_to_win

                board = make_board(current_rows, current_columns)
            # Change board dimensions
            elif num == 2:
                # Make sure columns and rows aren't less than connects_to_win 
                # to make sure winning is possible
                print(f"\nPlease enter the desired rows between {connects_to_win} and {MAX_ROWS}: ")
                rows = validate_input(connects_to_win, MAX_ROWS, "> ")

                print(f"Please enter the desired columns between {connects_to_win} and {MAX_COLUMNS}: ")
                columns = validate_input(connects_to_win, MAX_COLUMNS, "> ")

                current_rows = rows
                current_columns = columns
                board = make_board(current_rows, current_columns)
            # Set settings to default
            else:
                connects_to_win = ORIG_CONNECTS_TO_WIN
                current_rows = ORIG_ROWS
                current_columns = ORIG_COLUMNS
                board = make_board(current_rows, current_columns)
        # Print the rules
        elif num == 3:
            print_rules()
        # Quit program
        elif num == 4:
            running = False
            print("\nThanks for playing my Connect Four game, Mr. Cho!\n")

if __name__ == "__main__":
    main()