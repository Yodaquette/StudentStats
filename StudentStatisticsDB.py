"""
	Andrew Goodman
	July 14, 2016

	Database script to create the student_stats.db database
"""
import sqlite3 as lite

try:
	# Create database or open connect if it already exists
	# Use :memory: to create a database in memory
	dbConnection = lite.connect('StudentStatistics.db')

	# Create cursor object
	cursor = dbConnection.cursor()

	# Create table studentSampleSetStats
	cursor.execute('''DROP TABLE IF EXISTS studentSampleSetStats''')
	cursor.execute('''
		CREATE TABLE StudentSampleSetStats
		(
			studentSampleSetStatsID INTEGER PRIMARY KEY
			,studentSampleSet VARCHAR(500) NULL
			,totalStudents INTEGER NULL
			,meanGrade DECIMAL NULL
			,maxGrade INTEGER NULL
			,minGrade INTEGER NULL
			,medianGrade DECIMAL NULL
			,modeGrade INTEGER NULL
		)
	''')

	dbConnection.commit()
	dbConnection.close()
except Exception as e:
	print('Exception occurred: {0}'.format(str(e)))
