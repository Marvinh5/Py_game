import game_object

class pad(game_object.game_object):
    
    def __init__(self, game, image):
        super(pad, self).__init__(game, image)
        self.__speed = 12
            
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, y):
        self.__speed = y        
