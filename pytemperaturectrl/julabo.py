# -*- coding: utf-8 -*-
'''
julabo.py

Contains Julabo temperature control
 see documentation http://www.julabo.com/sites/default/files/downloads/manuals/french/19524837-V2.pdf at section 10.2.
 :copyright: (c) 2015 by Maxime DAUPHIN
 :license: MIT, see LICENSE for details
'''

import serial
import time
from .pytemperaturectrl import TemperatureControl


class Julabo(TemperatureControl):
	'''Julabo Temperature control implementation'''
	
	# see Julabo doc
	MIN_TIME_INTERVAL = 0.250
	
	
	def __init__(self, *args, **kwargs):
		super(TemperatureControl, self).__init__()
		self.min_time_interval = .250 
		self.serial = None 
		
	def checkIfOpen(self):
		''' Check if serial port is open '''
		if self.serial == None:
			raise Exception('Please call open function before all communication')
		
	def open(self, com_port):
		''' Open serial communication'''
		self.serial = serial.Serial( com_port,
				 baudrate=4800,
				 bytesize=serial.EIGHTBITS,
				 parity=serial.PARITY_NONE,
				 stopbits=serial.STOPBITS_ONE,
				 timeout=1,
				 xonxoff=0,
				 rtscts=0 ) 
		
	def close(self):
		''' Close serial communication'''
		self.checkIfOpen()
		if self.serial != None :
			self.serial.close()
			
	def power( self, on ):
		'''set power to on or off'''
		self.checkIfOpen()
		time.sleep(self.MIN_TIME_INTERVAL)
		value = 1 if on else 0
		self.serial.write('out_mode_05 %d' % value )
		
	def getVersion( self ):
		'''retrieve engine version'''
		self.checkIfOpen()
		time.sleep(self.MIN_TIME_INTERVAL)
		self.serial.write('version')
		return self.serial.readline().strip()

	def getStatus( self ):
		'''retrieve engine status'''
		self.checkIfOpen()
		time.sleep(self.MIN_TIME_INTERVAL)
		self.serial.write('status')
		return self.serial.readline().strip()
		
	def setWorkTemperature( self, temperature_in_degree ):
		'''set setpoint temperature'''
		self.checkIfOpen()
		time.sleep(self.MIN_TIME_INTERVAL)
		self.serial.write( 'out_sp_00 %f' % temperature_in_degree )

	def getWorkTemperature( self ):
		'''get setpoint temperature'''
		self.checkIfOpen()
		time.sleep(self.MIN_TIME_INTERVAL)
		self.serial.write( 'in_sp_00' )		
		return float(self.serial.readline())

	def getCurrentTemperature( self ):
		'''get current tank temperature'''
		self.checkIfOpen()
		time.sleep(self.MIN_TIME_INTERVAL)
		self.serial.write( 'in_pv_00' )		
		return float(self.serial.readline())		

