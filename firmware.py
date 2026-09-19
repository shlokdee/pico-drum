import time
from machine import Pin, ADC

s0=Pin(16, Pin.OUT)
s1=Pin(17, Pin.OUT)
s2=Pin(18, Pin.OUT)

adc=ADC(Pin(26))

def map_values(x):
  return int((x*127)/65535)


def selection(x):
  s0.value(x&1)
  s1.value((x>>1)&1)
  s2.value((x>>2)&1)


while True:
  lis=[]
  for i in range(8):
    selection(i)
    time.sleep_us(100)
    lis.append(map_values(adc.read_u16()))
  print(lis)
  time.sleep(1)

