# A labour of moles
import time
import picokeypad
from mole import Mole


class Labour ():
    
    def __init__(self):
        self.keypad = picokeypad.PicoKeypad()
        self.keypad.set_brightness(0.5)
        self.num_moles = self.keypad.get_num_pads()
        self.moles = []
        for i in range (0, self.num_moles):
            self.moles.append(Mole())
            
    def all_off(self):
        for mole in self.moles:
            mole.pop_down()
    
    def pop_up_mole (self, mole, duration):
        current_time = time.ticks_ms()
        expire_time = current_time + duration
        self.moles[mole].pop_up(expire_time)
        
    def num_up(self):
        num_moles_up = 0
        for mole in self.moles:
            if mole.state == "up":
                num_moles_up += 1
        return num_moles_up
        
    # Handles key presses
    # calls update against all moles
    # and sets LEDs as appropriate
    def update(self):
        current_time = time.ticks_ms()
        new_points = 0
        button_states = self.keypad.get_button_states()
        for i in range (0, self.num_moles):
            if button_states & 0x01 > 0:
                add_points = self.moles[i].hit()
                new_points += add_points
                # short delay if incorrect mole hit
                # prevent pressing all keys
                # if single key then negligable if multiple
                # then more of an impact
                if (add_points == 0):
                    time.sleep(0.2)
            else:
                # Update checks if time expired
                # Only needed if wasn't hit
                self.moles[i].update(current_time)
            mole_color = self.moles[i].get_color()
            self.keypad.illuminate(i, *mole_color)
            # shift button states - so that next button is checked
            button_states = button_states >> 1
        self.keypad.update()
        return new_points
    
    
    ########## Special methods related to start game / game over
    # Included here so that all keypad interactions are in one class
    def press_any_key(self):
        while True:
            # Loops waiting for any key to be pressed
            button_states = self.keypad.get_button_states()
            if (button_states > 0):
                break
            
    def light_all(self, color):
        for i in range (0, self.num_moles):
            self.keypad.illuminate(i, *color)
            self.keypad.update()
            
    def light_button (self, button_num, color):
        self.keypad.illuminate(button_num, *color)