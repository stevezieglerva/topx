import heapq


class TopX():
	def __init__(self, topn):
		self.__topn = topn
		self.values = []

	def add(self, item):
#		print("TopX adding: " + str(item))
		self.values.append(item)
		self.values = heapq.nlargest(self.__topn, self.values )
#		print("Current values: " + str(self.values))

	