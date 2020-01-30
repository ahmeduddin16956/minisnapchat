import requests


json_data = {"username": "ahmed3018","text": "this is a sample message for ahmed","timeout": 60}

print(json_data)
req = requests.post("http://127.0.0.1:5000/chat",data= {"username": "ahmed3018","text": "this is a sample message for ahmed","timeout": 60})

print(req.text)