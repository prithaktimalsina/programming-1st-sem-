import os
import struct


#highscore
score_count = 3
name_max = 20
if not os.path.exists('game_data'):
    os.makedirs('game_data')
    
filepath = os.path.join('game_data', 'scores.dat')

def write_high_scores(filename, scores=None):
    with open(filepath, 'wb') as score_file:
        if scores is None:
             for i in range(score_count):
                 score_file.write(struct.pack(f'{name_max}si', b'empty', 0))
            
        else:
         #TODO: write the actuall highscores to file
            pass
    
def read_high_scores(filename):
        with open(filename,'rb') as score_file:
            unpacked = (struct.unpack(f'{name_max}si' * score_count, score_file.read))
            print(unpacked)
            
            
        scores = []
        for i in range(0, len(unpacked), 2):
            player_name = unpacked[i].decode()
            player_name = ''.join(letter for letter in player_name if letter.isalnum())
            high_score = [player_name, unpacked[i + 1]]
            scores.append(high_score)
        return scores    
            
            
            
def display_high_scores(Scores):
    print(f'\nRank {"Player":<20}Scores')
    print('-' * 30)
    for rank, score_set in enumerate(Scores):
        print(f'{rank + 1:>4} {score_set[0]:<20}{score_set[1]}')
        
            




#write_high_scores(filepath)
high_score = read_high_scores(filepath)

