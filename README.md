# Volumio_caddy
Python scripts for buttons, rotary encoders and oled screen for Volumio on Raspberry Pi (including longpress actions that work)
## Dependencies
To have my code working, you need to install those Python libraries. They are all available through "pip install".

- SocketIO-client-2
- PIL
- Adafruit_SSD1306
- RPi.GPIO
## Fonts
For the script to work, you must put those fonts in the same directory as the scripts : (be sure to download the .ttf version)
- Proggy Clean https://proggyfonts.net/download/ (1st one in the list)
- Inky Thin Pixels http://www.fontspace.com/chequered-ink/inky-thin-pixels
- Volumio OLED (included in this directory)
## Software Install
To install my script, makes sure all the above libraries are installed to your system. 

Make sure you have JPEG and Freetype support libraries installed:
        
    sudo apt-get install -y python-dev libjpeg9-dev libfreetype6-dev swig

If you system has problems finding packages, it's a good idea to run:

    sudo apt-get update
        
But, please never run apt-get upgrade as it will break your volumio install.


It's time to clone this directory, running :

    git clone https://github.com/julien123123/volumio_caddy
  	cd volumio-buddy

The scripts will be install in your "/" directory

## Hardware install
Now that the scripts are copied on your Pi.
open cady.py running :

    sudo nano caddy.py
    
The pin numbers and the commands are assigned at the beginig of the code, please change them acording to your own wiring, you can also change the commands assigned to each button. 

By default:

- GPIO 22 is a button assigned to the play/pause on short press and shutdown on longpress
- GPIO 27 is a button assigned to next
- GPIO 17 is a button assigned to previous
- GPIO 25 is a Rotary encoder button asssigned to random on short press and mute on longpress
- GPIO 23 and 24 are the rotary encoder pins controlling the volume
All of which are connected to ground with software pull-up resistors

The Oled screen is using the I2c interface and it uses:
- Pin 1 (3.3v)
- Pin 3 (GPIO 2, SDA)
- Pin 5 (GPIO 3, SCL)
- Pin 9 (GND)
pin 26 is used as its reset, but you can change it in Caddy.py if you want

## Make it start with the PI

I worked on the script so that it can easily made as a servicectl. In the service file make sure you make the service restart upon failiure. Additionaly, if you want to be able to start your pi when it is shut without having to unplug it, the only way I know is to add a reset button. 
