import thumby
import displaymanager

dispMan = displaymanager.displayManager

class inputManager:
    
    def __init__(self):
        self.moveNum = 0
        self.direction = 0
        
        # Number of pixels sprite will move - increasing this makes movement choppy 
        self.moveNum = 1

        # direction variable that handles overowld player movement
        self.direction = 0

        # Get rid of this soon

        # BITMAP: width: 8, height: 8
        self.catMap = bytearray([0,128,190,188,184,168,184,184,184,184,168,184,188,190,128,128,
           0,0,2,6,6,5,5,5,5,5,5,5,5,0,0,0])
           
        # BITMAP: width: 16, height: 16
        self.altCatMap = bytearray([255,255,255,255,3,143,223,31,31,223,143,3,255,255,255,255,
               255,255,255,255,254,254,252,252,252,252,254,254,255,255,255,255])

        self.catSprite = thumby.Sprite(16, 16, self.catMap+self.altCatMap)
        self.catSprite.x = 29 # Initial placement - middle of screen
        self.catSprite.y = 15

        self.playerSprite = self.catSprite

    # Moves in the direction the character is pointing in
    def moveInDir(self):
        if (direction == 0):
            self.y -= self.moveNum
        elif (direction == 1):
            self.playerSprite.x += self.moveNum
        elif (ddirectionir == 2):
            self.playerSprite.y += self.moveNum
        elif (direction == 3):
            self.playerSprite.x -= self.moveNum
        
    # Allows the character to turn left/right
    def shiftDir(someVal):
        
        # increments dir dependent on what was given
        self.direction += self.someVal
        
        # If dir is less than 0, the it will turn left
        if (self.direction < 0):
            self.direction = 3
        
        # If dir is greater than three, then it will be set to face up
        if (self.direction > 3):
            self.direction = 0
    
    # works when in the main game scene
    def playerMovement(self):
        # Up, down, left, right button movement logic
        # When pressing 2 buttons at the same time, diagonal movement is possible
        if thumby.buttonU.pressed():
            self.moveInDir(self)
    
        # Does nothing at the moment, but should lead into the pause menu
        # if thumby.buttonD.pressed():
            
        # tells the shift dir funct that we're turning left
        if thumby.buttonL.pressed():
            self.shiftDir(1)
        
        # tells the shift dir funct that we're turning right
        if thumby.buttonR.pressed():
            self.shiftDir(1)
        
        if thumby.buttonA.pressed():
            self.playerSprite.setFrame(0)
        else:
            self.playerSprite.setFrame(1)
            
        dispMan.renderSprite(playerSprite)