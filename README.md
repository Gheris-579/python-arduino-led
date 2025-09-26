# python-arduino-led

A project to control LEDs on an Arduino UNO R3 using Python.  
This repository contains an Arduino sketch (`.ino`) and a Python script (`.py`) that allows the user to turn two LEDs on and off via input.

---

## Table of Contents
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Setup](#setup)
- [Usage](#usage)


---

## Hardware Requirements
- Arduino UNO R3  
- 2 LEDs  
- 2 resistors (220Ω recommended)  
- Breadboard and jumper wires  

---

## Software Requirements
- Arduino IDE  
- Python 3.x  
- `pyserial` library (`pip install pyserial`)  

---

## Setup

### Arduino
1. Open `led_control.ino` in the Arduino IDE.  
2. Connect LED1 to pin 8 and LED2 to pin 9 (with resistors in series).  
3. Connect Arduino to your PC via USB.  
4. Upload the sketch to the Arduino.  

### Python
1. Open `led_control.py`.  
2. Make sure the `port` variable matches your Arduino COM port:
   ```python
   arduino = serial.Serial(port="COM3", baudrate=9600, timeout=1)
   ```
   - On Windows: `COM3`, `COM4`, etc.  
   - On Linux/macOS: `/dev/ttyUSB0` or `/dev/ttyACM0`.  
3. Install pyserial if not already installed:
   ```bash
   pip install pyserial
   ```

---


## Usage
1. Run the Python script:
   ```bash
   python led_control.py
   ```
2. Enter your choice:
   - `1` → Turn on LED1  
   - `2` → Turn on LED2  
   - `0` → Turn off both LEDs  
   - `q` → Quit the program  

---



