from post import PostMessage
from flask import Flask, jsonify,request


app = Flask(__name__)


@app.route('/chat',methods=['POST'])

def Post():
	

	content = request.get_json()	
	id_data = PostMessage(content['username'],content['text'],content['timeout'],'PostProcedure')
	return jsonify(id_data)

@app.route('/chat/id',methods=['POST'])
def Get():
	content = request.get_json()
	result = GetMessage(content['id'])
	return jsonify(result)

if __name__ == '__main__':

	app.run(debug=True)

