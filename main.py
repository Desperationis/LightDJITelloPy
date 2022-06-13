from lightdjitellopy import Tello

tello = Tello()
tello.connect()
tello.takeoff()

## DO stuff

tello.land()
