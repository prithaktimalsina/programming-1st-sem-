import random
import math
#function notes
#function: a compartmentalized place of code that
#can be reused; in python function are denoted using()
#Functions can have input
print()
print("Hello World!")
#Functions can have more than one input
print("Hello", "Rhodes")
#Functions can have output
print(random.random())
#Functions can have both input and output
print(random.randint(1, 10))
math.sqrt(4)
#User defined functions


#Parts of a Function
def function_name(param1, param2): # 0 to many param
    # function body
    return None #optional

#Function call
function_name(1,2) #args match params

#no parameters, no return
def greet():
    print("Hello There!")
#one param, no return
def greet_personal(name):
    print("Hello" + name + "!")
    name = "Rhodes"
    greet_personal('ben')
    
    #two param, no return
    def greet_birthday(name, age):
        print(f' Happy {age} birthday, {name}!')
        greet_birthday('Rhodes', 21)
        
        #Two param, one return
        def adder(a, b):
            c = a + b
            return c
        
    
        x = adder(['student name'], ['student id'])
        print(x)
        
        
#Distance formula: four param, one return
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    dist = distance(5, 9, 6, 7)       # dist = distance(adder(2, 3), 9, 6, 7)
    print(dist)
    
    #Functions with decisions

    
    
    
    
    #Functions with loops
    def factorial(number):
        for i in range(number - 1, 0, -1):
            number *= i
            return number 
        print(factorial(5))
        
        #bottom-up/top-down programming
        #function stubs
        
        
        
        #Docstring
    
    
       
    