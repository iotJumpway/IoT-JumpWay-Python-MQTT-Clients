IoT JumpWay Python MQTT Application Samples
======================================

Here you will find sample application scripts for Raspberry Pi and Desktop (Mac/PC/Laptop etc) applications to connect to the TechBubble Technologies IoT JumpWay using Python and MQTT. The codes allow you to set up a basic application that allows control of devices attached to the same Location Space. Once you understand how it works you are free to modify your code accordingly.

# Before You Begin

Make sure that you have followed the instructions on the home page of this repository and installed the Python MQTT library on your device.

###Connection Credentials
-------------------------

Once you have set these up you can begin to edit your device connection credentials. You will be provided these credentials when you set up a device in the IoT JumpWay GUI.

```
locationID = "YourTechBubbleJumpWayLocationID" 
This is the ID of the Location Space that you attached the device to.
```
```
applicationID = "YourTechBubbleJumpWaApplicationID" 
This is the ID of the Location Application that you are connecting to.
```
```
applicationName = "YourTechBubbleJumpWayApplicationName"
This is the ID of the Location Application that you are connecting to.
```
```
username = "YourTechBubbleJumpWayMQTTUsername" 
This is the MQTT username you are given when you create the Location Application.
```
```
password = "YourTechBubbleJumpWayMQTTPassword" 
This is the MQTT password you are given when you create the Location Application.
```

###Message Callback Functions
--------------------------------

At this moment there is 6 application messagge callback function in place and you can edit the callback functions to carry out specific tasks once they are called.

#### Raspberry Pi Command Callback

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

#### Intel Galileo Command Callback

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
		actuator1Pin.write(1)
	elif jsonData['ActuatorID']==1 and jsonData['Command']=='TOGGLE' and jsonData['CommandValue']=='OFF':
		actuator1Pin.write(0)
```

###Message Publish Functions
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
