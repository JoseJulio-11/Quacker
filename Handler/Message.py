from flask import jsonify
from Handler import DictionaryBuilder as Dic
import datetime
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


def searchAllChatMessage(cid, json):
    if len(json) != 1:
        return jsonify(Error = " Malformed post request, missing or extra data")
    else:
        search = json['search']
        result = dao.searchAllChatMessages(cid, search)
        if not result:
            return jsonify(Error="No Chat Messages Found")
        mapped_result = []
        for r in result:
            mapped_result.append(Dic.build_extended_message_dict(r))
        return jsonify(Messages = mapped_result)


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
        result = Dic.build_extended_message_dict(row)
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


def getTopicsPerDay():
    today = datetime.datetime.now()
    weekBefore = today - datetime.timedelta(days=5)
    oneDay = datetime.timedelta(days=1)
    topicperday = dict()
    topicperday['1'] = topicsPerDayHelper(weekBefore, oneDay)
    topicperday['2'] = topicsPerDayHelper(weekBefore+oneDay, oneDay)
    topicperday['3'] = topicsPerDayHelper(weekBefore+oneDay+oneDay, oneDay)
    topicperday['4'] = topicsPerDayHelper(weekBefore+oneDay+oneDay+oneDay, oneDay)
    topicperday['5'] = topicsPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay, oneDay)
    topicperday['6'] = topicsPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay+oneDay, oneDay)
    topicperday['7'] = topicsPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay+oneDay+oneDay, oneDay)
    return jsonify(Topic=topicperday)


def topicsPerDayHelper(day, oneday):
    topicsinday = []
    topics = dao.getTopicsPerDay(day - oneday, day)
    for row in topics:
        result = Dic.build_dash_topic_dict(row)
        print(result)
        topicsinday.append(result)
    return topicsinday


def getMessagesPerDay():
    today = datetime.datetime.now()
    weekBefore = today - datetime.timedelta(days=5)
    oneDay = datetime.timedelta(days=1)
    messperday = dict()
    messperday['1'] = messagesPerDayHelper(weekBefore, oneDay)
    messperday['2'] = messagesPerDayHelper(weekBefore+oneDay, oneDay)
    messperday['3'] = messagesPerDayHelper(weekBefore+oneDay+oneDay, oneDay)
    messperday['4'] = messagesPerDayHelper(weekBefore+oneDay+oneDay+oneDay, oneDay)
    messperday['5'] = messagesPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay, oneDay)
    messperday['6'] = messagesPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay+oneDay, oneDay)
    messperday['7'] = messagesPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay+oneDay+oneDay, oneDay)
    return jsonify(Messages=messperday)


def messagesPerDayHelper(day, oneday):
    messages = dao.getMessagesPerDay(day - oneday, day)
    return messages


def getReplyPerDay():
    today = datetime.datetime.now()
    weekBefore = today - datetime.timedelta(days=5)
    oneDay = datetime.timedelta(days=1)
    messperday = dict()
    messperday['1'] = replyPerDayHelper(weekBefore, oneDay)
    messperday['2'] = replyPerDayHelper(weekBefore+oneDay, oneDay)
    messperday['3'] = replyPerDayHelper(weekBefore+oneDay+oneDay, oneDay)
    messperday['4'] = replyPerDayHelper(weekBefore+oneDay+oneDay+oneDay, oneDay)
    messperday['5'] = replyPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay, oneDay)
    messperday['6'] = replyPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay+oneDay, oneDay)
    messperday['7'] = replyPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay+oneDay+oneDay, oneDay)
    return jsonify(Messages=messperday)


def replyPerDayHelper(day, oneday):
    messages = dao.getRepliesPerDay(day - oneday, day)
    return messages

def getLikesPerDay():
    today = datetime.datetime.now()
    weekBefore = today - datetime.timedelta(days=5)
    oneDay = datetime.timedelta(days=1)
    likesperday = dict()
    likesperday['1'] = likesPerDayHelper(weekBefore, oneDay)
    likesperday['2'] = likesPerDayHelper(weekBefore+oneDay, oneDay)
    likesperday['3'] = likesPerDayHelper(weekBefore+oneDay+oneDay, oneDay)
    likesperday['4'] = likesPerDayHelper(weekBefore+oneDay+oneDay+oneDay, oneDay)
    likesperday['5'] = likesPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay, oneDay)
    likesperday['6'] = likesPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay+oneDay, oneDay)
    likesperday['7'] = likesPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay+oneDay+oneDay, oneDay)
    return jsonify(Likes=likesperday)


def likesPerDayHelper(day, oneday):
    messages = dao.getLikesPerDay(day - oneday, day)
    return messages

def getDislikesPerDay():
    today = datetime.datetime.now()
    weekBefore = today - datetime.timedelta(days=5)
    oneDay = datetime.timedelta(days=1)
    dislikesperday = dict()
    dislikesperday['1'] = dislikesPerDayHelper(weekBefore, oneDay)
    dislikesperday['2'] = dislikesPerDayHelper(weekBefore+oneDay, oneDay)
    dislikesperday['3'] = dislikesPerDayHelper(weekBefore+oneDay+oneDay, oneDay)
    dislikesperday['4'] = dislikesPerDayHelper(weekBefore+oneDay+oneDay+oneDay, oneDay)
    dislikesperday['5'] = dislikesPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay, oneDay)
    dislikesperday['6'] = dislikesPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay+oneDay, oneDay)
    dislikesperday['7'] = dislikesPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay+oneDay+oneDay, oneDay)
    return jsonify(Dislikes=dislikesperday)


def dislikesPerDayHelper(day, oneday):
    messages = dao.getDislikesPerDay(day - oneday, day)
    return messages


def insertMessage(json):
    if len(json) != 4:
        return jsonify(Error = " Malformed post request, missing or extra data")
    else:
        text = json['text']
        rid = json['rid']
        uid = json['uid']
        cid = json['cid']
        if text and uid and cid:
            mid = dao.insertMessage(text,uid,cid,rid)
            if mid:
                return jsonify(Chat = "Insert Successful!")
            else:
                return jsonify(ERROR = 'Could not send message')
        else:
            return jsonify(Error = 'Unexpected attributes in post request'), 400

def insertLikeDislike(json):
    if len(json)!=3:
        return jsonify(Error="Could not react to message due to missing information")
    else:
        uid = json['uid']
        mid = json['mid']
        vote = json['vote']
        if uid and mid and vote:
            rid= dao.insertReacted(uid,mid,vote)
            if rid:
                return jsonify(Message = "Like/Dislike successful")
            else:
                return jsonify(Error = "Could not like message")
        else:
            return jsonify(Error="Could not like message")
