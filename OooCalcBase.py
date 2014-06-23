#
# OooCalcBase - 
#
# Copyright 2013 Fahlstrom Research LLC
#
# Author : Carl A. Fahlstrom
#

import re
from utils_fr_ooo import string2num

class OooCalcBase(OooBase):
	'''
	'''

	def __init__(self):
		'''
		'''

		super(OooCalcBase, self).__init__()
		self.model.enableAutomaticCalculation(False)
		self.sheets = self.model.getSheets()
		self.calc_sheet = self.sheets.Sheet1
		self.cursor = None

	def get_rowcol(self, str1, str2):
		'''
		'''

		pattern_num = re.compile(r'[0-9]+')
		pattern_let = re.compile(r'[A-Z]+')
		try:
			if pattern_let.search(str1):
				colnum = string2num(str1)
			else:
				if pattern_num.search(str1):
					colnum = int(str1)
		except:
			print "Setting column integer failed"
			pass
		try:
			if pattern_num.search(str2):
				rownum = int(str2)
		except:
			pass

		return colnum, rownum

	def run_recalc(self):
		'''
		'''

		self.model.calculateAll()

	def set_cursor(self, num1, num2, num3, num4):
		'''
		'''

		self.cursor = self.calc_sheet.getCellRangeByPosition(num1, num2, num3, num4)

