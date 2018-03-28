from flask import Flask, jsonify, request
#from Handler.Chat import Chat
#from Handler.Message import Message
#from Handler.User import User
from Handler.DictionaryBuilder import DictionaryBuilder

stub_dict = {'ID': 1, "String": "StringStub", "Date": "2018-02-22"}
# Activate
app = Flask(__name__)


@app.route('/')
def mainPage():
    return '<p><b>Welcome</b>, this is the main page for our project application <b>Quacker!!!</b></p>' \
           '<p>Currently you can navigate to the following addresses in the app:</p>' \
           '<ol>' \
           '<li>/users</li>' \
           '<li>/credentials</li>' \
           '<li>/activities</li> ' \
           '<li>/contacts</li>' \
           '<li>/chats</li>' \
           '<li>/participants</li>' \
           '<li>/messages</li> ' \
           '<li>/reactions</li>' \
           '<li>/topics</li> ' \
           '<li>/medias</li>' \
           '</ol>'


# ==================== User Methods ====================== #
@app.route('/users', methods=['GET'])
def getAllUsers():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        result['User'] = 1
        return jsonify(Users=result)
    else:
        return jsonify(Error="Method not allowed"), 404

@app.route('/users/<int:uID>', methods=['GET'])
def getUserByID(uID):
    if request.method == 'GET':
        # @TODO Add Handler here (GIve uID)
        result = stub_dict.copy()
        result['User'] = uID
        return jsonify(Users=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# =================== Credential Methods ================= #
@app.route('/credentials', methods=['GET'])
def getCredentials():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        result['Credential'] = 1
        return jsonify(Credentials=result)
    else:
        return jsonify(Error="Method not allowed"), 404

@app.route('/credentials/user/<int:uID>', methods=['GET'])
def getCredentialsByUserID(uID):
    if request.method == 'GET':
        # @TODO Add Handler here (GIve uID)
        result = stub_dict.copy()
        result['User'] = uID
        return jsonify(Users=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# ================= Activity Methods ======================= #
@app.route('/activities', methods=['GET'])
def getAllActivities():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        result['Activity'] = 1
        return jsonify(userCredential=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# ================= Contact Methods ======================== #
@app.route('/contacts', methods=['GET'])
def getAllContacts():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        result['Contact'] = 1
        return jsonify(userCredential=result)
    else:
        return jsonify(Error="Method not allowed"), 404

# ================= Chat Methods ===================== #
@app.route('/chats', methods=['GET'])
def getAllChats():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        result['Chat'] = 1
        return jsonify(userCredential=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# ============== Participant Methods ================== #
@app.route('/participants', methods=['GET'])
def getAllParticipants():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        result['Participant'] = 1
        return jsonify(userCredential=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# ============== Message Methods ====================== #
@app.route('/messages', methods=['GET'])
def getAllMessages():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        result['Message'] = 1
        return jsonify(userCredential=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# =============== Topic Methods ======================== #
@app.route('/topics', methods=['GET'])
def getAllTopics():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        result['Topic'] = 1
        return jsonify(userCredential=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# =============== Media Methods ========================= #
@app.route('/media', methods=['GET'])
def getAllMedia():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        result['media'] = 1
        return jsonify(userCredential=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# ================ Reaction Methods ===================== #
@app.route('/reactions', methods=['GET'])
def getAllReactions():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        result['Reaction'] = 1
        return jsonify(userCredential=result)
    else:
        return jsonify(Error="Method not allowed"), 404


if __name__ == '__main__':
    app.run()