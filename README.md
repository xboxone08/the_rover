# the_rover
THE rover. Allows controlling Raspberry Pi "rovers" remotely and interactively from any OS's command line.
## Installation
There are five methods:
- Clone the repository and manually install the [requirements](requirements.txt).

- Clone the repository and run `pip(3) install -r requirements.txt` to install the requirements to the active Python installation.

- Clone the repository and run `pip(3) install .` in the directory you cloned it into to do the same thing and allow running with `(python(3) -m )the_rover` in your terminal.

- Don't clone the repository. Just download the .whl file in the latest release and `pip install` it.

- Don't clone the repository. Just `pip install the_rover` to install from PyPi.

## Setup
### System running the code
- This code can be run from any OS, but must connect to a (or multiple) Raspberry Pi "rover(s)".

- The system running the code must have `gpiozero`, `pigpio`, `keyboard`, and `fabric` installed (Automatically installed using the last four commands for installation).

### Raspberry Pi "Rover"
- The code expects pins 19 and 26 to control your front left motor, 16 and 20 your front right, 27 and 22 your back left, and 23 and 24 you back right (BCM numbering). The pins to which these numbers correspond to on your Pi can be found by running the `pinout` command in Bash or at [pinout.xyz](pinout.xyz).

- The code makes use of Remote GPIO to control the rover Pi, so it must have the "Remote GPIO" interface enabled in `sudo raspi-config`/Raspberry Pi Configuration/config.txt, have the `pigpio` Python module installed (`pip3 install pigpio`), and must `systemctl enable pigpiod` or alternatively use cron (`sudo crontab -e`) to run `pigpiod` at startup (`@reboot`) (Doesn't requires enabling Remote GPIO. Useful for allowing only specific IPs/hostnames using the `-n` flag. See the [Remote GPIO documentation](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html#command-line-pigpiod) for more details.)

- The code uses `raspistill`, so the "Camera" interface must be enabled in `sudo raspi-config`/Raspberry Pi Configuration/config.txt, and a PiCamera must be connected (Instructions [here](https://picamera.readthedocs.io/en/release-1.13/quickstart.html)).

- The code uses SSH and SFTP, so the "SSH" interface must be enabled.

## Usage
### Running
Once in the directory you cloned the repository to, you can run the code by either using `python(3) the_rover(/__main__.py)` unless you used the last two methods of installation.

Or, if you installed it using any of the last three installation commands, `(python(3) -m )the_rover` from anywhere.

Note: Due to its dependency on the `keyboard` module, the code must be run with `sudo` on most Linux systems.

### Once running
- Press <kbd>n</kbd> to switch to next rover (wraps around).
- Press <kbd>p</kbd> to switch to previous rover (wraps around).
- Press <kbd>c</kbd> to capture a picture with the picamera (and download it to the current working directory).
- WASD for controlling rover. (Only one control at a time.)

###### Note: All parenthesized parts of commands are optional/only needed in specific scenarios
