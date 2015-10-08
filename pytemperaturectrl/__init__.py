#-*- coding: utf-8 -*-
'''
:requieres: pyserial
:note: A temperature control library

**samples:**

Retrieve Julabo version USB connected on COM5 Windows
	>>> from temperaturectrl import julabo
	>>> tc = Julabo()
	>>> tc.open('COM5')
	>>> print tc.getVersion() # output JULABO CORIO CD - 200F 230V 50Hz Version 2.4.1
	>>> tc.close()
'''
from pytemperaturectrl import *
