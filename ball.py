from game_object import game_object
from shared import direction
import game_constants

class ball(game_object):
    
    def __init__(self, game, image):
        self.__direction = direction(-1, -1)
        self.__dead = False
        self.__speed = 4
        super(ball, self).__init__(game, image)
        
    @property    
    def direction(self):
        return self.__direction
    
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, new_speed):
        self.__speed = new_speed
    
    @direction.setter
    def direction(self, direction):
        self.__direction = direction
    
    def is_dead(self):
        return self.__dead
    
    
    def move_x(self):
        if self.x  + self.__speed * self.__direction.x <= game_constants.game_size.width - self.width and self.x + self.__speed * self.__direction.x >= 0:
            self.x += self.__speed   * self.__direction.x
        else:
            self.__direction.x *= -1
            self.x += self.__speed   * self.__direction.x            
    
    def move_y(self):
        if  self.y > 0:
            self.y += self.__speed   * self.__direction.y
        else:
            self.direction.y *= -1
            self.y += (self.__speed * self.__direction.y)
            
        if self.y + self.height >= game_constants.game_size.height:             
            self.__dead = True
            print "Dead"
            self.kill()
        else:
            self.__dead = False