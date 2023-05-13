# Mole Bop
Bop the moles. A game using a Raspberry Pi Pico and the Pimoroni Pico RGB Keypad, where you get to bop the moles as they light up on a keypad.

## Introduction

This is a game created for a tutorial based around the Pimoroni Pico RGB Keypad.

There are 3 folders.
* demo-port-expander - Demonstration code for a MCP23008 port expander
* mole-bop - Basic Whac-A-Mole game used in the tutorial
* mole-bop-2 - Improved game with improved difficulty, different levels and multiple moles

## Game Installation 

The game needs to be installed on a Pico connected to a Pimoroni Pico RGB Keypad. The simplist way to install MicroPython and the appropriate drivers is to the use the appropriate uf2 image from: [Github Pimoroni Pico Images](https://github.com/pimoroni/pimoroni-pico/releases/latest/) 

For Mole Bop - upload the file from the directory mole-bop to the Pico and launch it from Thonny. Note that this version needs a restart for subsequent games.

For Mole Bop 2 - upload all the files from the directory mole-bop-2. This can be done using the upload option in Thonny. To have the game start automatically save the file mole-bop2.py as main.py on the Pico.

The rest of the explanations relate to the Mole Bop game.

## Playing the game

* Press any key to start the game

* Initially one button will light up. Pressing that button in time will score a point.

* Keep pressing the buttons that light up scoring additional points.

* After a period of time the level will end. If you have scored sufficient points then it will briefly flash pale blue and advance to the next level.

* Higher levels increase the number of moles and reduces the time they are visible for.

* If you don't score enough for a level then the game will end.

* The score will be shown by lighting the buttons green. Each button represents up to 20 points.

* Press any key to restart the game

