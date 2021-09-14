# Morse
Some Python Morse code projects for the BBC micro:bit. 

Based on https://microbit-micropython.readthedocs.io/en/latest/tutorials/network.html

## Wired Morse

Connect two micro:bits together and send Morse code messages over wires, like a Victorian.

You'll need:
- 2 BBC micro:bits
- 3 crocodile clip leads
- at least 1 USB lead for flashing the code
- a computer
- battery pack or USB lead for powering the second micro:bit

Plug your micro:bits in to the computer in turn and copy the `Morse TX_RX wired.hex` file to the MICROBIT drive. You can also open this file or the `Morse TX_RX wired.py` file in a Python editor like https://python.microbit.org/ and flash the code that way.

Connect the GND pins together and connect pin 1 to pin 2 on the other micro:bit, and pin 2 to pin 1 on the other.

Press button A to send a dot, press B to send a dash. If you connect headphones or have a V2 micro:bit you'll hear the beeps.

Leave a gap between sending letters to make sure it works ok, and it's worth practising in sight of the receiver to get a feel for how long to leave between dots and dashes within a letter and how long to leave between letters.

The receiver flashes up letters as they arrive, and compiles a message. Shake to scroll the message on the LED display and clear the message.

Try making some really long wires to connect your micro:bits - how long can you go? What sorts of problems do you think pioneers of the electric telegraph would have encountered?

## Wireless Morse

Send messages in Morse by wireless like an Edwardian!

You'll need:
- 2 BBC micro:bits
- 3 crocodile clip leads
- at least 1 USB lead for flashing the code
- a computer
- battery pack or USB lead for powering the second micro:bit

Plug your micro:bits in to the computer in turn and copy the `Wireless_Morse.hex` file to the MICROBIT drive. You can also open this file or the `Wireless_Morse.py` file in a Python editor like https://python.microbit.org/ and flash the code that way.

This works very much like the wired project. Press button A to to send a dot, B to send a dash. It sounds on the sender. 

Letters flash up as they are received. Shake to read the whole message and clear it.

How far apart can you go and still send messages? What sorts of problems do you think people had sending messages this way?


