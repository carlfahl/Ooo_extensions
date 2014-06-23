#
# FilesGuiBase - A Base class for a GUI that includes a file open dialog.
# Inherits from the base class for all GUIs.
#
# Copyright 2013 Fahlstrom Research LLC
#
# Author : Carl A. Fahlstrom
#

import os
import pygtk
import gtk
import gobject
from GuiBase import GuiBase

class FilesGuiBase(GuiBase):
	'''
	'''

	def __init__(self):
		'''
		'''

		super(FilesGuiBase, self).__init__()
		self.filewin = None
                self.filename_save = None
		self.filename_open =None
		self.fopenb = gtk.Button(label="Select a file to open")

	def run_file_open(self, widget, data=None):
                '''
                '''

                self.filewin = gtk.FileSelection("Select a File to Open")

                self.filewin.ok_button.connect("clicked", self.file_ok_sel_open)
                self.filewin.cancel_button.connect("clicked", lambda w: self.filewin.destroy())

                self.filewin.show()

	def run_file_save(self, widget, data=None):
                '''
                '''

                self.filewin = gtk.FileSelection("Select a File to Save To")

                self.filewin.ok_button.connect("clicked", self.file_ok_sel_save)
                self.filewin.cancel_button.connect("clicked", lambda w: self.filewin.destroy())

                self.filewin.show()

	def file_ok_sel_open(self, widget, data=None):
                '''
                '''

                self.filename_open = self.filewin.get_filename()
		self.filewin.destroy()

	def file_ok_sel_save(self, widget, data=None):
                '''
                '''

                self.filename = self.filewin.get_filename()
                if os.path.isfile(self.filename):
                        w = gtk.Window(gtk.WINDOW_TOPLEVEL)
                        l = gtk.Label("Are you sure you want ot overwrite file?")
                        v = gtk.VBox(False, 0)
                        h = gtk.HBox(False, 0)
                        b1 = gtk.Button("YES")
                        b2 = gtk.Button("NO")
                        w.add(v)
                        v.pack_start(l, True, True, 0)
                        v.pack_start(h, True, True, 0)
                        h.pack_start(b1, True, True, 0)
                        h.pack_start(b2, True, True, 0)
                        b1.connect("clicked", lambda t: self.filewin.destroy())
                        b1.connect("clicked", lambda z: w.destroy())
                        b2.connect("clicked", lambda f: w.destroy())
                        w.show_all()
                else:
                        self.filewin.destroy()

