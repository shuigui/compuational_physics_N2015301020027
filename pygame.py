# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 00:12:27 2017

@author: panxiang
"""
import pygame,sys,math
pygame.init()
FPS=5
fpsClock=pygame.time.Clock()
DISPLAYS=pygame.display.set_mode((500,500))
pygame.display.set_caption("canon")
BLUE=(255,255,255)
GRAY=(192,192,192)
canon=pygame.image.load('canon.png')
bgm=pygame.image.load('bgm.jpg')
p=pygame.image.load('p.png')
angle=math.pi/4
canonv0=1000
canonx=10
canony=400
s='s'
DISPLAYS.blit(bgm,(0,0))
DISPLAYS.blit(p,(350,350))

myfont = pygame.font.Font(None,60)
Image = myfont.render("you win", True, (255,0,0))       
        
        
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        if event.type==pygame.MOUSEMOTION:
            a,b=pygame.mouse.get_pos()
            R=((a-10)**2+(b-400)**2)**(1/2)
            h=b-400
            angle=math.asin(h/R)
            canonv0=50
            canonvx=int(canonv0*math.cos(angle))
            canonvy=int(canonv0*math.sin(angle))
            DISPLAYS.blit(canon,(10,400))   
            
        if event.type==pygame.MOUSEBUTTONDOWN:
             pressed_array = pygame.mouse.get_pressed()
             for index in range(len(pressed_array)):
                 if pressed_array[index]:
                    if index == 0:
                        s='start'
    
            
    if s=='start':
        canonx=canonx+canonvx
        canony=canony+canonvy
        canonvx=canonvx
        canonvy=canonvy+10
        DISPLAYS.blit(bgm,(0,0))
        DISPLAYS.blit(canon,(canonx,canony))
        DISPLAYS.blit(p,(350,350)) 
    if (300<canonx<400) and (300<canony<400):
        DISPLAYS.blit(Image, (250,250))
        canonx==350
        canony==350
    pygame.display.update()
    fpsClock.tick(FPS)
if (300<canonx<400) and (300<canony<400):
    DISPLAYS.blit(Image, (250,250))
    canonx==350
    canony==350
    