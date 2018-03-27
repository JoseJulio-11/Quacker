from flask import Flask, jsonify, request
#from Handler.Chat import Chat
#from Handler.Message import Message
#from Handler.User import User
from Handler.DictionaryBuilder import DictionaryBuilder

# Activate
app = Flask(__name__)

@app.route('/')
def mainPage():
    return '<p><b>Welcome</b>, this is the main page for our project application <b>Quacker!!!</b></p>' \
           '<p>Currently you can navigate to the following addresses in the app:</p>' \
           '<ol><li> ###</li>' \
           '</ol>'

@app.route('/user', methods=['GET'])
def getAllUsers():
    if request.method == 'GET':
        result = DictionaryBuilder.build_credential_dict(DictionaryBuilder,[1, "Jackhammer", "TheHammer32", "jackhammer1@gmail.com", "7873431298"])
        return jsonify(userCredential=result)
    else:
        return jsonify(Error="Method not allowed"), 405


if __name__ == '__main__':
    app.run()