from gpiozero import Robot
from gpiozero.pins.pigpio import PiGPIOFactory
from keyboard import on_release_key, is_pressed

"""Run with sudo"""

ips = []

# Get rover IPv4 addresses from user
while True:
    ip = input("Enter a rover's IPv4 address or leave blank if you're done. ")
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

factories = []
for ip in ips:
    factories.append(PiGPIOFactory(host=ip))

rovers = []
for factory in factories:
    rovers.append((Robot((19, 26), (16, 20)), Robot((27, 22), (23, 24))))

x = 0

rover = rovers[x]


def next_rover(_=None):
    x = 0 if x >= len(rovers) - 1 else x + 1
    print("Switched to rover", rovers.index(rover) + ".", f"(IP: {ip[rovers.index(rover)]})")


on_release_key("n", next_rover)

while True:
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
