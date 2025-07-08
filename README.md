# WebPad

WebPad is a macropad made for web developers everywhere. It uses a system of 5 custom-mapped keys to offer developers the increased efficiency you need when on a tight deadline. It also includes two RGB LEDs (for that extra coolness factor) and uses KMK firmware to control everything.

<img src=assets/full.png alt="full WebPad" width="500"/>

## Features:
- 3D printed case
- 2RGB SK6812MINI LEDs for underglow (open to customization)
- 5 custom-mapped keys (Cherry MX keys)
- All code using kmk firmware (easy to modfiy if you know Python)

## CAD Model:
Everything fits together using 4 M3 screws and heatset inserts, used on the case

It has 2 separate printed pieces: the top section and the bottom section. These sections fit together using the screws mentioned above. These designs were created on Fusion 360, with fit tests done for each of the parts (including with the PCB).

<img src=assets/case_split.png alt="case of WebPad" width="500"/>

## PCB:
Below are my PCB design and schematic. I designed the schematic/PCB to match the needs of web developers, with 5 switches offering access to essential functions (described in the firmware section). Basic connection techniques like using both layers for traces were required and implemented. After a little research, I found that using a ground plane will likely improve functionality in this product.

<img src=assets/PCB_design.png alt="PCB Design" width="500"/>

<img src=assets/schematic.png alt="Schematic" width="500"/>

## Firmware:
This hackpad uses KMK firmware for everything, from mapping the switches to controlling the LEDs. Specifically, the firmware currently offers this functionality:

- RGB LED backlighting
- refresh web page
- clear cache in a browser
- open elements in browser developer tools
- open responsive design mode
- start VSCode Live Server
- open console in developer tools

## BOM:

Here is everything you need to make this hackpad (All parts part of the approved kit)

- 5x Cherry MX Switches
- 5x DSA Keycaps
- 4x M3x5x4 Heatset inserts
- 4x M3x16mm screws
- 2x SK6812 MINI-E LEDs
- 1x XIAO RP2040
- 1x Case (2 printed parts)
