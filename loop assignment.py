import random
#Ask the user for a number
target = input("What number between 2 and 12: ")

if not(target <2 or target >12):
#Roll a pair of dice
#Loop until thenumber id reached
d1 = d2 = rolls =  0
while d1 + d2 != target and target >= 2 and target <= 12:
    rolls += 1
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    print(f'[{d1}][{d2}]')

#count the number of rolls
print("Number of rolls:" + str(rolls))

#Sentinel value: value to determine when the loop should stop
#sentineal value should not be part of the acceptable data set

total = count = response = 0
while response != 'd':
    response = float(input("Enter a number (-1 to quit): "))
    if response > -1:
        total += float(response)                        #d is a sentineal value. why? bcz it isn't actually a part of programm and won't affect the program.
        count += 1
        print(f"Average: {total / count:.3f}")
        
        
        
        #while - the number of iterations is not known
        #for - the number of iterations is known
        #for (in) - for use with a collection
        #lists
        students = ['Ben', 'Andrew', 'Esther', 'Braxton', 'Shreeya']
        for name in students:
            print(name.upper())
            print("Hello" + name + "!")
            
        #Dict
        pop = {
            'California': 39029,
            'Utah': 3380,
            'Wyoming': 581
        }
        for state in pop:
            print(state + ":" + str(pop[state] * 1000))
            
            
        #string
        message = '4#3T@hrroughwfhw@63q6272368'
        for letter in message:
           if 97 <= ord(letter.lower()) <= 122:
            print(letter + '_', end='')
            
            
            
            
            for num in range(10):
                print("Elmo says", num)
                
#Nested for loops
    #example 1: math
    for i in range(1, 13):
        for j in range(1, 13):
            print(f'{i * j}:>5', end=' ')  
            print()  

    #Example 2: grid (rudimentary boggle)
for row in range(0,4):
    for col in range (0,4):
        print(f'{chr(random.randint(65, 90))}', end=' ')
        print()


#Break
    #example: 
    for i in range(0, 10):
        if i ==5:
            break     #can be used continue as well. WIth continue skip to the lat of code and keep going.
        print(i)
    #example2:
    animals = ['ant', 'bat', 'cat', 'dog', 'emu','fox']
    response = input("Three-letter-animal: ")
    for animal in animals:         #for i in range(6):
        if animal == response:     #if animals[i] == response:
            print("Found")         #print("Found at", i)
                                    #break




#Loop else
#enumerate
#fence post
#slot machine demo
#tricky loop scope