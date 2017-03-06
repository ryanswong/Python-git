class Coordinate:
	
	def __init__(self, X_coor, Y_coor):
		self.coor = [X_coor, Y_coor]
	
	def display(self, X_coor, Y_coor):
		print "here"
	
	
point = Coordinate(5,10)

print (point.coor)

coordinate_list = [[-50,20],[-10, 120],[10, 120],[50, 20], [30, 20]]

for point in coordinate_list:
	print point





