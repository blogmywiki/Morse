# Wired Morse code transmitter / receiver
# Connect 2 micro:bits together with 3 crocodile clip leads
# Pin 1 to pin 2 on the other micro:bit and vice versa, GND to GND 
# Press A for dot, press B for dash
# based on http://microbit-micropython.readthedocs.io/en/latest/tutorials/network.html

from microbit import *
import music

# A lookup table of morse codes and associated characters.
MORSE_CODE_LOOKUP = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0"
}

# durations made a bit shorter than 250ms for a dot
# durations made a bit shorter than 500ms for a dash
DOT_DURATION = 230
DASH_DURATION = 470

# detetct a DOT if incoming signal is less than 250ms.
DOT_THRESHOLD = 250
# detect a DASH if incoming signal is less than 500ms.
DASH_THRESHOLD = 500

# Holds the incoming Morse signals.
buffer = ''
# Holds the translated Morse as characters.
message = ''
# The time from which the device has been waiting for the next event.
started_to_wait = running_time()

def decode(buffer):
    # Attempts to get the buffer of Morse code data from the lookup table. If
    # it's not there, just return a question mark.
    return MORSE_CODE_LOOKUP.get(buffer, '?')

while True:
    if button_a.is_pressed():
        display.show('.')
        pin1.write_digital(1)
        music.pitch(1200, duration=DOT_DURATION, wait=True)
#        sleep(DOT_DURATION)
        pin1.write_digital(0)
        sleep(50) # little sleep added to debounce
        display.clear()
    elif button_b.is_pressed():
        display.show('-')
        pin1.write_digital(1)
        music.pitch(1200, duration=DASH_DURATION, wait=True)
#        sleep(DASH_DURATION)
        pin1.write_digital(0)
        sleep(50) # little sleep added to debounce
        display.clear()
    # Work out how long the device has been waiting for a signal.
    waiting = running_time() - started_to_wait
    # Reset the timestamp for the key_down_time.
    key_down_time = None
    # If pin2 (input) is getting a signal, start timing
    while pin2.read_digital():
        if not key_down_time:
            key_down_time = running_time()
    # Get the current time and call it key_up_time.
    key_up_time = running_time()
    # If there's a key_down_time (created when signal detected)
    if key_down_time:
        # ... then work out for how long it was pressed.
        duration = key_up_time - key_down_time
        # If the duration is less than the max length for a "dot" press...
        if duration < DOT_THRESHOLD:
            # ... then add a dot to the buffer containing incoming Morse codes
            # and display a dot on the display.
            buffer += '.'
            display.show('.')
        # Else, if the duration is less than the max length for a "dash"
        # (but longer than that for a DOT ~ handled above)
        elif duration < DASH_THRESHOLD:
            # ... then add a dash to the buffer and display a dash.
            buffer += '-'
            display.show('-')
        # Otherwise, any other sort of keypress duration is ignored (this isn't
        # needed, but added for "understandability").
        else:
            pass
        # The button press has been handled, so reset the time from which the
        # device is starting to wait for a signal.
        started_to_wait = running_time()
    # check there's not been a pause to indicate an end of the
    # incoming Morse code character. The pause must be longer than a DASH
    # code's duration.
    elif len(buffer) > 0 and waiting > DASH_THRESHOLD:
        # There is a buffer and it's reached the end of a code so...
        # Decode the incoming buffer.
        character = decode(buffer)
        # Reset the buffer to empty.
        buffer = ''
        # Show the decoded character.
        display.show(character)
        # Add the character to the message.
        message += character
    # Finally, if micro:bit was shaken while all the above was going on...
    if accelerometer.was_gesture('shake'):
        # ... display the message on LEDs and serial console
        print(message)
        display.scroll(message)
        # then reset it to empty (ready for a new message).
        message = ''
