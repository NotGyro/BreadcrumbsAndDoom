#Just calls print. Used for non-networked situations
class DumbPrinter(object):
	def write(self, string):
		print(string)