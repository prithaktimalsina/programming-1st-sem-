#class definition(blueprint)
import random


class Avatar:
    count = 0
     #constructor
def __init__(self, name, weapon='Stick', health=10, strength=20, defense=20):
         self.name = name
         self.health = health
         self.weapon = weapon
         self.strength = strength
         self.defense = defense
         Avatar.count += 1
         
         def __str__(self):
             return f"{self.name} ({self.weapon}): {self.health}"
         
@property
def name(self):
            return self._name = ''.join(letter for letter in name if letter.isalpha())
        
@name.setter
def name(self, name):
            return self 
         
@property
def health(self):
    return self._health

@health.setter
def health(self, health):
    self._health = health if health > 0 else 0
        
@staticmethod
def _success(self_attr, opp_attr):
    return random.randint(1, self_attr * 2) >= opp_attr
        

         
def attack(self, opponent):
             if not isinstance(opponent, Avatar):
                 raise TypeError(f'Expected <class Avatar>: The atatck method cannot be used with {type(opponent)}')
             print(self.name + " prepares to attack" + opponent.name + "......")
             
             if Avatar._success(self.strength, opponent.defence):
                        damage = random.randint(1, self.strength)
                        print(".... and strikes successfully")
                        opponent.health -= damage
                        
            
         
player = Avatar('Artimus', 'Sword', 50, 100, 100)
enemy = Avatar('Elsita', 'Bow', 30, 200, 200)
small_enemy = Avatar('Skeleton', 'Bonestaff')

player.name = 'Steve1234@%!Jobs'
print(player.name)
player.health = 25
print(player.health)

print("Number of avatars ", Avatar.count)
print(f'{player.name} encouters {enemy.name}...')
print(f'\n{player}\n{enemy}\n')

flee = False
response = input('What will you do? (F)ight or (R)un away? ')

if response.upper() == 'F':
    player.attack(enemy)
    
    print(f'\n{player}\n{enemy}\n')
    
    if enemy.health > 0:
        print(f'\n{enemy.name} is preparing to attack.')
        response = input('What will you do? (D)efend or (A)ttack?')
        
        if response.upper()=='D':
            enemy.attack(player)
        else:
            flee = True
    else:
        flee = True
        
if flee:
    print(f'{player.name} flees like a coward.')
elif player.health > 0:
    print(f'{enemy.name} stumbles to the ground in defeat')
else:
    print(f'{player.name} is dead.')
    
    
player.attack(enemy)
print(f'\n{player}\n{enemy}\n')