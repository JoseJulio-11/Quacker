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
           '<ul>' \
           '<li>/users</li> <li>/users/[int:uID]</li> <li>/users/[bool:active]</li>' \
           '<li>/credentials</li> <li>credentials/user/[int:uID]</li>' \
           '<li>/activities</li> <li>activities/user/[int:uID]</li>' \
           '<li>/contacts</li> <li>contacts/user/[int:uID]</li>' \
           '<li>/chats</li>' \
           '<li>/participants</li>' \
           '<li>/messages</li> ' \
           '<li>/reactions</li>' \
           '<li>/topics</li> ' \
           '<li>/medias</li>' \
           '</ul>'


# ==================== User Methods ====================== #
@app.route('/users', methods=['GET'])
def getAllUsers():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Users=result)
    else:
        return jsonify(Error="Method not allowed"), 404

@app.route('/users/<int:uid>', methods=['GET'])
def getUserByID(uid):
    if request.method == 'GET':
        # @TODO Add Handler here (GIve uID)
        result = stub_dict.copy()
        return jsonify(User=result)
    else:
        return jsonify(Error="Method not allowed"), 404

@app.route('/users/<bool:active>', methods=['GET'])
def getAllUsersByActivity(active):
    if request.method == 'GET':
        # @TODO Add Handler here (GIve active)
        result = stub_dict.copy()
        return jsonify(Users=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# =================== Credential Methods ================= #
@app.route('/credentials', methods=['GET'])
def getCredentials():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Credentials=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/credentials/user/<int:uid>', methods=['GET'])
def getUserCredentialByID(uid):
    if request.method == 'GET':
        # @TODO Add Handler here (GIve uID)
        result = stub_dict.copy()
        return jsonify(Credential=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# ================= Activity Methods ======================= #
@app.route('/activities', methods=['GET'])
def getAllActivities():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Activities=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/activities/user/<int:uid>', methods=['GET'])
def getUserActivityByID(uid):
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Activity=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# ================= Contact Methods ======================== #
@app.route('/contacts', methods=['GET'])
def getAllContacts():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Contacts=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/contacts/user/<int:uid>', methods=['GET'])
def getUserContactsByID(uid):
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Contacts=result)
    else:
        return jsonify(Error="Method not allowed"), 404

# ================= Chat Methods ===================== #
@app.route('/chats', methods=['GET'])
def getAllChats():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Chats=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/chats/<int:cid>', methods=['GET'])
def getChatByID(cid):
    if request.method == 'GET':
        # @TODO Add Handler here (Use cid)
        result = stub_dict.copy()
        return jsonify(userCredential=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/chats/user/<int:uid>', methods=['GET'])
def getUserChatsByID(uid):
    if request.method == 'GET':
        # @TODO Add Handler here (Use uid)
        result = stub_dict.copy()
        return jsonify(Chats=result)
    else:
        return jsonify(Error="Method not allowed"), 404

# ============== Participant Methods ================== #
@app.route('/participants', methods=['GET'])
def getAllParticipants():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Participants=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/participants/chat/<int:cid>', methods=['GET'])
def getChatParticipantsByID(cid):
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Participants=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# ============== Message Methods ====================== #
@app.route('/messages', methods=['GET'])
def getAllMessages():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Messages=result)
    else:
        return jsonify(Error="Method not allowed"), 404

@app.route('/messages/<int:mid>', methods=['GET'])
def getMessageByID(mid):
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Message=result)
    else:
        return jsonify(Error="Method not allowed"), 404

@app.route('/messages/chat/<int:cid>', methods=['GET'])
def getMessageByChatID(cid):
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Messages=result)
    else:
        return jsonify(Error="Method not allowed"), 404

@app.route('/messages/user/<int:uid>', methods=['GET'])
def getMessageByChatID(uid):
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Messages=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# =============== Topic Methods ======================== #
@app.route('/topics', methods=['GET'])
def getAllTopics():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Topics=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/topics/message/<int:mid>', methods=['GET'])
def getMessageTopicsByID(mid):
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Topics=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/topics/user/<int:uid>', methods=['GET'])
def getUserTopicsByID(uid):
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Topics=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/topics/chat/<int:cid>', methods=['GET'])
def getChatTopicsByID(cid):
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Topics=result)
    else:
        return jsonify(Error="Method not allowed"), 404

# =============== Media Methods ========================= #
@app.route('/media', methods=['GET'])
def getAllMedia():
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Medias=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/media/message/<int:mid>', methods=['GET'])
def getMessageMediaByID(mid):
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Media=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/media/chat/<int:cid>', methods=['GET'])
def getChatMediaByID(cid):
    if request.method == 'GET':
        # @TODO Add Handler here
        result = stub_dict.copy()
        return jsonify(Media=result)
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