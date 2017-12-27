"""
	Andrew Goodman
	July 5, 2016

	Create a class that calculates the descriptive statistics
	from a randomly generated set of students
"""
class StudentStats():
	def __init__(self,s = []):
		"""Initialize the Student Stats class"""
		self.studentSet = s
		self.sortDataset() # Sort the set

		self.totalStudents = len(s) # Get the total number of students in the sample set
		self.meanGrade = self.meanGrade()
		self.maxGrade = self.findMaxGrade()
		self.minGrade = self.findMinGrade()
		self.medianGrade = self.findMedianGrade()
		self.modeGrade = 0

	def sortDataset(self):
		"""Sort the dataset"""
		self.studentSet.sort()

	def meanGrade(self):
		"""Calculate the grade point average for the student set"""
		gradeSum = 0
		for student in self.studentSet:
			gradeSum += student
		return gradeSum / self.totalStudents

	def findMaxGrade(self):
		"""Determine which grade in the student set is the highest"""
		return self.studentSet[-1]

	def findMinGrade(self):
		"""Determine which grade in the student set is the highest"""
		return self.studentSet[0]

	def findMedianGrade(self):
		"""Determine which grade is in the middle of the student sample"""
		if(self.totalStudents % 2 == 0):
			# Calculate the average of the two grades in the middle of the sample set
			self.medianGrade = (((self.studentSet[int(round((self.totalStudents / 2),0))]) + (self.studentSet[int(round(((self.totalStudents / 2) + 1),0))])) / 2)
		else:
			# Get the grade in the middle of the sample set
			self.medianGrade = (self.studentSet[int(round(((self.totalStudents + 1) / 2),0))])
		return self.medianGrade

	def reportStats(self):
		"""Return all statistics for the student sample set"""
		return (str(self.studentSet),self.totalStudents,self.meanGrade,self.maxGrade
				,self.minGrade,self.medianGrade,self.modeGrade)
