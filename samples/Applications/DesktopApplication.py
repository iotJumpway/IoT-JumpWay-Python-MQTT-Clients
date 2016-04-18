# *****************************************************************************
# Copyright (c) 2016 TechBubble Technologies and other Contributors.
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
import techbubbleiotjumpwaymqtt.application
	
def customApplicationStatusCallback(topic,payload):
	print("Received application status data: %s" % (payload))

def customDeviceStatusCallback(topic,payload):
	print("Received device status data: %s" % (payload))
	
def customSensorCallback(topic,payload):
	print("Received sensor data: %s" % (payload))
	
def customActuatorCallback(topic,payload):
	print("Received sensor data: %s" % (payload))
	
def customDeviceCommandsCallback(topic,payload):
	print("Received commands data: %s" % (payload))
	
def customDeviceWarningsCallback(topic,payload):
	print("Received warning data: %s" % (payload))
	
locationID = "YourTechBubbleJumpWayLocationID"
applicationID = "YourTechBubbleJumpWayDeviceID"
applicationName = "YourTechBubbleJumpWayDeviceName"
username = "YourTechBubbleJumpWayMQTTUsername"
password = "YourTechBubbleJumpWayMQTTPassword"

try:
	applicationOptions = {"locationID": locationID, "applicationID": applicationID, "applicationName": applicationName, "username": username, "password": password}
	JumpWayPythonMQTTApplicationConnection = techbubbleiotjumpwaymqtt.application.JumpWayPythonMQTTApplicationConnection(applicationOptions)
except Exception as e:
	print(str(e))
	sys.exit()

JumpWayPythonMQTTApplicationConnection.connectToApplication()
#JumpWayPythonMQTTApplicationConnection.subscribeToApplicationStatus(1)
#JumpWayPythonMQTTApplicationConnection.applicationStatusCallback = customApplicationStatusCallback
#JumpWayPythonMQTTApplicationConnection.subscribeToDeviceStatus(1,1)
#JumpWayPythonMQTTApplicationConnection.deviceStatusCallback = customDeviceStatusCallback
#JumpWayPythonMQTTApplicationConnection.subscribeToDeviceSensors(1,1)
#JumpWayPythonMQTTApplicationConnection.deviceSensorCallback = customSensorCallback
#JumpWayPythonMQTTApplicationConnection.subscribeToDeviceActuators(1,1)
#JumpWayPythonMQTTApplicationConnection.deviceActuatorCallback = customActuatorCallback
#JumpWayPythonMQTTApplicationConnection.subscribeToDeviceCommands(1,1)
#JumpWayPythonMQTTApplicationConnection.deviceCommandsCallback = customDeviceCommandsCallback
#JumpWayPythonMQTTApplicationConnection.subscribeToDeviceWarnings(1,1)
#JumpWayPythonMQTTApplicationConnection.deviceWarningsCallback = customDeviceWarningsCallback

while True:
	JumpWayPythonMQTTApplicationConnection.publishToDeviceCommands(1,1,{"Actuator":"LED","ActuatorID":1,"Command":"TOGGLE","CommandValue":"ON"})
	time.sleep(10)
	JumpWayPythonMQTTApplicationConnection.publishToDeviceCommands(1,1,{"Actuator":"LED","ActuatorID":1,"Command":"TOGGLE","CommandValue":"OFF"})
	time.sleep(10)
JumpWayPythonMQTTApplicationConnection.disconnectFromApplication()