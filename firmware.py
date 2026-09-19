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

pad_notes=[36,38,42,46,49,52,45,48]

pad_hit=[False]*8

threshhold=5000

s0 = DigitalInOut(board.GP16)
s0.direction = Direction.OUTPUT

s1 = DigitalInOut(board.GP17)
s1.direction = Direction.OUTPUT

s2 = DigitalInOut(board.GP18)
s2.direction = Direction.OUTPUT

adc = analogio.AnalogIn(board.GP26)

def map_values(x):
  return min(127, max(1, x // 512))


def selection(x):
  s0.value(x&1)
  s1.value((x>>1)&1)
  s2.value((x>>2)&1)


while True:
  for i in range(8):
    selection(i)
    time.sleep_us(100)
    x=adc.value()
    if x>threshhold and not pad_hit[i]:
        vel=map_values(x)
        midi.send(NoteOn(pad_notes[i], vel))
        pad_hit=True
    elif x<threshhold and pad_hit[i]
        midi.send(NoteOff(pad_notes[i], 0))
        pad_hit=False
  time.sleep(1)
  time.sleep_us(10)

