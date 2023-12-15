# Data Types
x = 7
y = 6.9
name = "prithak"
print(x)


#boolean
light_on = False
cloudy = True



#string: any sequence of characters
#strings are immutable
quote = "Not there stick!"

#case maniulations
quote = quote.upper()
print(quote.upper())
print(quote.lower())
print(quote)


# Indexing
print(quote[7])

#Slicing
print(quote[8:11])
print(quote[:5])
print(quote[5:])  
print(quote[5:-2])    


#Length Function
print(quote[len(quote) - 1])

# Conceatentaion: combinig two strings
print(quote + " - Rafiki")
quote += " -says Rafiki"
print(quote)
quote.replace(' ', '-')
print(quote)

#Formatting Output
last = "Rhodes"
first = "Dr."
print("Hello" + first + " " + last)     #concat
print(f"Hello {first} {last}!")         #3.6+ users
print("Hello {} {}!".format(first, last))
print("Hello %s %s!" % (first, last))            #old schhol

x = 4
print(f"{x:d}")    #decimal
print(f"{x:b}")     #binary
print(f"{x:x}")      #hexadecimal



y = 2.2673104
print(f"{y:.2f}")
print(f"{y:.3f}")

#collection
#lists: mutable collection of elements (may be mixed)
movie = ["50 First Dates", "Adam Sandlers",2004, 7.99]
print(movie)
print(movie[1])                #Indexing
print(movie[1:3])
print(movie[2:1])
print(movie[:2])
print(movie[0][0])


movie.append("8908290")
print(movie)

movie[1] = "Sandler"
print(movie)

movie.insert(2, "Adam")
print(movie)

support = ['Bairimore', "Drew"]
#movie.extend(support)
movie += support
print(movie)

movie.remove("8908290")
print(movie)

print(len(movie))
print(movie.index('Drew'))
print(movie.count(7.99))

#tuple: immutable list
movie2 = ('Big Daddy', 'Sandler', 'Adam', 6.99)              #tuple no output??
#movie2[3] = 12.99
print(movie2)

#named tuple
from collections import namedtuple
film = namedtuple('Film', ['title', 'author', 'price'])
film1 = film('Waterboy', 'Sandler', 13.99)
print(film1)

print(film1.title)


#sets: mutable, non-indexed doohickey (Braxton) of unique values
comedy =  {'Sandler', 'Black', 'Pratt', 'Tatum', 'Tucker', 'Black'}
action ={'Reeves', 'Willis' , 'Gibons Black'}
print(comedy)
print(action)

print(comedy.intersection(action))           #And
print(comedy.union(action))                  #And/or
print(comedy.difference(action))            #Not
print(comedy.symmetric_difference(action))    #xor

#Dictionaries: set of key/values pairs
movie = {
    'title':"50  first dates",
    'actor':"Sandler,Adam",
    'year': 2004,
    'price': 7.99,
    15:67
 
}

movie['price'] = 12.99
print(movie[15])













#Dictionaries: