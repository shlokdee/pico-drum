import time
import board
import digitalio
import analogio
import usb_midi
import adafruit_midi

from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.control_change import ControlChange

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

pad_notes=[36,38,42,46,49,52,45,48]  #generic drum midi notes, edit this to put your own, or map in the player software...

pad_hit=[False]*8  #checks whether the pad has already been hit, stops from sending multiple midi commands for the same hit

threshhold=5000

#declaring outputs
s0 = DigitalInOut(board.GP16)
s0.direction = Direction.OUTPUT
s1 = DigitalInOut(board.GP17)
s1.direction = Direction.OUTPUT
s2 = DigitalInOut(board.GP18)
s2.direction = Direction.OUTPUT
adc = analogio.AnalogIn(board.GP26)


while True:
  for i in range(8):
    #selects the correct piezo by setting the proper values on the mux
    s0.value(i&1)
    s1.value((i>>1)&1)
    s2.value((i>>2)&1)

    time.sleep_us(100) #delay for mux to not glitch out
    x=adc.value()
    if x>threshhold and not pad_hit[i]:
        vel=min(127, max(1, x // 512))
        midi.send(NoteOn(pad_notes[i], vel))
        pad_hit=True
    elif x<threshhold and pad_hit[i]
        midi.send(NoteOff(pad_notes[i], 0))
        pad_hit=False
  time.sleep_us(10)

