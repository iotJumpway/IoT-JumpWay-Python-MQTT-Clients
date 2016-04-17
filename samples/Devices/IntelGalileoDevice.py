# *****************************************************************************
# Copyright (c) 2015 TechBubble Technologies and other Contributors.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html 
#
# Contributors:
#   Adam Milton-Barker  - Initial Contribution
#   Adam Mosely  - Tester
#   John Ducrest  - Tester
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

def customStatusCallback(topic,payload):
	print("Received status data: %s" % (payload))
	
def customSensorCallback(topic,payload):
	print("Received sensor data: %s" % (payload))
	
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
#JumpWayPythonMQTTDeviceConnection.subscribeToDeviceStatus()
#JumpWayPythonMQTTDeviceConnection.deviceStatusCallback = customStatusCallback
#JumpWayPythonMQTTDeviceConnection.subscribeToDeviceSensors()
#JumpWayPythonMQTTDeviceConnection.deviceSensorCallback = customSensorCallback
JumpWayPythonMQTTDeviceConnection.subscribeToDeviceCommands()
JumpWayPythonMQTTDeviceConnection.deviceCommandsCallback = customDeviceCommandsCallback

while True:
	time.sleep(1)
JumpWayPythonMQTTDeviceConnection.disconnectFromDevice()