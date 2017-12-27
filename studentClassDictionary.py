"""
    - Generate a dictionary of four student seniority levels
    - For each seniority level, generate a random number of students
    and generate a random grade for each student
"""
import random
from StudentStats import StudentStats
from insertStudentData import insertData,selectData

# Store the descriptive stats results
results = []

# Generate a random sample set of students and grades for each seniority level
c = {'freshmen': [random.randint(0,100) for i in range(random.randint(6,32))],
    'sophmore': [random.randint(0,100) for i in range(random.randint(6,32))],
    'junior': [random.randint(0,100) for i in range(random.randint(6,32))],
    'senior': [random.randint(0,100) for i in range(random.randint(6,32))]}

for level in c:
	#print(level) # Test output
	#print(c[level]) # Test output
	ss = StudentStats(c[level])
	results.append(ss.reportStats())

#print(results)
insertData(results)
selectData()
