from lightdjitellopy import Tello
import time

tello = Tello()
tello.connect(True)

tello.closeSocket()
tello.end()
