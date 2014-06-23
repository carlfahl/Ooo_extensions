#
#
#
#

class TextProcessBase():
	'''
	This is the base class for programs based on processing a text file and saving the
	output to another text file.

	This provides several methods originally provided by importing methods from utils_fr.py
	'''

	def __init__(self, fname=None):
		'''
		'''

		self.infilename = "";
		self.outfilename = "";
		self.outli = [];
		self.lines = [];

	def set_infilename(self, name):
		'''
		'''

		self.infilename = name

	def set_outfilename(self, name):
		'''
		'''

		self.outfilename = name

	def read_input(self):
		'''
		'''

		try:
			batch_file = open(self.filename, 'r+')
			bfile_lines = batch_file.readlines()
			batch_file.close()
		except:
			print "Not a valid file"

		if split_lines:
			for elem in bfile_lines:
				self.lines.append(elem.split(split_char))
		else:
			self.lines = bfile_lines

	def write_output(self):
		'''
		'''

		try:
			outfile = file(self.outfilename, 'w')
			outfile.write('\n'.join(self.outli))
			outfile.close()
		except:
			print 'Writing to File ', filename, ' Failed'

