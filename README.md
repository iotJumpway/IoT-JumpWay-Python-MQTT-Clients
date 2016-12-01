# TechBubble IoT JumpWay Python MQTT Library
============================================

##Introduction

TechBubble Tecnologies Internet of Things (IoT) JumpWay is a web platform that allows anyone to connect IoT devices such as Raspberry Pi, Intel Galileo, Arduino, ESP8266 and even phones,PCs, Macs and laptops to the Internet of Things. The various IoT JumpWay libraries and samples allow you to connect devices and sensors to the IoT JumpWay and control/monitor sensors/actuators and data to and from the devices.

The  Python MQTT library allows developers to communicate with the TechBubble IoT JumpWay MQTT Broker and provides a number of device and applications examples.

Platform <https://iot.techbubbletechnologies.com>.

### Library Installation
---------------------

In all cases whether using devices or applications you first need to install the library. 

- Install the latest version of the library with pip

```
    [root@localhost ~]# pip install techbubbleiotjumpwaymqtt
```

- Upgrade to the latest version of the library with pip

```
    [root@localhost ~]# pip install techbubbleiotjumpwaymqtt --upgrade
```

### Raspberry Pi
------------

Make sure your firmware and software etc is up to date.

- Update firmware

```
    [root@localhost ~]# sudo rpi-update
```

- Update trusted certificates

```
    [root@localhost ~]# sudo apt-get install ca-certificates
```

- Update software

```
    [root@localhost ~]# sudo apt-get update
    
    [root@localhost ~]# sudo apt-get upgrade
    
    [root@localhost ~]# sudo apt-get dist-upgrade
```

### Raspberry Pi Device 
--------------------

- Add LED to pin 18 of your Raspberry Pi

- Download device sample to home folder of Raspberry Pi and add device credentials from IoT JumpWay Developer GUI

    <a href="https://github.com/TechBubbleTechnologies/TechBubble-Iot-JumpWay-Python-MQTT/blob/master/samples/Devices/RaspberryPiDevice.py">https://github.com/TechBubbleTechnologies/TechBubble-Iot-JumpWay-Python-MQTT/blob/master/samples/Devices/RaspberryPiDevice.py</a>

- Run RaspberryPiDevice.py

```
    [root@localhost ~]# sudo python RaspberryPiDevice.py
```
- For more in depth information on setting up and using the device samples, check out the following link:

    <a href="https://github.com/TechBubbleTechnologies/TechBubble-Iot-JumpWay-Python-MQTT/tree/master/samples/Devices">https://github.com/TechBubbleTechnologies/TechBubble-Iot-JumpWay-Python-MQTT/tree/master/samples/Devices</a>

### Raspberry Pi Application 
-------------------------

- Download application sample to home folder of Raspberry Pi and add application credentials from IoT JumpWay Developer GUI. Remember to update the device/zone IDs that your application will be controlling.

    <a href="https://github.com/TechBubbleTechnologies/TechBubble-Iot-JumpWay-Python-MQTT/blob/master/samples/Applications/RaspberryPiApplication.py">https://github.com/TechBubbleTechnologies/TechBubble-Iot-JumpWay-Python-MQTT/blob/master/samples/Applications/RaspberryPiApplication.py</a>


- Run RaspberryPiApplication.py

```
    [root@localhost ~]# sudo python RaspberryPiApplication.py
```
- For more in depth information about setting up and using the application samples, check out the following link:

    <a href="https://github.com/TechBubbleTechnologies/TechBubble-Iot-JumpWay-Python-MQTT/tree/master/samples/Applications">https://github.com/TechBubbleTechnologies/TechBubble-Iot-JumpWay-Python-MQTT/tree/master/samples/Applications</a>

Your LED will now be controlled by the application via the TechBubble IoT JumpWay MQTT Broker

