import random
with open('dictionary/english_popular.txt') as file:
    dictionary = file.read().splitlines()
game_board = [[' ' for j in range(4)] for i in range(4)]
board_set = set()
dice = ['AACIOT', 'ABILITY', 'ABJMOQ', 'ACDEMP', 'ACELRS', 'ADENVZ', 'AHMORS', 'BIFORX', 'DENSOW', 'DKNOTU', 'EEFHIY', 'EGKLUY', 'EGINTV', 'EHINPS', 'ELPSTU', 'GILRUW']

for row in range(4):
    for col in range(4):
      game_board[row][col] = dice.pop(random.randint(0, len(dice) - 1))[random.randint(0, 5)]
        
        
        
    for row in range(4):
        for col in range(4):
            print(game_board[row][col], end='')
            print('u', end='') if game_board[row][col] == 'Q' else print(' ', end='')
            print()
            
            def get_list_with_prefix(prefix, dictionary_set):
                prefix_list = []
                for word in dictionary_set:
                    if prefix.lower() ==  word[:len(prefix)].lower():
                        prefix_list.append(word)
                        return prefix_list
            
def add_letter(board, next_row, next_col, prefix_set=None, word=''):
            if prefix_set is None:
                prefix_set = dictionary 
                
                word += board[next_row][next_col]      
                print(word)
            
            #TODO: add u to Qu
            
            copy = [r[:] for r in board]
            copy[next_row][next_col] = ' '
            
            
            #TODO: add valid words
            
            if len(word) >= 3 and word.lower() in dictionary:
             board_set.add(word)
            
            
            
            
            
            #TODO: CHECK WORD LISTS
            prefix_set = get_list_with_prefix(word,prefix_set)
            if len(prefix_set)>0:
                for row_adjust in range(-1, 2):
                 for col_adjust in range(-1, 2):
                    if (next_row + row_adjust >= 0 and next_row + row_adjust <=3 and next_col + col_adjust >=0 and next_col + col_adjust <=3 and not board[next_row][next_col].isspace()):
                     add_letter(copy, next_row + row_adjust, next_col + col_adjust, prefix_set, word)  
                    
                    
                    
                    
            def find_solution():
                for row in range(4):
                    for col in range(4):
                        add_letter(game_board, row, col)
                        
                        find_solution()
                        print(board_set)
                