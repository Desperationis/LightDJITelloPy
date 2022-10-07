from lightdjitellopy import Tello
from lightdjitellopy import TelloSwarm

"""
    Commands a group of Tello's to flip at the same time. Tello's must be
    connected to the same wifi network, 2.4 GHz, with a password and a SSID
    with no spaces.
"""


swarm = TelloSwarm.fromIps([
    "192.168.198.1",
    "192.168.198.91",
    "192.168.198.147",
    "192.168.198.202",
    ])

swarm.connect()
swarm.takeoff()

# Your code here
swarm.flip_forward()

swarm.land()
swarm.closeSocket()
swarm.end()
