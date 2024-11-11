import thumby
import displaymanager

dispMan = displaymanager.displayManager

# Number of pixels sprite will move - increasing this makes movement choppy 
moveNum = 1


# BITMAP: width: 8, height: 8
catMap = bytearray([0,128,190,188,184,168,184,184,184,184,168,184,188,190,128,128,
           0,0,2,6,6,5,5,5,5,5,5,5,5,0,0,0])
           
# BITMAP: width: 16, height: 16
altCatMap = bytearray([255,255,255,255,3,143,223,31,31,223,143,3,255,255,255,255,
           255,255,255,255,254,254,252,252,252,252,254,254,255,255,255,255])

catSprite = thumby.Sprite(16, 16, catMap+altCatMap)
catSprite.x = 29 # Initial placement - middle of screen
catSprite.y = 15

playerSprite = catSprite

class inputManager:
        
    def playerMovement():
        # Up, down, left, right button movement logic
        # When pressing 2 buttons at the same time, diagonal movement is possible
        if thumby.buttonU.pressed():
            playerSprite.y -= moveNum
    
        if thumby.buttonD.pressed():
            playerSprite.y += moveNum
         
        if thumby.buttonL.pressed():
            playerSprite.x -= moveNum
        
        if thumby.buttonR.pressed():
            playerSprite.x += moveNum
        
        if thumby.buttonA.pressed():
            playerSprite.setFrame(0)
        else:
            playerSprite.setFrame(1)
            
        dispMan.renderSprite(playerSprite)