from flask import jsonify
from Handler import DictionaryBuilder as Dic
from DAO.MessagesDAO import MessagesDAO
from DAO.UserDAO import UserDAO
dao = MessagesDAO()


def getAllMessages():
    rows = dao.getAllMessages()
    if not rows:
        return jsonify(Error=" Message does not contain reaction"), 404
    else:
        result = []
        for row in rows:
            result.append(Dic.build_message_dict(row))
        return jsonify(Messages=result)


def getAllReacts():
    rows = dao.getAllLikeReactions().append(dao.getAllDislikeReactions())
    if not rows:
        return jsonify(Error=" Message does not contain reaction"), 404
    else:
        result = []
        for row in rows:
            result.append(Dic.build_reacted_dict(row))
        return jsonify(Reacts=result)


def getAllLikes():
    rows = dao.getAllLikeReactions()
    if not rows:
        return jsonify(Error=" Message does not contain reaction"), 404
    else:
        result = []
        for row in rows:
            result.append(Dic.build_reacted_dict(row))
        return jsonify(Reacts=result)


def getAllDislikes():
    rows = dao.getAllDislikeReactions()
    if not rows:
        return jsonify(Error=" Message does not contain reaction"), 404
    else:
        result = []
        for row in rows:
            result.append(Dic.build_reacted_dict(row))
        return jsonify(Reacts=result)


def getAllMedias():
    rows = dao.getAllMedia()
    if not rows:
        return jsonify(Error=" Message does not contain reaction"), 404
    else:
        result = []
        for row in rows:
            result.append(Dic.build_media_dict(row))
        return jsonify(Medias=result)


def getAllTopics():
    rows = dao.getAllTopics()
    if not rows:
        return jsonify(Error=" Message does not contain reaction"), 404
    else:
        result = []
        for row in rows:
            result.append(Dic.build_topic_dict(row))
        return jsonify(Topics=result)


def getMessageByID(mID):
#This method return the message requested by its ID
    row = dao.getMessageInfo(mID)
    if not row:
        return jsonify(Error = " Message not found"), 404
    else:
        message = Dic.build_message_dict(row)
        return jsonify(Message = message)


def getMessageReactionsByID(mID):
    #THis method return the reaction of a determined message
    rows = dao.getMessageReaction(mID)
    if not rows:
        return jsonify(Error = " Message does not contain reaction"), 404
    else:
        result = []
        for row in rows:
            result.append(Dic.build_reacted_dict(row))
        return jsonify(Reaction = result)


def getMessageLikesByID(mID):
    #THis method return the reaction of a determined message
    rows = dao.getMessageLike(mID)
    if not rows:
        return jsonify(Error = " Message does not contain reaction"), 404
    else:
        result = []
        for row in rows:
            result.append(Dic.build_reacted_dict(row))
        return jsonify(Reaction = result)


def getMessageDislikesByID(mID):
    #THis method return the reaction of a determined message
    rows = dao.getMessageLike(mID)
    if not rows:
        return jsonify(Error = " Message does not contain reaction"), 404
    else:
        result = []
        for row in rows:
            result.append(Dic.build_reacted_dict(row))
        return jsonify(Reaction = result)


def getMessageMedia(mID):
    #THis method return the reaction of a determined message
    rows = dao.getMessageMedia(mID)
    if not rows:
        return jsonify(Error = " Message does not contain reaction"), 404
    else:
        result = []
        for row in rows:
            result.append(Dic.build_reacted_dict(row))
        return jsonify(Reaction = result)


def getMessageTopics(mID):
    #THis method return the reaction of a determined message
    rows = dao.getMessageTopics(mID)
    if not rows:
        return jsonify(Error = " Message does not contain reaction"), 404
    else:
        result = []
        for row in rows:
            result.append(Dic.build_reacted_dict(row))
        return jsonify(Reaction = result)

def getMessageByUserID(uID):
    #This method will returnt the messages of a determined user
    dao = UserDAO()
    messages = dao.getUserMessages(uID)
    if not messages:
        return jsonify(Error = " User does not have any messages sent."), 404
    else:
        result_list =[]
        for row in messages:
            result= Dic.build_message_dict(row)
            result_list.append(result)
        return jsonify(Messages = result_list)

