import math
class Point:
    'class that represents a point in the plane'

## exectuting Point(2,3)
## 1. creates an object of type point
## 2. calls an objects __init__ method
## 3. produces an object's memory address

## Assigning to a new variable using dot operator
## CREATES THAT VARIABLE INSIDE OF THE OBJECT

## Variables INSIDE of an object are called INSTANCE variables

## __init__ is method that is called to initialize the object (create it and initialize its variables)
## the first parameter of method is usually called self
## self refers to the object that is being initialized


#    constructor
#    notice two underscores
    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point, float, float) -> None
        >>> p=Point(2,3)
        >>> p.x
        >>> 2
        >>> p.y
        >>> 3

        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,float)->None
        set x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,float)->None
        set y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        return a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,float,float)->None
        change the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        'self == other if they have the same coordinates'
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        'return canonical string representation Point(x, y)'
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def distance(self,other):
        """(Point, Point) -> float
        Returns the distance between two point
        """
        return math.sqrt((self.x - other.x)**2 +(self.y - other.y)**2)
    def up(self):
        """(Point) -> None
        Moves Point up by 1
        """
        self.move(0, 1)
    def down(self):
        """(Point) -> None
        Moves Point down by 1
        """
        self.move(0,-1)
    def left(self):
        """(Point) -> None
        Moves Point left by 1
        """
        self.move(-1, 0)
    def right(self):
        """(Point) -> None
        Moves Point right by 1
        """
        self.move(1,0)
class Animal:
    'represents an animal'

    def __init__(self, species='animal', language='make sounds', age = 0):
        self.spec = species
        self.lang = language
        self.age = age

    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def speak(self):
        'prints a sentence by the animal'
        print('I am a', self.spec,'and I', self.lang)
    
    def getAge(self):
        """(Animal) -> int
        Returns age of the animal.
        """
        return self.age
class Bird(Animal): # class Bird inherits all atributes (data and method) from class Animal 
    'represents a bird'

    def speak(self):
        'prints bird sounds'
        print(self.language * 3)



class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit    

    def __repr__(self):
        'return formal representation'
        return 'Card('+self.rank+','+self.suit+')'

    def __eq__(self, other):
        'self == other if rank and suit are the same'
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        """(Card, Card) -> bool
            Return True if the rank of the card on the left,self
            is less than the rank of the card compared with it, other.
            Otherwise False
        """
        return int(self.rank) < int(other.rank)
    def __le__(self, other):
        """(Card, Card) -> bool
            Return True if the rank of the card on the left,self
            is less than or equal to the rank of the card compared with it, other.
            Otherwise False
        """
        return int(self.rank) <= int(other.rank)
    
    def __gt__(self, other):
        """(Card, Card) -> bool
            Return True if the rank of the card on the left,self
            is greater than the rank of the card compared with it, other.
            Otherwise False
        """
        return int(self.rank) > int(other.rank)
    
    def __ge__(self, other):
        """(Card, Card) -> bool
            Return True if the rank of the card on the left,self
            is greater than or equal to the rank of the card compared with it, other.
            Otherwise False
        """
        return int(self.rank) >= int(other.rank)
class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    # suits is a set of 4 Unicode symbols representing the 4 suits 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = []          # deck is initially empty

        for suit in Deck.suits: # suits and ranks are Deck
            for rank in Deck.ranks: # class variables
                # add Card with given rank and suit to deck
                self.deck.append(Card(rank,suit))

    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        return self.deck.pop()

    def shuffle(self):
        'shuffle the deck'
        random.shuffle(self.deck)


    def __len__(self):
        'returns size of deck'
        return len(self.deck)

    def __repr__(self):
        'returns canonical string representation'
        return 'Deck('+str(self.deck)+')'

    def __eq__(self, other):
        '''returns True if decks have the same cards
           in the same order'''
        return self.deck == other.deck

