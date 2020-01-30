from mysql.connector import connect, Error
import json

def GetMessage(**procedure_parameters):

	try:

		connection = connect(host='127.0.0.1',database='minisnap',port=3306,user='root',password='Ainshallah@010',connection_timeout=5)
		print(connection)
	except Error as e:
		print("problem occured connecting to database")
	else:
		cursor = connection.cursor()

	if procedure_parameters != None :

		procedure_result = cursor.callproc('GetMessage',procedure_parameters)
		print(procedure_result)
	else:
		print('procedure parameters are empty')
		for res in cursor.stored_results():
			dataset = res.fetchall()

		json_raw = dataset[0]
		
		return json_raw

if '__name__' == '__main__':
	GetMessage('ahd')

