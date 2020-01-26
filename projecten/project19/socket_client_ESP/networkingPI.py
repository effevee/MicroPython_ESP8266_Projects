# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:38:48 2017

@author: pi
"""

import socket

class PiSocketClient:

	host=""
	port=0
	NUMBYTES=32
	cSocket = None

	@classmethod
	def start(cls,host,port):
		cls.host=host
		cls.port=port
		try:
			cls.cSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			cls.cSocket.connect((cls.host,cls.port))
			return True
		except Exception as e:
			print(e)
			return False

	@classmethod
	def sendData(cls,data):
		cls.cSocket.send(data)

	@classmethod
	def readData(cls):
		data=cls.cSocket.recv(cls.NUMBYTES)
		data=data.decode('ascii')
		return data

	@classmethod
	def stop(cls):
		cls.cSocket.close()




