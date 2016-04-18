IoT JumpWay Python MQTT Device Samples
======================================

Here you will find sample device scripts for Raspberry Pi and Intel Galilleo devices to connect to the TechBubble Technologies IoT JumpWay using Python and MQTT. The codes allow you to set up a basic device that allows control of an LED. Once you understand how it works you are free to add as many actuators and sensors to your device and modify your code accordingly.

# Before You Begin

Make sure that you have followed the instructions on the home page of this repository and installed the Python MQTT library on your device.

##Raspberry Pi
------------

First of all you need to connect up an LED to your Raspberry Pi. Connect the LED to pin 18 of your Raspberry Pi or change the following line to reflect which pin your LED is connected to. To connect the LED you will need a minimum of 1 bread board, 1 LED, 1 resistor and two jumper wires.

```
actuator1Pin = 18
```

###Raspberry Pi Credentials
-------------------------

Once you have set these up you can begin to edit your device connection credentials. You will be provided these credentials when you set up a device in the IoT JumpWay GUI.

```
locationID = "YourTechBubbleJumpWayLocationID" 
This is the ID of the Location Space that you attached the device to.
```
```
zoneID = "YourTechBubbleJumpWayZoneID" 
This is the ID of the Location Zone that you attached the device to.
```
```
deviceId = "YourTechBubbleJumpWayDeviceID" 
This is the ID of the Location Device that you created.
```
```
deviceName = "YourTechBubbleJumpWayDeviceName" 
This is the name of the Location Device that you created.
```
```
username = "YourTechBubbleJumpWayMQTTUsername" 
This is the MQTT username you are given when you create the Location Device.
```
```
password = "YourTechBubbleJumpWayMQTTPassword" 
This is the MQTT password you are given when you create the Location Device.
```

###Raspberry Pi Message Callback Functions
--------------------------------

At this moment there is 1 device messagge callback function in place and you can edit the callback functions to carry out specific tasks once its is called.

#### Command Callback

```
JumpWayPythonMQTTDeviceConnection.subscribeToDeviceCommands()
JumpWayPythonMQTTDeviceConnection.deviceCommandsCallback = customDeviceCommandsCallback
```
This is a callback that is triggered when your device receives a command from an application. 
You can edit what this call back does by editing this section:

```
def customDeviceCommandsCallback(topic,payload):
	print("Received command data: %s" % (payload))
	jsonData = json.loads(payload)
	if jsonData['ActuatorID']==1 and jsonData['Command']=='TOGGLE' and jsonData['CommandValue']=='ON':
		GPIO.output(actuator1Pin,GPIO.HIGH)
	elif jsonData['ActuatorID']==1 and jsonData['Command']=='TOGGLE' and jsonData['CommandValue']=='OFF':
		GPIO.output(actuator1Pin,GPIO.LOW)
```

###Raspberry Pi Message Publish Functions
--------------------------------

At this moment there are 4 publish functions in place and you can choose which ones to use.

#### Status Publish

```
JumpWayPythonMQTTDeviceConnection.publishToDeviceStatus("ONLINE")
```
This is a publish command that can send device status notifications to all applications that are subscribed to the device status topic for a particular device. 

#### Sensor Publish

```
JumpWayPythonMQTTDeviceConnection.publishToDeviceSensors({"Sensor":"Temperature","SensorID":1,"SensorValue":"25.00"})
```
This is a publish command that can send device sensor data to all applications that are subscribed to the device sensor topic for a particular device. 

#### Actuator Publish

```
JumpWayPythonMQTTDeviceConnection.publishToDeviceActuators({"Actuator":"LED","ActuatorID":1,"ActuatorValue":"ON"})
```
This is a publish command that can send device actuator data to all applications that are subscribed to the device actuator topic for a particular device. 

#### Warning Publish

```
JumpWayPythonMQTTDeviceConnection.publishToDeviceWarnings({"WarningType":"Threshold","WarningOrigin":"Temperature","WarningValue":"150","WarningMessage":"Device temperature has passed threshold"})
```
This is a publish command that can send device warning statuses to all applications that are subscribed to the device warning topic for a particular device. 


