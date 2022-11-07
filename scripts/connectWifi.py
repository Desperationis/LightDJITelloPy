from lightdjitellopy import Tello
import sys

"""
    Connects a drone to a router. Drone will reboot after this script is done
    and will connect to the router. If the drone doesn't connect, or you
    mistyped the SSID or PASSWORD, hold the power button of the drone for 10
    seconds while it is on to reset to factory settings.

    The wifi to connect to must be 2.4 GHz, have a valid password, and must
    have no spaces in its SSID.
"""

SSID = "ssid"
PASSWORD = "password"

print("Connecting to %s" % SSID)

tello = Tello()
tello.connect()

tello.connect_to_wifi(SSID, PASSWORD)

tello.closeSocket()
tello.end()
