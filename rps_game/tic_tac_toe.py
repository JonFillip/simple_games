board_moves = {'top_L': ' ', 'top_M': ' ', 'top_R': ' ',
                'mid_L': ' ', 'mid_M': ' ', 'mid_R': ' ',
                'bottom_L': ' ', 'bottom_M': ' ', 'bottom_R': ' '}

def tic_tac_toe(board):
    """"Prints the demarcations for the board"""
    print(f"{board['top_L']}|{board['top_M']}|{board['top_R']}")
    print('-+-+-')
    print(f"{board['mid_L']}|{board['mid_M']}|{board['mid_R']}")
    print('-+-+-')
    print(f"{board['bottom_L']}|{board['bottom_M']}|{board['bottom_R']}")

move = 'X'
for i in range(9):
    tic_tac_toe(board_moves)
    player_move = print(input(f"Your turn - {move}. Move on which space?"))
    board_moves[player_move] = move
    if move == 'X':
        move = 'O'
    else:
        move = 'X'

tic_tac_toe(board_moves)