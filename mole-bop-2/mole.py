import time

class Mole ():
    
    def __init__(self):
        self.state = "down"
        # Time when the mole goes down if up
        self.time_expire = 0
        # default to white - advanced levels can use
        # different colours to determine time / points
        self.up_color = (255,255,255)
        # How many points if hit
        self.points = 1
        
    # Pop the mole up - set expire_time
    # If points and color not set then use existing
    def pop_up (self, expire_time, points=None, color=None):
        self.state = "up"
        self.time_expire = expire_time
        if points != None:
            self.points = points
        if color != None:
            self.up_color = color
            
    # checks if needs to go down
    # returns color of LED 
    def update (self, current_time):
        if self.state == "up":
            if time.ticks_diff(current_time, self.time_expire) > 0:
                self.state = "down"
        # If still up
        if self.state == "up":
            return self.up_color
        else :
            return (0,0,0)
        
    # If mole hit - if up then return score, otherwise return 0
    def hit (self):
        if self.state == "up":
            self.pop_down()
            return self.points
        return 0
    
    def pop_down(self):
        self.state = "down"
        
    # If up return up color - otherwise return black
    def get_color(self):
        if self.state == "up":
            return self.up_color
        return (0,0,0)
        
    
        