import random
from colorama import init, Fore, Style
init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()

def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).upper()
    if symbol == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def player_move(board, symbol):
    Purpose: Prompt the player for a move and update the board.
    Loop until a valid move is entered (number 1-9 and an available spot).
    Update the board at the chosen index with the player's symbol.
    pass

# Function: ai_move(board, ai_symbol, player_symbol)
#   - Purpose: Decide and execute the AI's move.
#   - For each free spot, simulate placing ai_symbol:
#         * If that move wins the game (using check_win), place the symbol and return.
#   - For each free spot, simulate placing player_symbol:
#         * If that move would let the player win, block it by placing ai_symbol and return.
#   - Otherwise, choose a random available move and place ai_symbol.

# Function: check_win(board, symbol)
#   - Purpose: Check if the given symbol has met any winning condition.
#   - Define winning conditions (horizontal, vertical, diagonal).
#   - Return True if any condition is met; otherwise, return False.

# Function: check_full(board)
#   - Purpose: Check if the board is completely filled.
#   - Return True if no cell contains a digit (i.e., all spots are taken).

# Function: tic_tac_toe()
#   - Purpose: Main game loop for Tic-Tac-Toe.
#   - Welcome the player and prompt for the player's name (display prompt in green).
#   - Loop to play games until the player chooses not to continue:
#         * Initialize the board with cell numbers.
#         * Get player's and AI's symbols via player_choice().
#         * Set the starting turn to 'Player'.
#         * While the game is on:
#               - Display the board.
#               - If it's the player's turn:
#                     > Call player_move() to get and execute the player's move.
#                     > Check if the player wins using check_win(); if so, display a win message and end the game.
#                     > Else, if the board is full, display a tie message and break.
#                     > Otherwise, set turn to 'AI'.
#               - If it's the AI's turn:
#                     > Call ai_move() to decide and execute the AI's move.
#                     > Check if the AI wins; if so, display a win message and end the game.
#                     > Else, if the board is full, display a tie message and break.
#                     > Otherwise, set turn to 'Player'.
#         * After the game ends, prompt the player if they want to play again.
#         * If the player does not type 'yes', exit the loop and thank the player.
#
# If the script is executed as the main module, call tic_tac_toe() to start the game.





