# LightDJITelloPy
This is a branch of the original [DJITelloPy](https://github.com/damiafuentes/DJITelloPy) meant to work on very lightweight devices such as an Android phone, Chromebook, or Raspberry Pi without using AV, NumPy, or Pillow for image processing. Essentially, it has no "fluff" and is now essentially just a UDP client for the Tello SDK. Currently, it has only been tested with Python3 apps on the Chromebook and Android devices. 

This branch is mainly intended for educational use with the Tello EDU drone, as some devices (such as the chromebook) are restricted from running linux and must resort to a very underwhelming IDE. 

Just like the original branch, this works with the  official [Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/tello/20180910/Tello%20SDK%20Documentation%20EN_1.3.pdf) and [Tello EDU SDK](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf) and obviously removes the video features. Other than that, this library can:

- Receive and parse state packets
- Send multiple commands to the drone
- Control a swarm of drones
- Work with Python 3.6 or higher. 
- Work with virtually any IoT device that can run Python3. 

Feel free to contribute!

## Usage
### API Reference
See ![documentation.pdf](documentation.pdf) for my custom documentation as the original one was simply "look at the source code". 

### Simple example
```Python

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_left(100)
tello.rotate_counter_clockwise(90)
tello.move_forward(100)

tello.land()
```

### Notes
- Mission pad detection and navigation is only supported by the Tello EDU.
- Bright environment is necessary for successful use of mission pads.
- Connecting to an existing wifi network is only supported by the Tello EDU.

## Authors of OG branch

* **Damià Fuentes Escoté**
* **Jakob Löw**
* [and more](https://github.com/damiafuentes/DJITelloPy/graphs/contributors)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details
