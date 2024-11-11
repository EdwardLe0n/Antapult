import thumby

class displayManager:
    
    def displaySetUp():
        thumby.display.fill(1) # Fill canvas to white
        
    def renderSprite (someSprite):
        # Display Sprite & Update screen
        thumby.display.drawSprite(someSprite)