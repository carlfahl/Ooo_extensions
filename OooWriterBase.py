#
# OooWriterBase - 
#
# Copyright 2013 Fahlstrom Research LLC
#
# Author : Carl A. Fahlstrom
#

from OooBase import OooBase

class OooWriterBase(OooBase):
	'''
	'''

	def __init__(self):
		'''
		'''

		super(OooWriterBase, self).__init__()
		self.texthandle = self.model.getText()
		self.cursor = self.texthandle.createTextCursor()

	def write_line(self, line):
		'''
		'''

		self.texthandle.setString(line)

	def ():
		'''
		'''
