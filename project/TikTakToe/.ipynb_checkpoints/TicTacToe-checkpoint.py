from operator import truediv


row = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

game_running = True
name = 'TicTecToe'
winner = None

player1 = 'X'
player2 = 'O'
move_number = 1

grid = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}

move_player_1 = True

win_seq = [[(0,0),(0,1),(0,2)],\
    [(1,0),(1,1),(1,2)],\
    [(2,0),(2,1),(2,2)],\
    [(0,0),(1,0),(2,0)],\
    [(0,1),(1,1),(2,1)],\
    [(0,2),(1,2),(2,2)],\
    [(0,0),(1,1),(2,2)],\
    [(0,2),(1,1),(2,0)]]

def help_board():
    print(['1','2','3'])
    print(['4','5','6'])
    print(['7','8','9'])

def print_board():
    print(row[0])
    print(row[1])
    print(row[2])

def get_user_input(msg, valid_answer_list, type='string'):
    answer = input(msg)
    if type == 'int':
        while not answer.isdigit:
            print('Not a valid input, valid inputs are:')
            print(valid_answer_list)
            answer = input(msg)
        answer = int(answer)
    while not answer in valid_answer_list:
        print('Not a valid input, valid inputs are:')
        print(valid_answer_list)
        answer = input(msg)
    return answer

def welcome():
    print("Welcome to {}!".format(name))
    answer = get_user_input('Do you want to play {}? (y, n): '.format(name), ['y','n','Y','N'])
    return answer == 'y' or answer == 'Y'

def goodbye():
    print("Thanks for playing {}".format(name))

def help():
    print('Game rules are simple. Game has following board (3x3=9)')
    print_board()
    print("It is numbered 1-9 as follow:")
    help_board()
    print('On your turn, select the number of the position you want to mark.')
    print('Player 1 = {}'.format(player1))
    print('Player 2 = {}'.format(player2))

def player_to_move():
    if move_player_1:
        return 'Player 1'
    else:
        return 'Player 2'

def get_current_player_sign():
    if move_player_1:
        return player1
    else:
        return player2

def check_game_status():
    if move_number >= 10:
        print('Game Draw')
        return False
    player_sign = get_current_player_sign()
    for seq in win_seq:

        if row[seq[0][0]][seq[0][1]] == player_sign and row[seq[1][0]][seq[1][1]] == player_sign and row[seq[2][0]][seq[2][1]] == player_sign:
            print('{} is winner!'.format(player_to_move()))
            return False

    return True

def draw():
    print('Game draw')
    exit

def move():
    global move_number

    valid_input = [1,2,3,4,5,6,7,8,9]
    answer = get_user_input('{}: select your position to mark (1-9)'.format(player_to_move()), valid_input, 'int')
    move_row,move_col = grid[answer]

    if move_player_1:
        row[move_row][move_col] = player1
    else:
        row[move_row][move_col] = player2

    move_number += 1

if not welcome():
    goodbye()
    sys.exit(0)
help()

while game_running:
    move()
    print_board()
    game_running = check_game_status()
    move_player_1 = not move_player_1