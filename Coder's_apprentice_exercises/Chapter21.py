"""#InChapter20, a Rectangle class was defined. Add to this class operators to test for
# equality of rectangles (two rectangles are equal if they have exactly the same shape),
# and greater/smaller operators (a rectangle is smaller than another rectangle if it has
# a smaller surface area). Test the new operators.

class Point:
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y
    def __repr__(self):
        return "({},{})".format(self.x,self.y)


class Rectangle:
    def __init__(self, point, width, height):
        self.point=point
        self.width=abs(width)
        self.height=abs(height)
    def __repr__(self):
        return "[{},w = {},h = {}]".format(self.point,self.width,self.height)
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2*self.width + 2*self.height
    def BRcorner(self):
        return Point(self.point.x + self.width, self.point.y + self.height)
    def __eq__(self, r):
        if r.width == self.width and r.height == self.height:
            return True
        else:
            return False
    def __gt__(self, r):
        if self.area() > r.area():
            return True
        else:
            return False
    def __lt__(self, r):
        if self.area() < r.area():
            return True
        else:
            return False

r1 = Rectangle(Point(2,3),5,2)
r2 = Rectangle(Point(5,1),4,3)

print(r1 == r2)
print(r2 > r1)"""

"""
class MesosticWord:
    def __init__(self, word, index, question):
        self.word = word
        self.index = index
        self.question = question


class Mesostic:
    def __init__(self, name, words):
        self.name, self.words = name, words

    def __len__(self):
        return len(self.words)

    def __getitem__(self, n):
        return self.words[n]

    def __setitem__(self, n, value):
        self.words[n] = value

    def __delitem__(self, n):
        del self.words[n]

    def display(self):
        print(self.name)
        for i in range(len(self)):
            print("{}. {}".format(i + 1, self[i].question),
                  end="  ")
            for j in range(len(self[i].word)):
                if j == self[i].index:
                    print("* ", end="")
                else:
                    print("_ ", end="")
            print()

    def solution(self):
        s = ""
        for i in range(len(self)):
            s += self[i].word[self[i].index]
        return s


puzzle = Mesostic(
    "The Monty Python and the Holy Grail Mesostic Puzzle",
    [MesosticWord("ANTHRAX", 5,
                  "Sir Galahad's tale took place in the Castle"),
     MesosticWord("PERIL", 2,
                  "Sir Robin was thrown into the Gorge of Eternal"),
     MesosticWord("RABBIT", 5,
                  "Sir Bors was killed by a"),
     MesosticWord("SHRUBBERY", 1,
                  "The Knights of Ni!'s first demand was to get a"),
     MesosticWord("COCONUT", 5,
                  "A horse can be replaced by a"),
     MesosticWord("MINSTRELS", 5,
                  "They were forced to eat Robin's")])

puzzle.display()
"""


"""#A Sentence is a list of words. A basic Sentence class is given below.
# Implement __len__(), __getitem__(), __setitem__(), and __contains__() methods for this class.

class Sentence:
    def __init__( self, words ):
        self.words = words
    def __repr__( self ):
        return " ".join( self.words )
    def __len__(self):
        return len(self.words)
    def __getitem__(self, n):
        return self.words[n]
    def __setitem__(self, n, value):
        self.words[n] = value
    def __contains__(self, word):
        if word in self.words:
            return True
        else:
            return False


s = Sentence( [ "There", "is", "only", "one", "thing", "worse",
"than", "being", "talked", "about",
"and", "that", "is", "not", "being", "talked", "about" ] )
print( s )
print( len( s ) )
print( s[5] )
s[5] = "better"
print( "better" in s )
"""

"""
#Exercise 21.1
#A playing card consists of a suit ("Hearts", "Spades", "Clubs", "Diamonds") and a
# value (2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"). Implement a Card class.
# Implement that cards are equal when they have an equal rank, and that the other comparisons
# use the ranks in the order given above (2 lowest, Ace highest). Test the class.

class Card:
    def __init__(self,value,suit):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return "{} of {}".format(self.value,self.suit)
    def __eq__(self, card):
        if self.value == card.value:
            return True
        else:
            return False
    def __gt__(self, card):
        if isinstance(self.value,int) and isinstance(card.value,int):
            if self.value > card.value:
                return True
            else:
                return False
        else:
            if self.value == "Ace":
                return True
            elif self.value == "King" and (card.value == "Queen" or card.value == "Jack" or
                  isinstance(card.value,int)):
                return True
            elif self.value == "Queen" and (card.value == "Jack" or isinstance(card.value,int)):
                return True
            else:
                return False

