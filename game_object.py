import os, pygame

class game_object(pygame.sprite.Sprite):
    def __init__(self, game, image):
        game.sprite.Sprite.__init__(self)
        self.__game = game
        self.image = game.image.load(image).convert()
        self.__rect  = self.image.get_rect()
        self.image.set_colorkey((255,255,255))
        self.__width = self.__rect.width
        self.__height = self.__rect.height

    
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def x(self):
        return self.__rect.x
    
    @x.setter
    def x(self, x):
        self.__rect.x = x
    
    @property
    def y(self):
        return self.__rect.y
    
    @y.setter
    def y(self, y):
        self.__rect.y = y
    
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height