import random




print("Welcome to Hangman!")




def choose_word():
   words = ['extra', 'mango', 'cheat', 'phone', 'mouse']
   return random.choice(words)




hangman_pics = ['''
    +---+
        |
        |
        |
        |
        |
       ===''', '''
    +---+
   O   |
       |
       |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
       |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
       |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
       |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
       |
       |
      ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
      |
      |
     ===''']


lose_win = ['''
    +---------------------+
    |                     |
    |                     |
    |      You Win        |
    |                     |
    |                     |
    +---------------------+''', '''
    +---------------------+
    |                     |
    |                     |
    |      You Lose       |
    |                     |
    |                     |
    +---------------------+''']


letters = ['_', '_', '_', '_', '_']
choice=choose_word()
print(choice)




hang_num=0
attempts=len(hangman_pics)-1
correct_num=0
while True:
    user = input("Choose a letter : ")
    for i in range(0,5):
        if user==choice[i]:
            letters[i]=choice[i]
            correct_num+=1
            print(letters)
            break
           
           
    else:
        attempts-=1
        print(hangman_pics[(len(hangman_pics)-1)-attempts])
       
       


    if attempts==0:
        print(lose_win[1])
        break
    elif correct_num==5:
        print(lose_win[0])
        break