class BankAccount:
    def __init__(self, balance=0):
        self.bal = float(balance)
        
    def withdraw(self, amount):
        """(BankAccount, number) -> None
        Takes amount from the balance of the BankAccount
        """
        self.bal -= amount
    
    def deposit(self, amount):
        """(BankAccount, number) -> None
        Adds amount to the balance of the BankAccount
        """
        self.bal += amount

    def balance(self):
        """(BankAccount) -> float
        Returns a nice representation of the balance of the account (2 decimal places)
        """
        return '{:.2f}'.format(self.bal)
    def __repr__(self):
        """Return Canonical representation"""
        return 'BankAccount({:.2f})'.format(self.bal)

class PingPong:
    def __init__(self):
        self._msg = "PING"
        self._next = "PONG"
    def next(self):
        """(PingPong) -> None
        Alternatively prints ping ang pong
        """
        print(self._msg)
        self._msg, self._next = self._next, self._msg

class Queue:
    def __init__(self):
        self._queue = []
    def enqueue(self, item):
        """(Queue, object) -> None
        Adds item to end of queue
        """
        self._queue.append(item)
    def dequeue(self):
        """(Queue) -> Object
        Return and remove first element in queue.
        """
        return self._queue.pop(0)
    def isEmpty(self):
        """(Queue) -> bool
        Return whether or not queue is empty
        """
        return len(self._queue) == 0
    def __eq__(self, other):
        """(Queue, Queue) -> bool
        Return True if all elements in queue are the same
        and in the same position. Otherwise False.
        """
        return self._queue == other._queue
    def __len__(self):
        """(Queue) -> int
        Returns size of the queue
        """
        return len(self._queue)
    def __repr__(self):
        """(Queue) -> str
        Returns canonical representation Queue([items,...])
        """
        return "Queue({})".format(self._queue)

class Vector(Point):
    def __init__(self, x=0,y=0):
        super().__init__(x,y)

    def __repr__(self):
        """(Vector) -> str
            Returns the canonical repersentation of the vector Vector(x,y)
        """
        return "Vector({}, {})".format(self.x,self.y)
    
    def __add__(self, other):
        """(Vector, Vector) -> Vector
            Returns a new vector that is the sum of the corresponding coordinates of
            self and other.
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        """(Vector, Vector) -> number
            Returns the sum of the products of the corresponding coordinates of
            self and other
        """
        return self.x * other.x + self.y * other.y
    
class Marsupial:
    def __init__(self, colour):
        self._colour = colour
        self._pouch = []
    def __str__(self):
        """(Marsupial) -> str
            Returns a nice string message describing the marsupial.
        """
        return "I am a {} Marsupial.".format(self._colour)

    def put_in_pouch(self, item):
        """(Marsupial, Object) -> None
            Adds the item into the pouch of the marsupial
        """
        self._pouch.append(item)

    def pouch_contents(self):
        """(Marsupial) -> list
            Returns a list containing every object in the marsupial's pouch
        """
        return self._pouch

class Kangaroo(Marsupial):
    def __init__(self, colour, x=0, y=0):
        super().__init__(colour)
        self._x = x
        self._y = y
    def jump(self, dx, dy):
        """(Kangaroo, number, number) -> None
        Moves the kangaroo by dx units in the x axis and dy units in the y axis.
        """
        self._x += dx
        self._y += dy
    
    def __str__(self):
        """(Kangaroo) -> str
            Returns a string describing the kangaroo
        """
        return "I am a {} Kangaroo located at coordinates ({},{})".format(self._colour, self._x, self._y)

class Points:
    def __init__(self, plane=[]):
        self._plane = plane

    def add(self, x, y):
        """(Points, number, number) -> None
        Adds a new point at x,y into the Plane
        """
        self._plane.append(Point(x,y))

    def __len__(self):
        """(Points)->int
            Returns the number of items in the plane.
        """
        return len(self._plane)

    def left_most_point(self):
        """(Points) -> Point
        Returns the left most point in the plane, if there is a tie, returns the
        bottom left most.
        """
        tmp = self._plane[0]
        for point in self._plane:
            if point.x < tmp.x or point.x == tmp.x and point.y < tmp.y:
                tmp = point
        return tmp

    def __repr__(self):
        """(Points) -> str
        Returns Canonical representation of form Points([Point(,)...Point(,)])
        """
        return "Points({})".format(self._plane)
            
