#!/usr/bin/python

import uno
import sys
import string
import re
from utils_fr import read_file, write_file
from utils_fr_ooo import string2num, ooo_open
from FilesGuiBase import FilesGuiBase
from OooCalcBase import OooCalcBase

class OptOoo(OooCalcBase):
	'''
	'''

	def __init__(self):
		'''
		'''

		super(OptOoo, self).__init__()
		
	def import_data(self, infile, first_column, first_row, skip_top, skip_bottom, recalc=True):
		'''
		'''

		print first_column, first_row
		data_li = read_file(infile)

		nums = []

		for line in data_li[1:]:
			li = []
			for elem in line.split():
				li.append(float(elem))
			nums.append(li)

		num_columns = len(nums[0])
		num_rows = len(nums)

		for i in range(num_rows):
			nums[i] = tuple(nums[i])

		nums = tuple(nums)

		self.set_cursor(first_column-1,first_row-1, first_column+num_columns-2,first_row+num_rows-2)

		self.cursor.setData(nums)
			
		if recalc:
			self.run_recalc()

class Optgui(FilesGuiBase):
	'''
	'''
	
	def __init__(self):
		'''
		'''

		super(Optgui, self).__init__()
		self.w.set_title('Fahlstrom Research LLC OpenOffice Text Importer')
		self.b1=gtk.Button(label="Import into Ooo")
                self.tooltips.set_tip(self.b1, "Import the Data into spreadsheet")
                self.b2=gtk.Button(label="Select a file")
                self.tooltips.set_tip(self.b2, "Select a text file to import into spreadsheet")
                self.b3=gtk.Button(label="Recalculate spreadsheet")
                self.tooltips.set_tip(self.b3, "Select a text file to import into spreadsheet")
                self.b4=gtk.Button(label="Save output to a text file")
                self.tooltips.set_tip(self.b4, "Select a text file to import into spreadsheet")
		self.qb=gtk.Button(label="Quit")
		self.ob=gtk.Button(label="Open Ooo")
		self.l1 = gtk.Label("Enter first cell column")
		self.l2 = gtk.Label("Enter first cell row")
                self.e1 = gtk.Entry()
                self.tooltips.set_tip(self.e1, "Enter a letter or number")
                self.e2 = gtk.Entry()
                self.tooltips.set_tip(self.e2, "Enter a number")
                self.h1=gtk.HBox(False,0)
                self.h2=gtk.HBox(False,0)
                self.v=gtk.VBox(False,0)
                self.w.add(self.v)
                self.v.pack_start(self.h1, True, True, 0)
                self.h1.pack_start(self.l1, True, True, 0)
                self.h1.pack_start(self.e1, True, True, 0)
                self.h1.pack_start(self.l2, True, True, 0)
                self.h1.pack_start(self.e2, True, True, 0)
                self.v.pack_start(self.h2, True, True, 0)
		self.h2.pack_start(self.ob, True, True, 0)
                self.h2.pack_start(self.b2, True, True, 0)
                self.h2.pack_start(self.b1, True, True, 0)
                self.h2.pack_start(self.b3, True, True, 0)
                self.h2.pack_start(self.b4, True, True, 0)
                self.h2.pack_start(self.qb, True, True, 0)
		self.ob.connect('clicked', ooo_open)
		self.b1.connect('clicked', self.run_import)
                self.b2.connect('clicked', self.run_file_open)
                self.b3.connect('clicked', self.run_recalc)
                self.b4.connect('clicked', self.run_file_save)
		self.qb.connect('clicked', self.destroy)

	def run_import(self, widget, data=None):
		'''
		'''

		x = OptOoo()
		colnum, rownum = x.get_rowcol(self.e1.get_text(), self.e2.get_text())
		x.import_data(self.filename_open, colnum, rownum, 0, 0)

def guimain():
	'''
	'''
	
	y = Optgui()
	y.gtk_main()

if __name__ == "__main__":
        if len(sys.argv) > 1:
		if sys.argv[1] == '--gui':
			import pygtk
			import gtk
			import gobject
			guimain()
		else:
			opts = {'-if':None, '-sl':0, '-el':0, '-fc':1, '-fr':1}
			for elem in sys.argv[1:]:
				if elem in opts.keys():
					idex = sys.argv.index(elem)+1
					opts[elem] = sys.argv[idex]
					sys.argv.remove(sys.argv[idex])
					sys.argv.remove(elem)
			x = OptOoo()
			x.import_data(opts['-if'], opts['-fc'], opts['-fr'], opts['-sl'], opts['-el'])

