from lightdjitellopy import Tello

tello = Tello(host="192.168.47.1")
tello.connect()
tello.takeoff()





# Your code here





tello.land()
tello.closeSocket()
tello.end()
