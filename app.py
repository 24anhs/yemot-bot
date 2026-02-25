from flask import Flask, request
import os

app = Flask(name)

@app.route('/')
def home():
return "Server is Up!"

@app.route('/yemot', methods=['GET', 'POST'])
def yemot_api():
phone = request.values.get('ApiPhone', 'unknown')
response = "id_list_message=t-Shalom, your phone number is " + phone + "&hangup"
return response

if name == "main":
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
