class PingPong:


    def __init__(self, sound = 'PONG'):
        '''(Point)-> None'''
        self.sound = sound

    def next(self):
        '''switches between PING and PONG'''
        if self.sound == 'PING':
            self.sound = 'PONG'
        else:
            self.sound = 'PING'
        return self.sound
