from lightdjitellopy import Tello

"""
    Basic template to control the Tello. Simply connect to the Tello's wifi
    (TELLO-XXXX) and run.
"""

tello = Tello()
tello.connect()
tello.takeoff()





# Your code here





tello.land()
tello.closeSocket()
tello.end()
