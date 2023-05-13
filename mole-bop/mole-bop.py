import time
import random
import picokeypad

keypad = picokeypad.PicoKeypad()
keypad.set_brightness(0.5)
NUM_KEYS = keypad.get_num_pads()

lit_button = random.randint(0, NUM_KEYS - 1)
lit_time = time.ticks_ms()
lit_duration = 1000

score = 0
lives = 3

def all_off():
    for i in range (0, NUM_KEYS):
        keypad.illuminate(i, 0,0,0)

while True:
    # Check to see if the time has expired
    now_time = time.ticks_ms()
    if (time.ticks_diff (now_time, lit_time) > lit_duration):
        # light it red for missed
        keypad.illuminate(lit_button, 255, 0, 0)
        keypad.update()
        time.sleep (1)
        lives -= 1
        if (lives <=0):
            break
        # make the next one a little easier by adding 400ms
        lit_duration += 500
        # choose new button
        lit_button = random.randint(0, NUM_KEYS - 1)
        lit_time = time.ticks_ms()
        
    # Turn LEDs off and the lit one on
    all_off()
    keypad.illuminate(lit_button, 255, 255, 255)
    keypad.update()
    
    # scan keys to see if the lit_button key is pressed
    button_states = keypad.get_button_states()
    for i in range (0, NUM_KEYS):
        if i == lit_button and button_states & 0x01 > 0:
            score += 1
            lit_duration -= 30
            lit_button = random.randint(0, NUM_KEYS - 1)
            lit_time = time.ticks_ms()
        button_states = button_states >> 1
        
print ("Score {}".format(score))
all_off()
if (score > 64):
    score = 64
for i in range (0, score / 4): 
    keypad.illuminate(i, 0, 255, 0)
keypad.update()

    
