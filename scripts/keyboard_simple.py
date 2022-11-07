# LightDJITelloPy (c) 2022 Diego Contreras
# This code is licensed under MIT license (see LICENSE.txt for details)

"""
    keyboard_simple.py

    Moves a Tello drone via keystrokes. Code is much, much simpler than
    keyboard.py, and only implements safe mode.
"""

# Tell python interpreter to import library from parent folder. 
import os
import sys
sys.path.append(os.path.join(os.getcwd(), ".."))
from lightdjitellopy import Tello

print("Move the drone by pressing W,A,S,D. Press T to takeoff and L to land.")
print("Press Q and E to turn, and J and K to move up or down.")
print("")
print("Press ENTER after typing each command. Only the last command will be")
print("run. For example, \"WSDA\" will only run the last command \"A\"")

tello = Tello()
tello.connect()

HOZ_DIST = 60
VER_DIST = 60
TURN_DIST = 45 # Degrees

while True:
    commands = input("KEY or press 0 to quit: ")
    
    # Don't continue if user didn't send a command
    if len(commands) == 0:
        continue

    command = commands[-1]

    if command == "0":
        break

    if command.upper() == "W":
        tello.move_forward(HOZ_DIST)

    if command.upper() == "A":
        tello.move_left(HOZ_DIST)

    if command.upper() == "S":
        tello.move_back(HOZ_DIST)

    if command.upper() == "D":
        tello.move_right(HOZ_DIST)

    if command.upper() == "E":
        tello.rotate_clockwise(TURN_DIST)

    if command.upper() == "Q":
        tello.rotate_counter_clockwise(TURN_DIST)

    if command.upper() == "J":
        tello.move_up(VER_DIST)

    if command.upper() == "K":
        tello.move_down(VER_DIST)

    if command.upper() == "T":
        tello.takeoff()

    if command.upper() == "L":
        tello.land()


tello.land()
tello.closeSocket()
tello.end()
