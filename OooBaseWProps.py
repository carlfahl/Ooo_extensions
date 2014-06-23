#
# OooBase - The base class for general python programs to interact with OpenOffice.
#
# Copyright 2013 Fahlstrom Research LLC
#
# Author : Carl A. Fahlstrom
#

import uno

class OooBaseWProps(object):
	'''
	Base object for Python OpenOffice extensions
	'''

	def __init__(self):
		'''
		This init method creates a UNO conection to OpenOffice on port 2002.
		The method gets a handle to the current app (Writer, Calc, Impress)
		'''

		self.localContext = uno.getComponentContext()
		self.resolver = self.localContext.ServiceManager.createInstanceWithContext(
				"com.sun.star.bridge.UnoUrlResolver", self.localContext)
		self.ctx = self.resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
		self.smgr = self.ctx.ServiceManager
		self.desktop = self.smgr.createInstanceWithContext("com.sun.star.frame.Desktop", self.ctx)
		self.props = self.smgr.createInstanceWithContext("com.sun.star.beans.PropertySet", self.ctx)
		self.model = self.desktop.getCurrentComponent()
		
