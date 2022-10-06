from lightdjitellopy import Tello

tello = Tello()
tello.connect(True)
tello.takeoff()

# Your code here


tello.closeSocket()
tello.end()
