from flask import jsonify
from Handler import DictionaryBuilder as Dic
from DAO.MessagesDAO import MessagesDAO
dao = MessagesDAO()


def getAllMessages():
    rows = dao.getAllMessages()
    if not rows:
        return jsonify(Error="No Message found"), 404
    result = []
    for row in rows:
        result.append(Dic.build_extended_message_dict(row))
    return jsonify(Messages=result)


def getAllReacts():
    rows = dao.getAllReactions()
    if not rows:
        return jsonify(Error="No reaction"), 404
    result = []
    for row in rows:
        result.append(Dic.build_reacted_dict(row))
    return jsonify(Reacts=result)


def getAllLikes():
    rows = dao.getAllLikes()
    if not rows:
        return jsonify(Error="No reaction"), 404
    result = []
    for row in rows:
        result.append(Dic.build_reacted_dict(row))
    return jsonify(Reacts=result)


def getAllDislikes():
    rows = dao.getAllDislikes()
    if not rows:
        return jsonify(Error="No reaction"), 404
    result = []

    for row in rows:
        result.append(Dic.build_reacted_dict(row))
    return jsonify(Reacts=result)


def getAllMedias():
    rows = dao.getAllMedia()
    if not rows:
        return jsonify(Error="No media"), 404
    result = []
    for row in rows:
        result.append(Dic.build_media_dict(row))
    return jsonify(Medias=result)


def getAllTopics():
    rows = dao.getAllTopics()
    if not rows:
        return jsonify(Error="No topics"), 404
    result = []
    for row in rows:
        result.append(Dic.build_topic_dict(row))
    return jsonify(Topics=result)


def getMessageByID(mID):
    # This method return the message requested by its ID
    row = dao.getMessageInfo(mID)
    if not row:
        return jsonify(Error="Message not found"), 404
    message = Dic.build_message_dict(row)
    return jsonify(Message=message)


def getAllReactionsInMessage(mID):
    # This method return the reaction of a determined message
    rows = dao.getAllReactionsInMessage(mID)
    if not rows:
        return jsonify(Error="Message does not contain reaction"), 404
    result = []
    for row in rows:
        result.append(Dic.build_reacted_dict(row))
    return jsonify(Reaction=result)


def getMessageLikesByID(mID):
    # This method return the reaction of a determined message
    rows = dao.getAllLikesInMessage(mID)
    if not rows:
        return jsonify(Error="Message does not contain reaction"), 404
    result = []
    for row in rows:
        result.append(Dic.build_reacted_dict(row))
    return jsonify(Reaction=result)


def getMessageDislikesByID(mID):
    # This method return the reaction of a determined message
    rows = dao.getAllDislikesInMessage(mID)
    if not rows:
        return jsonify(Error="Message does not contain reaction"), 404
    result = []
    for row in rows:
        result.append(Dic.build_reacted_dict(row))
    return jsonify(Reaction=result)


def getMessageMedia(mID):
    # This method return the reaction of a determined message
    rows = dao.getMessageMedia(mID)
    if not rows:
        return jsonify(Error="Message does not contain Media"), 404
    result = []
    for row in rows:
        result.append(Dic.build_media_dict(row))
    return jsonify(Media=result)


def getMessageTopics(mID):
    # This method return the reaction of a determined message
    rows = dao.getAllTopicsInMessage(mID)
    if not rows:
        return jsonify(Error="Message does not contain Topics"), 404
    result = []
    for row in rows:
        result.append(Dic.build_topic_dict(row))
    return jsonify(Topics=result)


def getMessageByUserID(uID):
    # This method will return the messages of a determined user
    messages = dao.getAllUserMessages(uID)
    if not messages:
        return jsonify(Error="User does not have any messages sent."), 404
    result_list = []
    for row in messages:
        result = Dic.build_message_dict(row)
        result_list.append(result)
    return jsonify(Messages=result_list)


def getUserReactions(uID):
    result = dao.getAllReactionsByUser(uID)
    if not result:
        return jsonify(Error="No Reactions Found")
    mapped_result = []
    for r in result:
        mapped_result.append(Dic.build_reacted_dict(r))
    return jsonify(UserReactions=mapped_result)

def getMessageReactionsCountByID(mID):
    result = dao.getCountReactionsInMessage(mID)
    if not result:
        return jsonify(Error="No Reactions Found")
    mapped_result = dict()
    mapped_result["votes"] = result[0][0]
    return jsonify(MessageReactions=mapped_result)


