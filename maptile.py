#A container for the contexts where actual gameplay takes place.
class MapTile(object):
	def __init__(self, x, y, world):
		self.x = x
		self.y = y
		self.world = world
		self.levels = dict()
	def addLevel(self, name, lev):
		self.levels[name] = lev
	def getLevel(self, name):
		return self.levels[name]
	def getWorld(self):
		return self.world