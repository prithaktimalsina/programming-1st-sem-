#set
mysteryauthor = {'Grisham, Patterson, Baldacci, Koontz, Petrie'}
fictionauthor = {'King, Koontz, Patterson, Crichton, Child'}
print(mysteryauthor)
print(fictionauthor)
print(mysteryauthor.intersection(fictionauthor))
print(mysteryauthor.union(fictionauthor))
print(mysteryauthor.difference(fictionauthor))
print(mysteryauthor.symmetric_difference(fictionauthor))


#lists
price = [3.99, 4.99, 1.99, 17.99, 18.99, 2.99]
print(min(price))
print(max(price))
print(f'{sum(price):.2f}')


from collections import namedtuple
#Tuple
book = namedtuple("book", ['title','author', 'isbn', 'price'])
book_p= book["Life of a fly", "ALex Gotham", 993, 49.99]

#String
institution = "Weber State University Libary"
print(institution[0] + institution[6] + institution[12] + institution[22:1])


#Dictionaries
book = {
    "F Child": "Never Go Back",
    "F Baldacci": "Mercy",
    "F King": "The Stand",
    "F Crichton": "Sphere"   
}



