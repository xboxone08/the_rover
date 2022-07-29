from gpiozero import Robot
from gpiozero.pins.pigpio import PiGPIOFactory
from keyboard import on_release_key, is_pressed

"""Run with sudo"""

ips = []

# Get rover IPv4 addresses from user
while True:
    ip = input("Enter a rover's IPv4 address or leave blank if you're done.")
    try:
        # Verify IPv4 address to be valid
        if ip != "":
            if ip.count(".") != 3:
                raise ValueError
            if len(ip) > 15:
                raise ValueError
            for i in range(len(ip)):
                if ip != "0" and ip != "1" and ip != "2" and ip != "3" and ip != "4" and ip != "5" and ip != "6" and ip != "7" and ip != "8" and ip != "9" and ip != ".":
                    raise ValueError
            ips.append(ip)
        else:
            if len(ips) < 1:
                print("You must give at least on rover IP.")
            else:
                break
    except ValueError:
        print("Invalid IPv4 address:", ip)

factories = []
for ip in ips:
    factories.append(PiGPIOFactory(host=ip))

rovers = []
for factory in factories:
    rovers.append((Robot((19, 26), (16, 20)), Robot((27, 22), (23, 24))))

x = 0

rover = rovers[x]


def next_rover(_=None):
    x = 0 if x >= len(rovers) - 1 else x + 1  # Epic one-liner


on_release_key("n", next_rover)

while True:
    if is_pressed("w"):
        rover[0].forward()
        rover[1].forward()
    elif is_pressed("s"):
        rover[1].backward()
        rover[0].backward()
    elif is_pressed("a"):
        rover[0].left()
        rover[1].left()
    elif is_pressed("d"):
        rover[0].right()
        rover[1].right()
    else:
        rover[1].stop()
        rover[0].stop()
