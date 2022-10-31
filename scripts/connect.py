import os
import sys
sys.path.append(os.path.join(os.getcwd(), ".."))
from lightdjitellopy import Tello

import time

"""
    Connects Tello and ends the connection. Used for debugging purposes.
"""


tello = Tello()
tello.connect()

tello.closeSocket()
tello.end()
