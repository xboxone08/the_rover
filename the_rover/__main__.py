#! /usr/bin/env python3
from gpiozero import Robot
from gpiozero.pins.pigpio import PiGPIOFactory
from keyboard import on_release_key, is_pressed
from fabric import Connection

"""Setup
System running the code
This code can be run from any OS, but must connect to a (or multiple) Raspberry Pi "rover(s)".

The system running the code must have gpiozero, pigpio, keyboard, and fabric installed (Automatically installed using the last four commands for installation).

Raspberry Pi "Rover"
The code expects pins 19 and 26 to control your front left motor, 16 and 20 your front right, 27 and 22 your back left, and 23 and 24 you back right (BCM numbering). The pins to which these numbers correspond to on your Pi can be found by running the pinout command in Bash or at pinout.xyz.

The code makes use of Remote GPIO to control the rover Pi, so it must have the "Remote GPIO" interface enabled in sudo raspi-config/Raspberry Pi Configuration/config.txt, have the pigpio Python module installed (pip3 install pigpio), and must systemctl enable pigpiod or alternatively use cron (sudo crontab -e) to run pigpiod at startup (@reboot) (Doesn't requires enabling Remote GPIO. Useful for allowing only specific IPs/hostnames using the -n flag. See the Remote GPIO documentation for more details.)

The code uses raspistill, so the "Camera" interface must be enabled in sudo raspi-config/Raspberry Pi Configuration/config.txt, and a PiCamera must be connected (Instructions here).

Usage
Running
Once in the directory you cloned the repository to, you can run the code by either using python(3) the_rover/(__main__.py) unless you used the last two methods of installation.

Or, if you installed it using any of the last three installation commands, (python(3) -m )the_rover from anywhere.

Note: Due to its dependency on the keyboard module, the code must be run with sudo on most Linux systems.

Once running
Press n to switch to next rover (wraps around).
Press p to switch to previous rover (wraps around).
Press c to capture a picture with the picamera (and download it to the current working directory).
WASD for controlling rover. (Only one control at a time.)
Note: All parenthesized parts of commands are optional/only needed in specific scenarios
"""

ips: list[str] = []

# Get rover IPv4 addresses from user
while True:
    ip: str = input("Enter a rover's IPv4 address or leave blank if you're done. ")
    try:
        # Verify IPv4 address to be valid
        if ip != "":
            if ip.count(".") != 3:
                raise ValueError
            if len(ip) > 15:
                raise ValueError
            for i in range(len(ip)):
                if ip[i] != "0" and ip[i] != "1" and ip[i] != "2" and ip[i] != "3" and ip[i] != "4" and ip[i] != "5" and ip[i] != "6" and ip[i] != "7" and ip[i] != "8" and ip[i] != "9" and ip[i] != ".":
                    raise ValueError
            ips.append(ip)
        else:
            if len(ips) < 1:
                print("You must give at least on rover IP.")
            else:
                break
    except ValueError:
        print("Invalid IPv4 address:", ip)

# Initialize rovers using the IPs

factories: list[PiGPIOFactory] = []
sshs: list[Connection] = []
for ip in ips:
    factories.append(PiGPIOFactory(host=ip))
    sshs.append(Connection(ip, "pi", 22))

rovers: list[tuple[Robot, Robot]] = []
for factory in factories:
    rovers.append((Robot((19, 26), (16, 20)), Robot((27, 22), (23, 24))))

x: int = 0
rover: tuple[Robot, Robot] = rovers[x]

# Hotkeys


def next_rover(_=None):
    global x
    x = 0 if x >= len(rovers) - 1 else x + 1
    print("Switched to rover", rovers.index(rover) +
          ".", f"(IP: {ip[rovers.index(rover)]})")


def previous_rover(_=None):
    global x
    x = len(rovers) - 1 if x < 0 else x - 1
    print("Switched to rover", rovers.index(rover) +
          ".", f"(IP: {ip[rovers.index(rover)]})")


def capture(_=None):
    sshs[x].run("rm img.jpg")
    sshs[x].run("raspistill -o img.jpg")
    sshs[x].get("img.jpg", preserve_mode=False)


on_release_key("n", next_rover)
on_release_key("p", previous_rover)
on_release_key("c", capture)

while True:
    rover = rovers[x]
    if is_pressed("w"):
        print("Forward")
        rover[0].forward()
        rover[1].forward()
    elif is_pressed("s"):
        print("Backward")
        rover[1].backward()
        rover[0].backward()
    elif is_pressed("a"):
        print("Left")
        rover[0].left()
        rover[1].left()
    elif is_pressed("d"):
        print("Right")
        rover[0].right()
        rover[1].right()
    else:
        print("Stop")
        rover[1].stop()
        rover[0].stop()
