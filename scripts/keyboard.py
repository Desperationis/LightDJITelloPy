# LightDJITelloPy (c) 2022 Diego Contreras
# This code is licensed under MIT license (see LICENSE.txt for details)

"""
    keyboard.py

    Moves a Tello drone via keystrokes. 
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
print("")
print("SAFE mode moves the drone just a little bit for every command, and halts")
print("until the drone finishes each command. MANUAL mode sets the velocity of")
print("the drone instantly, meaning you have to manually press buttons to")
print("\"brake\" the drone.")
print("")

VALID_COMMANDS="WASDTLQEQJK "

choice = input("Safe mode [S] or Manual mode [M]? ")
mode = "safe"
if choice.lower() == "m":
    mode = "manual"

print("Controlling via %s mode." % mode)

class BaseDrone:
    def __init__(self):
        self.tello = Tello()
        self.tello.connect()

    def takeoff(self):
        self.tello.takeoff()

    def land(self):
        self.tello.land()

    def end(self):
        self.tello.closeSocket()
        self.tello.end()

class SafeDrone(BaseDrone):
    def __init__(self, hozDist, verDist, turnDist):
        """
        @param hozDist Horizontal distance to travel for every command, in
        centimeters.

        @param verDist Vertical distance to travel for every command, in
        centimeters.

        @param turnDist Angle to turn for every command, in degrees.
        """

        super().__init__()

        self.hozDist = hozDist
        self.verDist = verDist
        self.turnDist = turnDist

    def forward(self):
        self.tello.move_forward(self.hozDist)

    def backward(self):
        self.tello.move_back(self.hozDist)
        
    def right(self):
        self.tello.move_right(self.hozDist)
        
    def left(self):
        self.tello.move_left(self.hozDist)

    def up(self):
        self.tello.move_up(self.verDist)

    def down(self):
        self.tello.move_down(self.verDist)

    def clockwise(self):
        self.tello.rotate_clockwise(self.turnDist)

    def counter_clockwise(self):
        self.tello.rotate_counter_clockwise(self.turnDist)

class ManualDrone(BaseDrone):
    def __init__(self, hozSpeed, verSpeed, turnSpeed):
        super().__init__()

        self.hozSpeed = hozSpeed
        self.verSpeed = verSpeed
        self.turnSpeed = turnSpeed

    def forward(self):
        self.tello.send_rc_control(0, self.hozSpeed, 0, 0)

    def backward(self):
        self.tello.send_rc_control(0, -self.hozSpeed, 0, 0)

    def right(self):
        self.tello.send_rc_control(self.hozSpeed, 0, 0, 0)

    def left(self):
        self.tello.send_rc_control(-self.hozSpeed, 0, 0, 0)

    def up(self):
        self.tello.send_rc_control(0, 0, self.verSpeed, 0)

    def down(self):
        self.tello.send_rc_control(0, 0, -self.verSpeed, 0)

    def clockwise(self):
        self.tello.send_rc_control(0, 0, 0, self.turnSpeed)

    def counter_clockwise(self):
        self.tello.send_rc_control(0, 0, 0, -self.turnSpeed)

    def stop(self):
        self.tello.send_rc_control(0, 0, 0, 0)


drone = None
if mode == "manual":
    input("WARNING: The drone will continue moving in manual mode. Press SPACE to stop the drone. Press ENTER if you have read this message.")
    drone = ManualDrone(60, 60, 20)

else:
    drone = SafeDrone(60, 60, 45)

while True:
    commands = input("KEY or press 0 to quit: ")
    
    # Don't continue if user didn't send a command
    if len(commands) == 0:
        continue

    command = commands[-1]

    if command.upper() not in VALID_COMMANDS:
        print(command + " is not a valid command")
        continue

    if command == "0":
        break

    if command == " " and mode == "manual":
        drone.stop()

    if command.upper() == "W":
        drone.forward()

    if command.upper() == "A":
        drone.left()

    if command.upper() == "S":
        drone.backward()

    if command.upper() == "D":
        drone.right()

    if command.upper() == "E":
        drone.clockwise()

    if command.upper() == "Q":
        drone.counter_clockwise()

    if command.upper() == "J":
        drone.up()

    if command.upper() == "K":
        drone.down()


    if command.upper() == "T":
        drone.takeoff()

    if command.upper() == "L":
        drone.land()


drone.land()
drone.end()
