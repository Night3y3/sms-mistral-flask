from flask import Flask
from flask import request,jsonify
from service.messageService import MessageService

app = Flask(__name__)
app.config.from_pyfile('config.py')

messageService = MessageService()

@app.route('/v1/ds/message', methods=['POST'])
def handle_message():
    message = request.json.get('message')
    result = messageService.processMessage(message)
    print(str(result))
    return str(result)

@app.route('/', methods=['GET'])
def handle_get():
    print("GET request received bruv")

if __name__ == "__main__":
    app.run(host="localhost",port=8000,debug=True)