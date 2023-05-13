# Improved version for Pico Mole Bop
# Works with Pimoroni Pico RGB Keypad
# Based on levels - you have a fixed length of time to score points
# Get enough points within time to move to the next level
# At the end the buttons show the score with 20 points for each button

import time
import random
from labour import Labour
from levels import Levels

moles = Labour()
levels = Levels()

# Outer loop - runs once per game
while True:
    # In game loop - runs until game over
    # Set / Reset game values
    score = 0
    level_score = 0
    level = 0
    level_end_time = time.ticks_add (time.ticks_ms(), levels.get_level_duration(level))
    
    # Wait until a key is pressed
    moles.press_any_key()
    
    while True:
        current_time = time.ticks_ms()
        
        # Is this the end of this level
        if time.ticks_diff(level_end_time, current_time) < 0:
            # Scored enough to move to the next level
            if (level_score >= levels.get_num_points(level)):
                # briefly flash lights and then continue
                moles.light_all((0,255,255))
                time.sleep (0.3)
                level += 1
                level_end_time = time.ticks_add (time.ticks_ms(), levels.get_level_duration(level))
                level_score = 0
            # Otherwise game over
            else:
                break
        
        
        # How many moles are up, perhaps add more
        if (moles.num_up() < levels.get_num_moles(level)):
            # Possible that a mole will get chosen which is already up
            # in which case it gets ignored and another attempt made next time
            new_mole = random.randrange(0, moles.num_moles)
            moles.pop_up_mole(new_mole, levels.get_mole_duration(level))

        score_update = moles.update()
        if score_update > 0:
            score += score_update
            level_score += score_update
        
        
    print ("Score {}".format(score))
    # Show score - each button is worth 20 points 
    if (score > 320):
        score = 320
    for i in range (0, moles.num_moles):
        if (score / 20 > i):
            moles.light_button(i, (0, 255, 0))
        else:
            moles.light_button(i, (0, 0, 0))
    moles.keypad.update()
    # delay to give time to see score
    time.sleep(1)
    # Wait until a key is pressed
    moles.press_any_key()

    
