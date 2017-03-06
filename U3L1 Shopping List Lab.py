class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

emp1 = Employee("Tobi", 200)
emp2 = Employee("kassy", 300)
print Employee.empCount






'''"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
'''


class Point:
   """docstring for Point"""
   def __init__(self, X_coordinate, Y_coordinate):
      
      self.X_coordinate = X_coordinate
      self.Y_coordinate = Y_coordinate

   def displayPoint(self):
      print "Point %d" % ZZZZZZZZ





point1 = Point(9,8)

