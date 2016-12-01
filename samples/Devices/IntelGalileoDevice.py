# *****************************************************************************
# Copyright (c) 2016 TechBubble Technologies and other Contributors.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html 
#
# Contributors:
#   Adam Milton-Barker - TechBubble Technologies Limited
#   Andrej Petelin - TechBubble Technologies Limited
#   Irene Naya  - TechBubble Technologies Limited
# *****************************************************************************

import time
import sys
import json
import mraa
import techbubbleiotjumpwaymqtt.device

actuator1Pin = 5
	
locationID = "YourTechBubbleJumpWayLocationID"
zoneID = "YourTechBubbleJumpWayZoneID"
deviceId = "YourTechBubbleJumpWayDeviceID"
deviceName = "YourTechBubbleJumpWayDeviceName"
username = "YourTechBubbleJumpWayMQTTUsername"
password = "YourTechBubbleJumpWayMQTTPassword"

actuator1Pin = mraa.Gpio(actuator1Pin)
actuator1Pin.dir(mraa.DIR_OUT) 
actuator1Pin.write(0)

def customDeviceCommandsCallback(topic,payload):
	print("Received command data: %s" % (payload))
	jsonData = json.loads(payload)
	if jsonData['ActuatorID']==1 and jsonData['Command']=='TOGGLE' and jsonData['CommandValue']=='ON':
		actuator1Pin.write(1)
	elif jsonData['ActuatorID']==1 and jsonData['Command']=='TOGGLE' and jsonData['CommandValue']=='OFF':
		actuator1Pin.write(0)

try:
	deviceOptions = {"locationID": locationID, "zoneID": zoneID, "deviceId": deviceId, "deviceName": deviceName, "username": username, "password": password}
	JumpWayPythonMQTTDeviceConnection = techbubbleiotjumpwaymqtt.device.JumpWayPythonMQTTDeviceConnection(deviceOptions)
except Exception as e:
	print(str(e))
	sys.exit()

JumpWayPythonMQTTDeviceConnection.connectToDevice()
JumpWayPythonMQTTDeviceConnection.subscribeToDeviceCommands()
JumpWayPythonMQTTDeviceConnection.deviceCommandsCallback = customDeviceCommandsCallback

while True:
	#JumpWayPythonMQTTDeviceConnection.publishToDeviceSensors({"Sensor":"Temperature","SensorID":1,"SensorValue":"25.00"})
	#JumpWayPythonMQTTDeviceConnection.publishToDeviceActuators({"Actuator":"LED","ActuatorID":1,"ActuatorValue":"ON"})
	#JumpWayPythonMQTTDeviceConnection.publishToDeviceWarnings({"WarningType":"Threshold","WarningOrigin":"Temperature","WarningValue":"150","WarningMessage":"Device temperature has passed threshold"})
	time.sleep(1)
JumpWayPythonMQTTDeviceConnection.disconnectFromDevice()