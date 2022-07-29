# the_rover
THE rover.
## Setup
### System running the code
- This code can be run from any OS, but must connect to a (or multiple) Raspberry Pi "rover(s)".

- The system running the code must have `gpiozero` and `keyboard` installed
### Raspberry Pi "Rover"
- The code expects pins 19 and 26 to control your front left motor, 16 and 20 your front right, 27 and 22 your back left, and 23 and 24 you back right (BCM numbering). The pins to which these numbers correspond to on your Pi can be found by running the `pinout` command in Bash.

- The code makes use of Remote GPIO to control the rover Pi, so it must have Remote GPIO enabled in `sudo raspi-config`/Raspberry Pi Configuration, have the `pigpio` Python module installed (`pip3 install pigpio`), and must `systemctl enable pigpiod` or alternatively use `cron` to run `pigpiod` at startup.
## Usage
- Due to its dependency on the `keyboard` module, the code must be run with `sudo` on Linux systems.
- Press "n" to cycle through rovers if using multiple.
- WASD for controlling rover.
