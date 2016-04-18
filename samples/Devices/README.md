IoT JumpWay Python MQTT Device Samples
======================================

Here you will find sample device scripts for Raspberry Pi and Intel Galilleo devices to connect to the TechBubble Technologies IoT JumpWay using Python and MQTT. The codes allow you to set up a basic device that allows control of an LED. Once you understand how it works you are free to add as many actuators and sensors to your device and modify your code accordingly.

# Before You Begin

Make sure that you have followed the instructions on the home page of this repository and installed the Python MQTT library on your device.

Raspberry Pi
------------

First of all you need to connect up an LED to your Raspberry Pi. Connect the LED to pin 18 of your Raspberry Pi or change the following line to reflect which pin your LED is connected to. To connect the LED you will need a minimum of 1 bread board, 1 LED, 1 resistor and two jumper wires.

```
actuator1Pin = 18
```
