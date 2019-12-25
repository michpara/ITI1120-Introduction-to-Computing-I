class PingPong:
    '''class that represents ping pong'''

    def __init__(self, sound = 'PONG'):
        '''(PingPong)-> None'''
        self.sound = sound

    def next(self):
        '''(PingPong)->Strng
        switches between PING and PONG'''
        if self.sound == 'PING':
            self.sound = 'PONG'
        else:
            self.sound = 'PING'
        return self.sound
