TechBubble IoT JumpWay Python MQTT Library
============================================

Python MQTT library that allows developers to communicate with the TechBubble IoT JumpWay MQTT Broker
Platform <https://iot.techbubbletechnologies.com>.

-  Python 2.7 <https://www.python.org/downloads/release/python-2710/>

Library Dependencies
-------------------

-  paho-mqtt <https://pypi.python.org/pypi/paho-mqtt>

Library Installation
---------------------

- Install the latest version of the library with pip

    [root@localhost ~]# pip install techbubbleiotjumpwaymqtt

- Upgrade to the latest version of the library with pip

    [root@localhost ~]# pip install techbubbleiotjumpwaymqtt --upgrade

Raspberry Pi
------------

- Update firmware

    [root@localhost ~]# sudo rpi-update

- Update trusted certificates

    [root@localhost ~]# sudo apt-get install ca-certificates

- Update software

    [root@localhost ~]# sudo apt-get update
    [root@localhost ~]# sudo apt-get upgrade
    [root@localhost ~]# sudo apt-get dist-upgrade

Raspberry Pi Device 
--------------------

- Add LED to pin 18 of your Raspberry Pi

- Download device sample to home folder of Raspberry Pi and add device credentials from IoT JumpWay Developer GUI

    https://github.com/AdamMiltonBarker/TechBubble-Iot-JumpWay-Python-MQTT/blob/master/samples/Devices/RaspberryPiDevice.py

- Run RaspberryPiDevice.py

    [root@localhost ~]# sudo python RaspberryPiDevice.py

Raspberry Pi Application 
-------------------------

- Download application sample to home folder of Raspberry Pi and add application credentials from IoT JumpWay Developer GUI. Remember to update the device/zone IDs that your application will be controlling.

    https://github.com/AdamMiltonBarker/TechBubble-Iot-JumpWay-Python-MQTT/blob/master/samples/Applications/RaspberryPiApplication.py

- Run RaspberryPiDevice.py

    [root@localhost ~]# sudo python RaspberryPiApplication.py

Your LED will now be controlled by the application via the TechBubble IoT JumpWay MQTT Broker

