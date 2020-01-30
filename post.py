from mysql.connector import connect
from mysql.connector import Error
import json


def PostMessage(*procedure_parameters):
	
	try:

		connection = connect(host='127.0.0.1',database='minisnap',port=3306,user='root',password='Ainshallah@010',connection_timeout=5)
	except Error as e:
		print(e)

	else:
		try:

			cursor = connection.cursor()
		except err as e:
			print(e)
		else:

			try:

				procedure_result = cursor.callproc('PostMessage', procedure_parameters)

			except Error as e:
				print("An error occured while executing procedure {}".format(e))
			else:

				for res in cursor.stored_results():
					dataset = res.fetchall()
					column_names = res.description

				json_raw = dataset[0][0]
				json_data = {}
				json_data['id'] = json_raw

				return json_data





if __name__ == '__main__':
	PostMessage('vhfv','this is for yaba',10,'PostMessage')




