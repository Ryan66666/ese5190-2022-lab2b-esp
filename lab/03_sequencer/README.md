### TODO:

Create a 'sequencer' that allows you to record BOOT button presses and play them on the Neopixel, and also play a sequence of read/write commands. You should be able to:
- record at a least a few seconds of button input to your RP2040 (in RAM)
- replay a recorded sequence on your NeoPixel
- loop a recording
- save a recording to your laptop (the Python Serial library is one way to do this)
- play a recording from your laptop
- record 'macros' (a sequence of console commands) based on keystrokes in your serial console
- hand-edit a list of register read/write commands on your laptop, and play them on the RP2040
- include multiple I/O sources in a recording, and remap among the following:
    - inputs: BOOT button, console commands, register read/write commands
    - outputs: neopixel color, neopixel brightness, data over serial, register read/write commands


#### Worked with Katrina Ji & Yuchen Wang

## record reading data from BOOT pin

![202268733-38efb52a-c3af-4d6f-ab77-3d794cb96c40](https://user-images.githubusercontent.com/114255407/202771136-b7477bae-6b32-40d6-819e-8e443a524099.gif)

The Python code will read the output from tty termial and record the status of BOOT PIN with sequencer.txt file on your computer.

## re-displaing the data via WS2812 LED

![202269079-c60ff665-0ff7-453c-b378-5822bd2fcb5f](https://user-images.githubusercontent.com/114255407/202771354-ad162cc7-43ef-4433-b348-74d8f79a14fc.gif)

## recording data in txt file

<img width="794" alt="202269338-4ad18a11-5259-47e8-9877-c0a61c3036d4" src="https://user-images.githubusercontent.com/114255407/202771421-23cf9703-f74d-412e-b2e3-792f832f420e.png">

## Switch Mode

It is easier to switch mode with python code.

- r (lowercase) -> read from BOOT PIN and recored the raw data to sequencer.txt file

- w (lowercase) -> write the data stored in sequencer.txt to QTPY-2040

## Explain

In this part, the python code will communicate with QTPY 2040 via tty terminal. First, in read mode, the Python code will sent a 'r' to qtpy 2040 indicates starting to read the BOOT PIN status(1 or 0) for specific duration, such as 5 sec,and stored the data into a txt file. Then reboot the python code, microcontroller and input 'w', the python also write a 'w' to 2040 and it will return "OK" to python, then allow the python to write the data into WS2812.

