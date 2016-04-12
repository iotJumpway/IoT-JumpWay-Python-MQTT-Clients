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
# *****************************************************************************

import inspect
import json
import os
import paho.mqtt.client as mqtt
import sys
import time

class JumpWayPythonMQTTDeviceConnection():
	
	def __init__(self, configs):	
		self._configs = configs
		self.mqttClient = None
		self.mqttTLS =  os.path.dirname(os.path.abspath(__file__)) + "/ca.pem"
		self.mqttHost = 'iot.techbubbletechnologies.com'
		self.mqttPort = 8883	
		self.deviceStatusCallback = None	
		self.deviceSensorCallback = None
		self.deviceCommandsCallback = None
		if self._configs['locationID'] == None:
			raise ConfigurationException("locationID property is required")
		if self._configs['zoneID'] == None:
			raise ConfigurationException("zoneID property is required")
		elif self._configs['deviceId'] == None:
			raise ConfigurationException("deviceId property is required")
		elif self._configs['deviceName'] == None:
			raise ConfigurationException("deviceName property is required")
		elif self._configs['username'] == None: 
			raise ConfigurationException("username property is required")
		elif self._configs['password'] == None: 
			raise ConfigurationException("password property is required")
	
	
	def connectToDevice(self):
		self.mqttClient = mqtt.Client(client_id=self._configs['deviceName'], clean_session=True)
		deviceStatusTopic = '%s/Devices/%s/%s/Status' % (self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'])
		self.mqttClient.will_set(deviceStatusTopic, "OFFLINE", 0, False)
		self.mqttClient.tls_set(self.mqttTLS, certfile=None, keyfile=None)
		self.mqttClient.on_connect = self.on_connect
		self.mqttClient.on_message = self.on_message
		self.mqttClient.on_publish = self.on_publish
		self.mqttClient.on_subscribe = self.on_subscribe
		self.mqttClient.username_pw_set(str(self._configs['username']),str(self._configs['password']))
		self.mqttClient.connect(self.mqttHost,self.mqttPort,10)
		self.mqttClient.loop_start()

	def on_connect(self, client, obj, flags, rc):
			self.publishToDeviceStatus("ONLINE")
			print("rc: "+str(rc))
	
	def subscribeToDeviceStatus(self, qos=0):
		if self._configs['locationID'] == None:
			print("locationID is required!")
			return False
		elif self._configs['zoneID'] == None:
			print("zoneID is required!")
			return False
		elif self._configs['deviceId'] == None:
			print("deviceId is required!")
			return False
		else:
			deviceStatusTopic = '%s/Devices/%s/%s/Status' % (self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'])
			self.mqttClient.subscribe(deviceStatusTopic, qos=qos)
			print("Subscribed to Device Status "+deviceStatusTopic)
			return True
	
	def subscribeToDeviceCommands(self, qos=0):
		if self._configs['locationID'] == None:
			print("locationID is required!")
			return False
		elif self._configs['zoneID'] == None:
			print("zoneID is required!")
			return False
		elif self._configs['deviceId'] == None:
			print("deviceId is required!")
			return False
		else:
			deviceCommandsTopic = '%s/Devices/%s/%s/Commands' % (self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'])
			self.mqttClient.subscribe(deviceCommandsTopic, qos=qos)
			print("Subscribed to Device Commands "+deviceCommandsTopic)
			return True
	
	def subscribeToDeviceSensors(self, qos=0):
		if self._configs['locationID'] == None:
			print("locationID is required!")
			return False
			return False
		elif self._configs['zoneID'] == None:
			print("zoneID is required!")
			return False
		elif self._configs['deviceId'] == None:
			print("deviceId is required!")
			return False
		else:
			deviceDataTopic = '%s/Devices/%s/%s/Sensors' % (self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'])
			self.mqttClient.subscribe(deviceDataTopic, qos=qos)
			print("Subscribed to Device Sensors "+deviceDataTopic)
			return True

	def on_subscribe(self, client, obj, mid, granted_qos):
			print("Subscribed: "+str(self._configs['deviceName']))

	def on_message(self, client, obj, msg):
		splitTopic=msg.topic.split("/")
		if splitTopic[4]=='Status':
			if self.deviceStatusCallback == None:
				print("No deviceStatusCallback set")
			else:
				self.deviceStatusCallback(msg.topic,msg.payload)
		elif splitTopic[4]=='Sensors':
			if self.deviceSensorCallback == None:
				print("No deviceSensorCallback set")
			else:
				self.deviceSensorCallback(msg.topic,msg.payload)
		elif splitTopic[4]=='Commands':
			if self.deviceCommandsCallback == None:
				print("No deviceCommandsCallback set")
			else:
				self.deviceCommandsCallback(msg.topic,msg.payload)
	
	def publishToDeviceStatus(self, data):
		if self._configs['locationID'] == None:
			print("locationID is required!")
			return False
		elif self._configs['zoneID'] == None:
			print("zoneID is required!")
			return False
		elif self._configs['deviceId'] == None:
			print("deviceId is required!")
			return False
		else:
			deviceStatusTopic = '%s/Devices/%s/%s/Status' % (self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'])
			self.mqttClient.publish(deviceStatusTopic,data)
			print("Published to Device Status "+deviceStatusTopic)
	
	def publishToDeviceCommands(self, data):
		if self._configs['locationID'] == None:
			print("locationID is required!")
			return False
		elif self._configs['zoneID'] == None:
			print("zoneID is required!")
			return False
		elif self._configs['deviceId'] == None:
			print("deviceId is required!")
			return False
		else:
			deviceCommandsTopic = '%s/Devices/%s/%s/Commands' % (self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'])
			self.mqttClient.publish(deviceCommandsTopic,json.dumps(data))
			print("Published to Device Commands "+deviceCommandsTopic)
	
	def publishToDeviceSensors(self, data):
		if self._configs['locationID'] == None:
			print("locationID is required!")
			return False
		elif self._configs['zoneID'] == None:
			print("zoneID is required!")
			return False
		elif self._configs['deviceId'] == None:
			print("deviceId is required!")
			return False
		else:
			deviceSensorsTopic = '%s/Devices/%s/%s/Sensors' % (self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'])
			self.mqttClient.publish(deviceSensorsTopic,json.dumps(data))
			print("Published to Device Sensors "+deviceSensorsTopic)
	
	def publishToDeviceWarnings(self, data):
		if self._configs['locationID'] == None:
			print("locationID is required!")
			return False
		elif self._configs['zoneID'] == None:
			print("zoneID is required!")
			return False
		elif self._configs['deviceId'] == None:
			print("deviceId is required!")
			return False
		else:
			deviceSensorsTopic = '%s/Devices/%s/%s/Warnings' % (self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'])
			self.mqttClient.publish(deviceSensorsTopic,json.dumps(data))
			print("Published to Device Warnings "+deviceSensorsTopic)

	def on_publish(self, client, obj, mid):
			print("Published: "+str(mid))

	def on_log(self, client, obj, level, string):
			print(string)
	
	def disconnectFromDevice(self):
		self.publishToDeviceStatus("OFFLINE")
		self.mqttClient.disconnect()	
		self.mqttClient.loop_stop()
	
			
