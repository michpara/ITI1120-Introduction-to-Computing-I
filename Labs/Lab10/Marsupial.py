class Marsupial:
    '''class that represents a marsupial'''
    
    def __init__(self, colour, items = []):
        '''(Marsupial, String, List)->None'''
        self.colour = colour
        self.items = items
        
    def put_in_pouch(self, item):
        '''(Marsupial, String)->()
        adds item to items'''
        self.items.append(item)

    def pouch_contents(self):
        '''(Marsupial)->List
        returns the list of items'''
        return self.items

    def __repr__(self):
        '''(Marsupial)->String
        formal representation of Marsupial'''
        return 'I am a ' + self.colour + ' Marsupial.'

class Kangaroo(Marsupial):
    '''class that represents a Kangaroo which is a marsupial'''
    
    def __init__(self, colour , xcoord = 0, ycoord = 0, items = []):
        '''(Kangaroo, String, Number, Number, List)->None'''
        self.colour = colour
        self.items = items
        self.x = xcoord
        self.y = ycoord

    def jump(self, dx, dy):
        '''(Kangaroo, Number, Number)->()
        moves the kangaroo by dx and dy'''
        self.x += dx
        self.y += dy

    def __str__(self):
        '''(Kangaroo)->String
        string representation of Kangaroo'''
        return 'I am a ' + self.colour + ' Kangaroo located at coordinates (' + str(self.x) + ',' + str(self.y) + ')'
