#
# OooBaseBase - 
#
# Copyright 2013 Fahlstrom Research LLC
#
# Author : Carl A. Fahlstrom
#

from OooBaseWProps import OooBaseWProps

class OooBaseBase(OooBaseWProps):
	'''
	'''

	def __init__(self):
		'''
		'''

		super(OooBaseBase, self).__init__()
		self.rows = self.smgr.createInstanceWithContext("com.sun.star.sdbc.RowSet", self.ctx)

	def setSource(self, dataSource):
		'''
		'''

		self.props.setPropertyValue("DataSourceName", dataSource)

	def runCommand(self, commandtype, command):
		'''
		commandtypes:
		TABLE = 0
		QUERY = 1
		COMMAND = 2
		'''

		self.props.setPropertyValue("CommandType", commandtype)
		self.props.setPropertyValue("Command", command)
		self.rows.execute()

	def insertDataRow(self, data):
		'''
		data is a dictionary of {key:value}
		'''

		self.rows.moveToInsertRow()
		for i, j in data.items():
			self.rows.updateString(self.rows.findColumn(i), j)
		self.rows.insertRow()

