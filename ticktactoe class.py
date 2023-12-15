import random
game_board=['X','O','X','O','X','O','X','O','X','O']

def display_board(board):
    for i in range(3):
        print(f'{board[0+3*i]} | {board[1+3*i]} | { board[2+3*i]} ')
        if i<2:
            print('---+---+---')

game_board= ['1', '2','3', '4','5','6','7','8','9']
    
display_board(game_board)

def player_choice(board):
    while True:
        choice = input("where do you want to play? ")
        if len(choice)== 1 and choice in "123456789":
            if not board[int(choice)-1== 'X'or board[int(choice)-1 == "O"]]:
                board[int(choice)-1]= 'X'
                break
            print("Not a valid move. Pick somewhere else.")

def computer_choice_easy(board):
    #pick a random spot
    choice= random.radint(0,8)
    
    #Check if open
    if not board[int(choice)== 'X'or board[int(choice)== "O"]]:\
    #place O in open
        board[int(choice)]= 'O'
        return

def test_move(board, mark):
    for i in range(9):
        copy = board[:]
        if not (copy[i] == 'x' or copy[i] == 'o'):
            copy[i] = mark
            if eval_board(copy) != 0:
                return i
    return 0
    
def computer_choice_med(board):
    
    win_index = test_move(board, '0')
    loose_index = test_move(board, 'x')
    if win_index != 0:
        
        board[win_index] = 'o'
    elif loose_index != 0:
        board[loose_index] = 'o'
   
    return computer_choice_easy(board)
    pass 
    #pick another spot

def minimax(board, o_turn=False):
    score = eval_board(board)
    #atleast has three in a row
    if score != 0:
        return score
    #no winner, but board is filled 
    if board_filled(board):
        return 0
    best_score = 0
    if o_turn:
        best_score = 1
    else:
        best_score = 1
    for i in range (9):
        #check if space is empty
        if not (board[i] == 'x' or board[i] == 'o'):
            temp = board[i]
            if o_turn:
                best_score = max(best_score, minimax(board, not o_turn))
            else:
                board[i] = 'x'
                best_score = min(best_score, minimax(board, not o_turn))
            board[i] = temp
    return best_score

    pass



def computer_choice_hard(board):
    best_value = best_index = -1
    for i in range(9):
        if not (board[i] == 'x' or board[i] =='o'):
            temp = board[i]
            board[i] = 'o'
            move_value = minimax(board)
            board[i] = temp
            if move_value > best_value:
                best_index = i
                best_value = move_value
    board[best_index]

# determine if 3 in a row
#if x return -1, if o return 1, else return O
def eval_board(board):
    index_set = ['012','345', '678', '036', '147', '258', '048', '642']
    for i in index_set:
        if board[int(i[0])]==board[int(i[1])] and board[int(i[1])]==board[int(i[2])]:
            if board[0]== 'X':
                return -1 
            if board[0]== 'O':
                return 1
    return 0
        

#true if filled or false if otherwise
def board_filled(board):
    for i in range(1,10):
        if'1' in board:
            return False
    return True
choice = input("1 - Easy, 2 - Medium, 3 - Hard?")


while not board_filled(game_board) and eval_board(game_board)==0:
    display_board(game_board)
    player_choice(game_board)
    if not board_filled(game_board) and eval_board(game_board)==0:
        computer_choice_hard(game_board)

display_board(game_board)
if eval_board(game_board)== -1:
    print("YOu win")
elif eval_board(game_board)== 1:
    print("I Win.")
else:
    "IT's a tie!"