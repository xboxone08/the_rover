# the_rover
THE rover.
## Installation
There are three methods:
- Clone the repository and manually install requirements.

- Clone the repository and run `pip install -r requirements.txt` to install the requirements to the active Python installation.

- Clone the repository and run `pip install .` in the directory you cloned it into to do the same thing and allow running with `rover` in your terminal.

## Setup
### System running the code
- This code can be run from any OS, but must connect to a (or multiple) Raspberry Pi "rover(s)".

- The system running the code must have `gpiozero`, `pigpio`, and `keyboard` installed (Automatically installed using the latter two commands for installation).

### Raspberry Pi "Rover"
- The code expects pins 19 and 26 to control your front left motor, 16 and 20 your front right, 27 and 22 your back left, and 23 and 24 you back right (BCM numbering). The pins to which these numbers correspond to on your Pi can be found by running the `pinout` command in Bash.

- The code makes use of Remote GPIO to control the rover Pi, so it must have Remote GPIO enabled in `sudo raspi-config`/Raspberry Pi Configuration, have the `pigpio` Python module installed (`pip3 install pigpio`), and must `systemctl enable pigpiod` or alternatively use `cron` to run `pigpiod` at startup.

## Usage
### Running
Once in the directory you cloned the repository to, you can run the code by either using:
- `python3 rover/__main__.py` on Mac/Linux or `python rover\__main__.py` on Windows.
- `python3 -m rover` on Mac/Linux or `python -m rover` on Windows.
Or, if you installed it using `pip install .`, simply run `rover` from anywhere.
Note: Due to its dependency on the `keyboard` module, the code must be run with `sudo` on most Linux systems.

### Once running
- Press "n" to cycle through rovers if using multiple.
- WASD for controlling rover.
