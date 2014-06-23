#
# GuiBase - A Base class for all GUIs based on PyGTK
#
# Copyright 2013 Fahlstrom Research LLC
#
# Author : Carl A. Fahlstrom
#

import pygtk
import gtk
import gobject

class GuiBase(object):
	'''
	'''
	
	def __init__(self):
		'''
		'''

                self.tooltips = gtk.Tooltips()

		self.w=gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.w.connect('delete_event', self.delete_event)
		self.w.connect('destroy', self.destroy)

	def delete_event(self, widget, event, data=None):
                '''
                '''

                print 'main window closed'
                return False

        def destroy(self, widget, data=None):
                '''
                '''

                gtk.main_quit()

	def gtk_main(self):
		'''
		'''

		self.w.show_all()
		gtk.main()

