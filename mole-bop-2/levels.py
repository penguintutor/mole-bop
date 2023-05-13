class Levels ():
    # Lists must be same length
    # Num moles is maximum to pop_up at one time
    num_moles = [1,1,2,2,3,3,4,4,5,5]
    num_points = [5,10,15,20,25,30,35,40,45,50]
    mole_duration = [2000,1900,1800,17000,16000,15000,14000,13000,12000,11000]
    level_duration = [10000,10000,10000,10000,10000,10000,10000,10000,10000,10000]
    
    def __init__(self):
        self.num_levels = len(Levels.num_moles)
       
    # Safe methods which safely cope with too short a list
    def get_num_moles (self, level_num):
        if len(Levels.num_moles) > level_num:
            return Levels.num_moles[level_num]
        else:
            return Levels.num_moles[len(Levels.num_moles)-1]
        
    def get_num_points (self, level_num):
        if len(Levels.num_points) > level_num:
            return Levels.num_points[level_num]
        else:
            return Levels.num_points[len(Levels.num_points)-1]
    
    def get_level_duration (self, level_num):
        if len(Levels.level_duration) > level_num:
            return Levels.level_duration[level_num]
        else:
            return Levels.level_duration[len(Levels.level_duration)-1]
        
    def get_mole_duration (self, level_num):
        if len(Levels.mole_duration) > level_num:
            return Levels.mole_duration[level_num]
        else:
            return Levels.mole_duration[len(Levels.mole_duration)-1]