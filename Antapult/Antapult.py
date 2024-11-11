# This set of code was honestly just me attempting to get a handle on python, 
# and using that knowledge for basic sprite changes

import thumby


from sys import path
if not '/Games/CharTest' in path:
    path.append( '/Games/CharTest' )

import displaymanager
import inputmanager

# BITMAP: width: 8, height: 8
catMap = bytearray([0,128,190,188,184,168,184,184,184,184,168,184,188,190,128,128,
           0,0,2,6,6,5,5,5,5,5,5,5,5,0,0,0])
           
# BITMAP: width: 16, height: 16
altCatMap = bytearray([255,255,255,255,3,143,223,31,31,223,143,3,255,255,255,255,
           255,255,255,255,254,254,252,252,252,252,254,254,255,255,255,255])

catSprite = thumby.Sprite(16, 16, catMap+altCatMap)
catSprite.x = 29 # Initial placement - middle of screen
catSprite.y = 15

thumby.display.setFPS(45) # set frame rate, between 30-60 is usually best

dispMan = displaymanager.displayManager
inpHand = inputmanager.inputManager

# Begin main game loop that runs for the course of the game
while(True):
    dispMan.displaySetUp()

    inpHand.playerMovement()
    
    thumby.display.update()