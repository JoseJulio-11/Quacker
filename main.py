from flask import Flask, jsonify, request
from Handler import Chat
from Handler import Message
from Handler import User
from mainpage import mainpage

app = Flask(__name__)

@app.route('/')
def mainPage():
    return mainpage

# ==================== User Methods ====================== #
@app.route('/users', methods=['GET'])
def getAllUsers():
    if request.method == 'GET':
        result = User.getAllUsers()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/users/<int:uid>', methods=['GET'])
def getUserByID(uid):
    if request.method == 'GET':
        result = User.getUserInfo(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/users/active', methods=['GET'])
def getAllUsersByActivity():
    if request.method == 'GET':
        result = User.getActiveUsers()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


# =================== Credential Methods ================= #
@app.route('/credentials', methods=['GET'])
def getCredentials():
    if request.method == 'GET':
        result = User.getAllCredentials()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/credentials/user/<int:uid>', methods=['GET'])
def getUserCredentialByID(uid):
    if request.method == 'GET':
        result = User.getUserCredentials(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


# ================= Activity Methods ======================= #
@app.route('/activities', methods=['GET'])
def getAllActivities():
    if request.method == 'GET':
        result = User.getAllActivity()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/activities/user/<int:uid>', methods=['GET'])
def getUserActivityByID(uid):
    if request.method == 'GET':
        result = User.getUserActivity(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


# ================= Contact Methods ======================== #
@app.route('/contacts', methods=['GET'])
def getAllContacts():
    if request.method == 'GET':
        result = User.getAllContacts()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/contacts/user/<int:uid>', methods=['GET'])
def getUserContactsByID(uid):
    if request.method == 'GET':
        result = User.getUserContacts(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


# ================= Chat Methods ===================== #
@app.route('/chats', methods=['GET'])
def getAllChats():
    if request.method == 'GET':

        result = Chat.getAllChats()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/chats/<int:cid>', methods=['GET'])
def getChatByID(cid):
    if request.method == 'GET':

        result = Chat.getChatByID(cid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/chats/user/<int:uid>', methods=['GET'])
def getUserChatsByID(uid):
    if request.method == 'GET':

        result = Chat.getChatByUserID(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/chats/admin/user/<int:uid>', methods=['GET'])
def getChatsAsAdminByID(uid):
    if request.method == 'GET':

        result = User.getChatAsAdmin(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404

# ============== Participant Methods ================== #
@app.route('/participants', methods=['GET'])
def getAllParticipants():
    if request.method == 'GET':
        result = Chat.getALlParticipants()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/participants/chat/<int:cid>', methods=['GET'])
def getChatParticipantsByID(cid):
    if request.method == 'GET':
        result = Chat.getParticipantsByChatID(cid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


# ============== Message Methods ====================== #
@app.route('/messages', methods=['GET'])
def getAllMessages():
    if request.method == 'GET':

        result = Message.getAllMessages()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404

@app.route('/messages/<int:mid>', methods=['GET'])
def getMessageByID(mid):
    if request.method == 'GET':
        result = Message.getMessageByID(mid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404

@app.route('/messages/chat/<int:cid>', methods=['GET'])
def getMessageByChatID(cid):
    if request.method == 'GET':
        result = Chat.getMessagesByChatID(cid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/messages/user/<int:uid>', methods=['GET'])
def getMessageByUserID(uid):
    if request.method == 'GET':
        result = Message.getMessageByUserID(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


# =============== Topic Methods ======================== #
@app.route('/topics', methods=['GET'])
def getAllTopics():
    if request.method == 'GET':
        result = Message.getAllTopics()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/topics/message/<int:mid>', methods=['GET'])
def getMessageTopicsByID(mid):
    if request.method == 'GET':
        result = Message.getMessageTopics(mid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/topics/user/<int:uid>', methods=['GET'])
def getUserTopicsByID(uid):
    if request.method == 'GET':
        result = User.getUserTopics(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/topics/chat/<int:cid>', methods=['GET'])
def getChatTopicsByID(cid):
    if request.method == 'GET':
        result = Chat.getChatMediaByID(cid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


# ==================== Media Methods ========================= #
@app.route('/medias', methods=['GET'])
def getAllMedia():
    if request.method == 'GET':
        result = Message.getAllMedias()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/medias/message/<int:mid>', methods=['GET'])
def getMessageMediaByID(mid):
    if request.method == 'GET':
        result = Message.getMessageMedia(mid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/medias/chat/<int:cid>', methods=['GET'])
def getChatMediaByID(cid):
    if request.method == 'GET':
        result = Chat.getChatMediaByID(cid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


# ================ Reaction Methods ===================== #
@app.route('/reactions', methods=['GET'])
def getAllReactions():
    if request.method == 'GET':
        result = Message.getAllReacts()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/like', methods=['GET'])
def getAllLikeReactions():
    if request.method == 'GET':
        result = Message.getAllLikes()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/dislike', methods=['GET'])
def getAllDislikeReactions():
    if request.method == 'GET':
        result = Message.getAllDislikes()
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/message/<int:mid>', methods=['GET'])
def getMessageReactionsByID(mid):
    if request.method == 'GET':
        result = Message.getMessageReactionsByID(mid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/user/<int:uid>', methods=['GET'])
def getUserReactionsByID(uid):
    if request.method == 'GET':
        result = User.getUserReactions(uid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/like/message/<int:mid>', methods=['GET'])
def getMessageLikeReactionsByID(mid):
    if request.method == 'GET':
        result = Message.getMessageLikesByID(mid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


@app.route('/reactions/dislike/message/<int:mid>', methods=['GET'])
def getMessageDisLikeReactionsByID(mid):
    if request.method == 'GET':
        result = Message.getMessageDislikesByID(mid)
        return result
    else:
        return jsonify(Error="Method not allowed"), 404


if __name__ == '__main__':
    app.run()
