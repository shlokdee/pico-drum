# pico-drum

pico-drum rpi pico based midi octapad drum... It uses piezos to sense a tap and outputs midi to your computer. 
Its low cost and really easy to build

## Features:
* 8 pads you can map to any drum piece
* Can play using drum sticks
* connects as midi device to your computer
* screw less, you can connect different pieces together with clips
* tpu pads to stop the ceramic disk from shattering on impact with a drumstick

## CAD Model:
<img width="445" height="348" alt="Screenshot From 2026-09-18 23-24-44" src="https://github.com/user-attachments/assets/f3750ca3-e629-4ab5-a048-d99e93610765" />

There is a base plate, on which there are 8 slots to put your pads
The brown and black pads are printed with TPU, and the piezo sensor is sandwiched between them to ensure that it does not break. The bottom plate mounts the pico, multiplexer and the perf board.

## Schematic
<img width="650" height="396" alt="Screenshot From 2026-09-18 15-51-26" src="https://github.com/user-attachments/assets/138a1a25-f7b0-4e73-a301-4a1b594fdad9" />


Raspberry pi pico has only 3 analog ports, hence we have used a multiplexer to connect 8 drum pads. Piezo emits more than 20 volts when struck hard, which could fry the multiplexer and pico. So we use diodes and resistors to cap the voltage to 3.3 volts, which is safe. The resistors and diodes are mounted on a perf board and it is placed in the bottom plate of the enclosure, along with the pico and the multiplexer...


<img width="453" height="315" alt="Screenshot From 2026-09-18 23-11-58" src="https://github.com/user-attachments/assets/b4d9218a-54dc-426a-b2a9-727df4f0b390" />

The perf board layout

## Firmware:
TODO

## How to build
Purchase the components listed in [BOM](BOM.csv)
1. Print the topplate and bottomplate in pla, or any other hard plastic filament.
2. Print the tpupad-Part 1 in 10% infill TPU filament, as we want it to be a bit softer and shock absorbing. Print 8 qty
3. Print the tpupad-Part 2 in 30% infill TPU filament, as it needs to be a bit hard for the drum taps. Print 8 qty
4. Print the clips in TPU 10%, as we need to bend them to fit in place. Print 2 qty
5. Solder in the resistors and the diodes onto the perf board according to the schematic and perf board layout given. Also drill 4 2 mm holes according to the diagram given below...
<img width="318" height="256" alt="image" src="https://github.com/user-attachments/assets/6c6c75e7-ddda-4c41-bd05-dafa376983ad" />
<br>
<img width="594" height="354" alt="image" src="https://github.com/user-attachments/assets/b3fc260d-0801-4e96-97b0-ac6487f780a2" />

6. Place the Pico, mux and the perf board according to the image shown above
7. Place the tpupad-part 1 on the slots provided in the topplate. Then, place your piezo sensors in the circular slot, and route your wires through the holes provided on top. Further, place the tpupad-part 2 on top of the piezo.

<img width="621" height="348" alt="Screenshot From 2026-09-18 20-56-39" src="https://github.com/user-attachments/assets/94d0e1c4-1746-4650-9341-ef6c20b5eed8" />

8. Make all the connections using wires and solder as per the schematic
9. Keep the top plate on top of the bottom plate and secure it using the printed clips.
10. Flash the firmware according to the instructions provided and voila!


