import thumby
import displaymanager

dispMan = displaymanager.displayManager

# Number of pixels sprite will move - increasing this makes movement choppy 
moveNum = 1

# direction variable that handles overowld player movement
dir = 0;

# Get rid of this soon

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

    # Moves in the direction the character is pointing in
    def moveInDir():
        if (dir == 0):
            playerSprite.y -= moveNum
        elif (dir == 1):
            playerSprite.x += moveNum
        elif (dir == 2):
            playerSprite.y += moveNum
        elif (dir == 3):
            playerSprite.x -= moveNum
        
    # Allows the character to turn left/right
    def shiftDir(someVal):
        
        # increments dir dependent on what was given
        dir += someVal
        
        # If dir is less than 0, the it will turn left
        if (dir < 0):
            dir = 3
        
        # If dir is greater than three, then it will be set to face up
        if (dir > 3):
            dir = 0
    
    # works when in the main game scene
    def playerMovement():
        # Up, down, left, right button movement logic
        # When pressing 2 buttons at the same time, diagonal movement is possible
        if thumby.buttonU.pressed():
            shiftDir()
    
        # Does nothing at the moment, but should lead into the pause menu
        # if thumby.buttonD.pressed():
            
        # tells the shift dir funct that we're turning left
        if thumby.buttonL.pressed():
            shiftDir(1)
        
        # tells the shift dir funct that we're turning right
        if thumby.buttonR.pressed():
            shiftDir(1)
        
        if thumby.buttonA.pressed():
            playerSprite.setFrame(0)
        else:
            playerSprite.setFrame(1)
            
        dispMan.renderSprite(playerSprite)




