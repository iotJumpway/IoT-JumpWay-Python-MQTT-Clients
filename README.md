TechBubble IoT JumpWay Python MQTT Library
============================================

Python MQTT library that allows developers to communicate with the TechBubble IoT JumpWay MQTT Broker.

Platform <https://iot.techbubbletechnologies.com>.

Library Installation
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

Raspberry Pi
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

Raspberry Pi Device 
--------------------

- Add LED to pin 18 of your Raspberry Pi

- Download device sample to home folder of Raspberry Pi and add device credentials from IoT JumpWay Developer GUI

    https://github.com/AdamMiltonBarker/TechBubble-Iot-JumpWay-Python-MQTT/blob/master/samples/Devices/RaspberryPiDevice.py

- Run RaspberryPiDevice.py

```
    [root@localhost ~]# sudo python RaspberryPiDevice.py
```
- For more in depth information on setting up and using the device samples, check out the following link:

    https://github.com/AdamMiltonBarker/TechBubble-Iot-JumpWay-Python-MQTT/blob/master/samples/Devices/README.md#iot-jumpway-python-mqtt-device-samples

Raspberry Pi Application 
-------------------------

- Download application sample to home folder of Raspberry Pi and add application credentials from IoT JumpWay Developer GUI. Remember to update the device/zone IDs that your application will be controlling.

    https://github.com/AdamMiltonBarker/TechBubble-Iot-JumpWay-Python-MQTT/blob/master/samples/Applications/RaspberryPiApplication.py


- Run RaspberryPiApplication.py

```
    [root@localhost ~]# sudo python RaspberryPiApplication.py
```

Your LED will now be controlled by the application via the TechBubble IoT JumpWay MQTT Broker

