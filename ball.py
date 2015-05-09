from game_object import game_object
from shared import direction
import game_constants

class ball(game_object):
    
    def __init__(self, game, image):
        self.__direction = direction(-1, -1)
        super(ball, self).__init__(game, image)
        
    @property    
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self, direction):
        self.__direction = direction
    
    def move_x(self, speed = 4):
        if self.x  + speed * self.__direction.x <= game_constants.game_size.width - self.width and self.x + speed * self.__direction.x >= 0:
            self.x += speed   * self.__direction.x
        else:
            self.__direction.x *= -1
            self.x += speed   * self.__direction.x            
    
    def move_y(self, speed = 4):
        if  self.y > 0:
            self.y += speed   * self.__direction.y
        else:
            self.y += (speed * -1)
            
        if self.y + self.height >= game_constants.game_size.height:             
            self.kill()
            print "dead"