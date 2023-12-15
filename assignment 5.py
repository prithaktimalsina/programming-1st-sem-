#Relation operators/relational expressions

 #Relational Expression: Expression returns True or False
#Made using relational operators: >, <, ==, >=, <=,!=
#Usage:[operand] [rel op] [operand]
# = single equals is assignment
# == used for realtional comparsion
print(5 == 7) #true
print(x = 7) #false


#Boolean Variables (expression)
is_light_on = False
age = 5 +7
can_vote = age > 18
print(can_vote)

#Membership identity (in, not in, is, is not)
name = "Lance P. Rhodes"
print("Dillion" not in name)
movies = ['Die hard', '6th sense', 'Surrogates']
print('Die Hard 2' in movies) #won't generate output cuz not in movies
x = 7
y = 8
w = x
print(x is y)
print(x is w)

#Logical operators (and, or,not)
#and:  used to combine two or more relation expression into a single expression, the result are only true if all sub-expression are true.

gas = 5
money = 15
needs = True
print("To store:", (gas > 3 and money > 20 and needs == True))

#or
#not
