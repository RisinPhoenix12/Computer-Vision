import pygame
from time import sleep


class img(object):

    def __init__(self):

        #loading the required images
        self.ghosti=pygame.image.load('pacmang.png')
        self.pacl=pygame.image.load('pacmanl.png')
        self.pacr=pygame.image.load('pacmanr.png')

        #setting sizes of images
        self.ghosti=pygame.transform.scale(self.ghosti,(50,50))
        self.pacl=pygame.transform.scale(self.pacl,(50,50))
        self.pacr=pygame.transform.scale(self.pacr,(50,50))
        
        self.x=0
        self.y=10
        self.xspd=0
        self.yspd=0
        self.h=50
        self.w=50
        

 
    