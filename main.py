from flask import Flask, jsonify, request
from Handler import Chat
from Handler import Message
from Handler import User


stub_dict = {'ID': 1, "String": "StringStub", "Date": "2018-02-22"}
# Activate
app = Flask(__name__)

@app.route('/')
def mainPage():
    return '<p><b>Welcome</b>, this is the main page for our project application <b>Quacker!!!</b></p>' \
           '<p>Currently you can navigate to the following addresses in the app:</p>' \
           '<ul>' \
           '<li>/users</li> <li>/users/[int:uid]</li> <li>/users/active</li>' \
           '<li>/credentials</li> <li>/credentials/user/[int:uid]</li>' \
           '<li>/activities</li> <li>/activities/user/[int:uid]</li>' \
           '<li>/contacts</li> <li>/contacts/user/[int:uid]</li>' \
           '<li>/chats</li> <li>/chats/[int:cid]</li> <li>/chats/user/[int:uid]</li>' \
           '<li>/participants</li> <li>/participants/chats/[int:cid]</li>' \
           '<li>/messages</li> <li>/messages/[int:mid]</li> <li>/messages/user/[int:uid]</li>' \
           '<li>/messages/chat/[int:cid]</li>' \
           '<li>/medias</li> <li>/medias/chat/[int:cid]</li> <li>/medias/messages/[int:mid]</li>' \
           '<li>/topics</li> <li>/topics/chat/[int:cid]</li> <li>/topics/messages/[int:mid]</li>' \
           '<li>/topics/user/[int:mid]</li>' \
           '<li>/reactions</li> <li>/reactions/messages/[int:mid]</li> <li>/reactions/user/[int:uid]</li>' \
           '<li>/reactions/likes</li> <li>/reactions/likes/messages/[int:mid]</li> ' \
           '<li>/reactions/dislikes</li> <li>/reactions/dislikes/messages/[int:mid]</li> ' \
           '</ul>'


# ==================== User Methods ====================== #
@app.route('/users', methods=['GET'])
def getAllUsers():
    if request.method == 'GET':
        result = User.getAllUsers()
        return jsonify(Users=result)
    else:
        return jsonify(Error="Method not allowed"), 404

@app.route('/users/<int:uid>', methods=['GET'])
def getUserByID(uid):
    if request.method == 'GET':
        result = User.getUserInfo(uid)
        return jsonify(User=result)
    else:
        return jsonify(Error="Method not allowed"), 404

@app.route('/users/active', methods=['GET'])
def getAllUsersByActivity():
    if request.method == 'GET':
        result = User.getActiveUsers()
        return jsonify(Users=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# =================== Credential Methods ================= #
@app.route('/credentials', methods=['GET'])
def getCredentials():
    if request.method == 'GET':
        result = User.getAllCredentials()
        return jsonify(Credentials=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/credentials/user/<int:uid>', methods=['GET'])
def getUserCredentialByID(uid):
    if request.method == 'GET':
        result = User.getUserCredentials(uid)
        return jsonify(Credential=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# ================= Activity Methods ======================= #
@app.route('/activities', methods=['GET'])
def getAllActivities():
    if request.method == 'GET':
        result = User.getAllActivity()
        return jsonify(Activities=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/activities/user/<int:uid>', methods=['GET'])
def getUserActivityByID(uid):
    if request.method == 'GET':
        result = User.getUserActivity(uid)
        return jsonify(Activity=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# ================= Contact Methods ======================== #
@app.route('/contacts', methods=['GET'])
def getAllContacts():
    if request.method == 'GET':
        result = User.getAllContacts()
        return jsonify(Contacts=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/contacts/user/<int:uid>', methods=['GET'])
def getUserContactsByID(uid):
    if request.method == 'GET':
        result = User.getUserContacts(uid)
        return jsonify(Contacts=result)
    else:
        return jsonify(Error="Method not allowed"), 404

# ================= Chat Methods ===================== #
@app.route('/chats', methods=['GET'])
def getAllChats():
    if request.method == 'GET':

        result = Chat.getAllChats()
        return jsonify(Chats=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/chats/<int:cid>', methods=['GET'])
def getChatByID(cid):
    if request.method == 'GET':

        result = Chat.getChatByID(cid)
        return jsonify(userCredential=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/chats/user/<int:uid>', methods=['GET'])
def getUserChatsByID(uid):
    if request.method == 'GET':

        result = Chat.getChatByUserID(uid)
        return jsonify(Chats=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# ============== Participant Methods ================== #
@app.route('/participants', methods=['GET'])
def getAllParticipants():
    if request.method == 'GET':
        result = Chat.getALlParticipants()
        return jsonify(Participants=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/participants/chat/<int:cid>', methods=['GET'])
def getChatParticipantsByID(cid):
    if request.method == 'GET':
        result = Chat.getParticipantsByChatID(cid)
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
def getMessageByUserID(uid):
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


# ==================== Media Methods ========================= #
@app.route('/medias', methods=['GET'])
def getAllMedia():
    if request.method == 'GET':
        result = Message.getAllMedias()
        return jsonify(Medias=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/medias/message/<int:mid>', methods=['GET'])
def getMessageMediaByID(mid):
    if request.method == 'GET':
        result = Message.getMessageMedia(mid)
        return jsonify(Media=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/medias/chat/<int:cid>', methods=['GET'])
def getChatMediaByID(cid):
    if request.method == 'GET':
        result = Chat.getChatMediaByID(cid)
        return jsonify(Media=result)
    else:
        return jsonify(Error="Method not allowed"), 404


# ================ Reaction Methods ===================== #
@app.route('/reactions', methods=['GET'])
def getAllReactions():
    if request.method == 'GET':
        result = Message.getAllReacts()
        return jsonify(Reactions=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/like', methods=['GET'])
def getAllLikeReactions():
    if request.method == 'GET':
        result = Message.getAllLikes()
        return jsonify(Reactions=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/dislike', methods=['GET'])
def getAllDislikeReactions():
    if request.method == 'GET':
        result = Message.getAllDislikes()
        return jsonify(Reactions=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/message/<int:mid>', methods=['GET'])
def getMessageReactionsByID(mid):
    if request.method == 'GET':
        result = Message.getMessageReactionsByID(mid)
        return jsonify(Reactions=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/user/<int:uid>', methods=['GET'])
def getUserReactionsByID(uid):
    if request.method == 'GET':
        result = User.getUserReactions(uid)
        return jsonify(Reactions=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/like/message/<int:mid>', methods=['GET'])
def getMessageLikeReactionsByID(mid):
    if request.method == 'GET':
        result = Message.getMessageLikesByID(mid)
        return jsonify(Reactions=result)
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/dislike/message/<int:mid>', methods=['GET'])
def getMessageDisLikeReactionsByID(mid):
    if request.method == 'GET':
        result = Message.getMessageDislikesByID(mid)
        return jsonify(Reactions=result)
    else:
        return jsonify(Error="Method not allowed"), 404


if __name__ == '__main__':
    app.run()