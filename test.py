from lightdjitellopy import *

swarm = TelloSwarm.fromIps([
    "192.168.10.1",
])

swarm.connect()

swarm.takeoff()
swarm.sync()
swarm.land()

swarm.end()

