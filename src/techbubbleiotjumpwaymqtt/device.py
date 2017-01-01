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
		self.deviceCommandsCallback = None
		self.deviceKeysCallback = None
		self.deviceSSLsCallback = None
		self.devicePackageCallback = None
		self.deviceAITrainingCallback = None
		self.deviceAITrainingDataCallback = None
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
		self.mqttClient = mqtt.Client(client_id=self._configs['deviceName'], clean_session=False)
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

	def on_subscribe(self, client, obj, mid, granted_qos):
			print("Subscribed: "+str(self._configs['deviceName']))

	def on_message(self, client, obj, msg):
		splitTopic=msg.topic.split("/")
		if splitTopic[4]=='Commands':
			if self.deviceCommandsCallback == None:
				print("No deviceCommandsCallback set")
			else:
				self.deviceCommandsCallback(msg.topic,msg.payload)
		elif splitTopic[4]=='Keys':
			if self.deviceKeysCallback == None:
				print("No deviceKeysCallback set")
			else:
				self.deviceKeysCallback(msg.topic,msg.payload)
		elif splitTopic[4]=='SSLs':
			if self.deviceSSLsCallback == None:
				print("No deviceSSLsCallback set")
			else:
				self.deviceSSLsCallback(msg.topic,msg.payload)
		elif splitTopic[4]=='Package':
			if self.devicePackageCallback == None:
				print("No devicePackageCallback set")
			else:
				self.devicePackageCallback(msg.topic,msg.payload)
		elif splitTopic[4]=='AITraining':
			if self.deviceAITrainingCallback == None:
				print("No deviceAITrainingCallback set")
			else:
				self.deviceAITrainingCallback(msg.topic,msg.payload)
		elif splitTopic[4]=='AITrainingData':
			if self.deviceAITrainingDataCallback == None:
				print("No deviceAITrainingDataCallback set")
			else:
				self.deviceAITrainingDataCallback(msg.topic,msg.payload)
	
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
	
	def subscribeToDeviceKey(self, qos=0):
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
			deviceKeyTopic = '%s/Devices/%s/%s/Keys' % (self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'])
			self.mqttClient.subscribe(deviceKeyTopic, qos=qos)
			print("Subscribed to Device Keys "+deviceKeyTopic)
			return True
	
	def subscribeToDeviceSSL(self, qos=0):
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
			deviceSSLTopic = '%s/Devices/%s/%s/SSLs' % (self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'])
			self.mqttClient.subscribe(deviceSSLTopic, qos=qos)
			print("Subscribed to Device SSLs "+deviceSSLTopic)
			return True
	
	def subscribeToAITraining(self, qos=0):
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
			deviceAITrainingTopic = '%s/Devices/%s/%s/AITraining' % (self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'])
			self.mqttClient.subscribe(deviceAITrainingTopic, qos=qos)
			print("Subscribed to AI Training "+deviceAITrainingTopic)
			return True
	
	def subscribeToAITrainingData(self, qos=0):
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
			deviceAITrainingDataTopic = '%s/Devices/%s/%s/AITrainingData/#' % (self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'])
			self.mqttClient.subscribe(deviceAITrainingDataTopic, qos=qos)
			print("Subscribed to AI Training Data"+deviceAITrainingDataTopic)
			return True
	
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
	
	def publishToDeviceActuators(self, data):
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
			deviceActuatorsTopic = '%s/Devices/%s/%s/Actuators' % (self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'])
			self.mqttClient.publish(deviceActuatorsTopic,json.dumps(data))
			print("Published to Device Actuators "+deviceActuatorsTopic)
	
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
			deviceWarningsTopic = '%s/Devices/%s/%s/Warnings' % (self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'])
			self.mqttClient.publish(deviceWarningsTopic,json.dumps(data))
			print("Published to Device Warnings "+deviceWarningsTopic)
	
	def publishToDeviceCCTV(self, label, byteArray):
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
			deviceCCTVTopic = '%s/Devices/%s/%s/CCTV/%s' % (self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'], label)
			self.mqttClient.publish(deviceCCTVTopic,byteArray,0)
			print("Published to Device CCTV "+deviceCCTVTopic)
	
	def publishToDeviceCCTVWarnings(self, byteArray):
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
			deviceCCTVWarningsTopic = '%s/Devices/%s/%s/CCTVWarnings' % (self._configs['locationID'], self._configs['zoneID'], self._configs['deviceId'])
			self.mqttClient.publish(deviceCCTVWarningsTopic,byteArray,0)
			print("Published to Device CCTV Warnings "+deviceCCTVWarningsTopic)

	def on_publish(self, client, obj, mid):
			print("Published: "+str(mid))

	def on_log(self, client, obj, level, string):
			print(string)
	
	def disconnectFromDevice(self):
		self.publishToDeviceStatus("OFFLINE")
		self.mqttClient.disconnect()	
		self.mqttClient.loop_stop()
	
			
