from Sim import *
import sys
from playsound import playsound
import threading
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

icon = pygame.image.load("icon.ico")
cmcSns = pygame.font.SysFont("Comic Sans MS", 30)

def playDayPassSound():
    playsound("DayPassSFX.wav")

sim = simulation()
susceptibleNum = sim.population - 1
infectedNum = 1

#loading in images
susceptibleIconImage = pygame.transform.scale(pygame.image.load("SusceptibleIcon.png"), (40,40))
deadIconImage = pygame.transform.scale(pygame.image.load("DeadIcon.png"), (40,40))
infectedIconImage = pygame.transform.scale(pygame.image.load("InfectedIcon.png"), (40,40))
immuneIconImage = pygame.transform.scale(pygame.image.load("ImmuneIcon.png"), (40,40))
numAliveIconImage = pygame.transform.scale(pygame.image.load("TotalAliveIcon.png"), (40,40))
dayIconImage = pygame.transform.scale(pygame.image.load("dayIcon.png"), (40,40))

#text stuff
ns = str(sim.peopleGroups[0])
sDisplay = "= " + ns

ninf = str(sim.peopleGroups[1])
infDisplay = "= " + ninf

nd = str(sim.peopleGroups[2])
dDisplay = "= " + nd

nim = str(sim.peopleGroups[3])
imDisplay = "= " + nim

d = str(sim.day)
dayDisplay = "= " + d

#pygame stuff
BACKGROUND = (0,0,0)
WHITE_COLOR = (255, 255, 255)

FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 390
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
gameDisplay = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_icon(icon)

#loading text
def displayText():
    numSusceptibileTxt = cmcSns.render(sDisplay, False, (255, 255, 255))
    gameDisplay.blit(numSusceptibileTxt, (120,25))
    
    numInfectedTxt = cmcSns.render(infDisplay, False, (255,255,255))
    gameDisplay.blit(numInfectedTxt, (120, 75))
    
    numDeadTxt = cmcSns.render(imDisplay, False, (255,255,255))
    gameDisplay.blit(numDeadTxt, (120, 125))
    
    numImmuneTxt = cmcSns.render(dDisplay, False, (255,255,255))
    gameDisplay.blit(numImmuneTxt, (120, 175))
    
    numDaysTxt = cmcSns.render(dayDisplay, False, (255,255,255))
    gameDisplay.blit(numDaysTxt, (120,225))
    
    NewDayTxt = cmcSns.render("Next Day", False, (255,255,255))
    gameDisplay.blit(NewDayTxt, (75, 300))

#displaying images
def displayImages():
    gameDisplay.blit(susceptibleIconImage, (75,25))
    gameDisplay.blit(infectedIconImage, (75,75))
    gameDisplay.blit(immuneIconImage, (75,125))
    gameDisplay.blit(deadIconImage, (75,175))
    gameDisplay.blit(dayIconImage, (75,225))
    pygame.draw.rect(gameDisplay, (89, 89, 89), pygame.Rect(70, 300, 140, 50))




looping = True
while looping:
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(70 <= mouse[0] <= 210 and 275 <= mouse[1] <= 335):
                sim.stepDay()
                a = threading.Thread(target=playDayPassSound)
                a.start()
        
        #text updates
        ns = str(sim.peopleGroups[0])
        sDisplay = "= " + ns

        ninf = str(sim.peopleGroups[1])
        infDisplay = "= " + ninf

        nd = str(sim.peopleGroups[2])
        dDisplay = "= " + nd

        nim = str(sim.peopleGroups[3])
        imDisplay = "= " + nim
        
        d = str(sim.day)
        dayDisplay = "= " + d
        
        #loading
        WINDOW.fill(BACKGROUND)
        
        displayImages()
        displayText()
        
        pygame.display.update()
        fpsClock.tick(FPS)



'''
To make this project(both this file,- and the sim.py file), I used these websites as reference/for help:

https://www.geeksforgeeks.org/multithreading-python-set-1/    -    geeks for geeks
https://pythonbasics.org/python-play-sound/     -     python basics
https://stackoverflow.com/questions/27770602/pygame-rect-what-are-the-arguments     -     stack overflow    
https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame#20842987     -     stack overflow
https://pythonprogramming.net/displaying-images-pygame/     -     python programming

'''
