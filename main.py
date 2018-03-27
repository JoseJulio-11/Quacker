from flask import Flask, jsonify, request
from DAO import UserDAO
from Handler import Chat, Dashboard, Message, User, DictionaryBuilder

# Activate
app = Flask(__name__)

@app.route('/')
def mainPage():
    return 'Welcome, this is the main page for our project application Quacker!!!\n\n' \
           'Currently you can navigate to the following addresses in the app:\n' \
           '\t 1. ###'


@app.route('/login/<int:uid>', methods=['GET'])
def getUserCredential(uid):
    if request.method == 'GET':
        result = DictionaryBuilder.DictionaryBuilder.build_credential_dict([1, "Jackhammer", "TheHammer32", "jackhammer1@gmail.com", "7873431298"])
        return jsonify(userCredential=result)
    else:
        return jsonify(Error="Method not allowed"), 405


if __name__ == '__main__':
    app.run()