def getMessageLikesCountByID(mID):
    result = dao.getCountLikesInMessage(mID)
    if not result:
        return jsonify(Error="No Reactions Found")
    mapped_result = dict()
    mapped_result["votes"] = result[0][0]
    return jsonify(MessageReactions=mapped_result)


def getMessageDislikesCountByID(mID):
    result = dao.getCountDislikesInMessage(mID)
    if not result:
        return jsonify(Error="No Reactions Found")
    mapped_result = dict()
    mapped_result["votes"] = result[0][0]
    return jsonify(MessageReactions=mapped_result)


def getUserMessages(uID):
    result = dao.getAllUserMessages(uID)
    if not result:
        return jsonify(Error="No Messages Found")
    mapped_result = []
    for r in result:
        mapped_result.append(Dic.build_message_dict(r))
    return jsonify(UserMessages=mapped_result)

def getUserTopics(uID):
    result = dao.getAllTopicsByUser(uID)
    if not result:
        return jsonify(Error = "No Topics Found")
    mapped_result = []
    for r in result:
        mapped_result.append(Dic.build_topic_dict(r))
    return jsonify(UserTopics = mapped_result)

def getAllTopicsByUser(uID):
    result = dao.getAllTopicsByUser(uID)
    if not result:
        return jsonify(Error="No Topics Found")
    mapped_result = []
    for r in result:
        mapped_result.append(Dic.build_topic_dict(r))
    return jsonify(UserTopics=mapped_result)


def getAllChatMessages(cID):
    # This method will return the messages in a determined  chat
    chat_messages = dao.getAllChatMessages(cID)
    if not chat_messages:
        return jsonify(Error="No Messages Found")
    result_messages = []
    for row in chat_messages:
        result = Dic.build_message_dict(row)
        result_messages.append(result)
    return jsonify(Messages=result_messages)


def getAllUserMessagesInChat(uID,cID):
    # This method will return the messages in a determined  chat
    chat_messages = dao.getAllUserMessagesInChat(uID,cID)
    if not chat_messages:
        return jsonify(Error="No Messages Found")
    result_messages = []
    for row in chat_messages:
        result = Dic.build_message_dict(row)
        result_messages.append(result)
    return jsonify(Messages=result_messages)


def getAllChatactiveMessages(cID):
    # This method will return the messages in a determined  chat
    chat_messages = dao.getAllChatActiveMessages(cID, 'false')
    if not chat_messages:
        return jsonify(Error="No Messages Found")
    result_messages = []
    for row in chat_messages:
        result = Dic.build_message_dict(row)
        result_messages.append(result)
    return jsonify(Messages=result_messages)


def getAllMediaInChat(cid):
    media = dao.getAllMediaInChat(cid)
    if not media:
        return jsonify(Error="No Media Found")
    result_list = []
    for row in media:
        result = Dic.build_media_dict(row)
        result_list.append(result)
    return jsonify(Media=result_list)


def getChatTopicByID(cid):
    media = dao.getAllTopicsInChat(cid)
    if not media:
        return jsonify(Error="No Topic Found")
    result_list = []
    for row in media:
        result = Dic.build_topic_dict(row)
        result_list.append(result)
    return jsonify(Topic=result_list)


def getAllMediaByUser(uid):
    media = dao.getAllMediaByUser(uid)
    if not media:
        return jsonify(Error="No Media Found")
    result_list = []
    for row in media:
        result = Dic.build_media_dict(row)
        result_list.append(result)
    return jsonify(Media=result_list)

def insertMessage(mid,form):
    if len(form) != 5 or mid == 0:
        return jsonify(Error = " Malformed post request, missing or extra data")
    else:
        print('working handler for insert message')
        text = form['text']
        mtime = form['mtime']
        uid = form['uid']
        cid = form['cid']
        isDeleted = form['isDeleted']

        if text and mtime and uid and cid and isDeleted:
           mid = dao.insertMessage(text,mtime,uid,cid,isDeleted)
           print(mid)
           if mid:
            result = Dic.build_message_dict([mid,text,mtime,uid,cid,isDeleted])
            return jsonify(Chat = result)
           else:
               return jsonify(ERROR = 'Could not create group')
        else:
            return jsonify(Error = 'Unexpected attributes in post request'), 400