suits =["Hearts", "Spades", "Clubs", "Diamonds"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

deck=[]
for i in suits:
    for j in values:
        deck.append(Card(j,i))

#Exercise 21.2
#Use the Card class as given above. Now also create a Drawpile class. A Drawpile consists of a sequence of cards.
# The cards are supposed to form a pile with the top card having the lowest index,
# and the bottom card the highest index. Implement the __len__() and __getitem__() methods.
# Create an add() method to add a card to the drawpile at the bottom, and a draw() method
# to remove the top card from a drawpile and return it. Test the class.

from random import sample

class Drawpile:
    def __init__(self, drawpile=[]):
        self.drawpile = drawpile
    def __repr__(self):
        return "{}".format(self.drawpile)
    def __len__(self):
        return len(self.drawpile)
    def __getitem__(self, n):
        return self.drawpile[n]
    def __contains__(self, card):
        if card in self.drawpile:
            return True
        else:
            return False
    def add(self, card):
        if card not in self.drawpile:
            return self.drawpile.append(card)
    def remove(self):
        if len(self) <= 0:
            return None
        return self.drawpile.pop(0)

randeck = sample(deck, 25)
randeck = Drawpile(randeck)


#Exercise 21.3
#Using the definitions created in the previous exercises, create two drawpiles.
# The first has the 2 of Diamonds, King of Hearts, and 7 of Clubs (in this order).
# The second has the 4 of Hearts, 3 of Hearts, and 8 of Spades (in this order). Let the draw piles play “War!”
# This game is played as follows: Draw the top card from each deck. The highest of these cards goes on
# the bottom of its own deck, and the other card goes there too. The game continues until there is only
# one pile left.

deck1 = [Card(2,"Diamonds"),Card("King","Hearts"),Card(7,"Clubs")]
deck2 = [Card(4,"Hearts"),Card(3,"Hearts"),Card(8,"Spades")]

deck1 = Drawpile(deck1)
deck2 = Drawpile(deck2)


def war(d1,d2):
    round=1
    while True:
        if len(d1) == 0:
            print("Deck 2 wins")
            break
        if len(d2) == 0:
            print("Deck 1 wins")
            break
        print("This is round number {}".format(round))
        c1 = d1.remove()
        c2 = d2.remove()
        if c2 > c1:
            d2.add(c2)
            d2.add(c1)
            print("Deck 2 wins this round")
        else:
            d1.add(c1)
            d1.add(c2)
            print("Deck 1 wins this round")
        round+=1

war(deck1,deck2)
"""


#Exercise 21.4
#Implement a FruitBasket class. The FruitBasket contains fruit items, and it may contain a certain number
# of each item type. Keep it simple: store the fruit items as a dictionary, with the name of the fruit as key,
# and the quantity as value. For this exercise there is no need to limit what keys can be, anything can be the
# name of a fruit. Implement the __add__() method to add a piece of fruit to the basket (and it might be a
# good idea to also implement __iadd()__), and implement the __sub__() method to remove a piece of fruit from
# the basket (and __isub__() is a good candidate too). Implement the __contains__() method to check if a certain
# kind of fruit is in the basket. Also implement __getitem__() to check how much of a piece of fruit there is,
# __setitem__() to add a whole bunch of a piece of fruit at once, and __len__() to check how many different
# pieces of fruit there are in the basket. Note that when nothing more of a piece of fruit remains in the basket,
# you have to remove the key.

from copy import deepcopy

class FruitBasket:
    def __init__(self,basket={}):
        self.basket = basket
    def __repr__(self):
        s = ""
        sep = "["
        for fruit in self.basket:
            s+= sep + fruit + ":" + str(self.basket[fruit])
            sep = ", "
        s+="]"
        return s
    def __contains__(self, fruit):
        return fruit in self.basket
    def __add__(self, fruit):
        fbcopy=deepcopy(self)
        fbcopy.basket[fruit] = fbcopy.basket.get(fruit,0)+1
        return fbcopy
    def __iadd__(self, fruit):
        self.basket[fruit]=self.basket.get(fruit,0)+1
        return self
    def __sub__(self, fruit):
        if fruit not in self.basket:
            return self
        fbcopy=deepcopy(self)
        fbcopy.basket[fruit]=fbcopy.basket.get(fruit,0)-1
        if fbcopy.basket[fruit]<=0:
            del fbcopy.basket[fruit]
        return fbcopy
    def __isub__(self, fruit):
        self.basket[fruit] = self.basket.get(fruit, 0) - 1
        if self.basket[fruit]<=0:
            del self.basket[fruit]
        return self
    def __len__(self):
        return len(self.basket)
    def __getitem__(self, fruit):
        return self.basket.get(fruit,0)
    def __setitem__(self, fruit, n):
        if n<=0:
            if fruit in self.basket:
                del self.basket[fruit]
        else:
            self.basket[fruit]=n

fb = FruitBasket()
fb += "apple"
fb += "apple"
fb += "banana"
fb = fb + "cherry"
fb["orange"] = 20
print( len( fb ) )
print( fb )
print( "banana" in fb )
print( "durian" in fb )
fb -= "apple"
fb -= "banana"
fb = fb - "cherry"
fb -= "durian"
print( fb )
print( "banana" in fb )
fb["orange"] = 0
print( fb )
