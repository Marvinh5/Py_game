import game_object, pygame

class brick(game_object.game_object):
    
    def __init__(self, game, image):
        super(brick, self).__init__(game, image)
        self.__lives = 2
        self.__image = image
    
    def reduce_lives(self):
        
        self.__lives -=1
        
        if self.__lives  == 1:
            self.image = pygame.image.load(self.__image.replace(".png", "_broke.png")).convert()
            
        if self.__lives < 1:
            self.kill()
        