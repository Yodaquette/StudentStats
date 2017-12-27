"""
	Andrew Goodman
	July 15, 2016

	Load generated data into a database
"""
import sqlite3 as lite

def insertData(d):
	"""Insert the passed dataset into the table StudentSampleSetStats"""
	try:
		# Open a connection to the database
		dbConnection = lite.connect('StudentStatistics.db')
		cursor = dbConnection.cursor()

		# Insert the data
		cursor.executemany('INSERT INTO StudentSampleSetStats (studentSampleSet,totalStudents,meanGrade,maxGrade,minGrade,medianGrade,modeGrade) VALUES (?,?,?,?,?,?,?)',d)

		# Commit insert statement
		dbConnection.commit()
		dbConnection.close()
		return 0
	except Exception as e:
		print('Error inserting data: {0}'.format(e))
		return 1

def selectData():
	"""Select data from the database"""
	try:
		# Open db connection
		dbConnection = lite.connect('StudentStatistics.db')
		cursor = dbConnection.cursor()

		# Will hold the sql query
		query = ""

		while True:
			# Prompt user for query string
			line = input("Write a SQL query to select some data, or type 'q' to exit\n")

			# Check if the user-entered text is null
			if (line.lower() == "q" or line == ""):
				break

			# Assemble the query string and remove any leading/trailing spaces
			query += line + ";"
			query = query.strip()
			print(query)

			# Validate that the SQL statement is complete and that it begins with SELECT
			if (lite.complete_statement(query) and query.lstrip().upper().startswith("SELECT")):
				for row in cursor.execute(query):
					print(row)
				#print(cursor.fetchall())
			else:
				print("Error selecting data")
				break

				# Reset query string
				query = ""

		# Close the connection
		dbConnection.close()

		return 0
	except Exception as e:
		print('Error selecting data: {0}'.format(e))
		return 1
