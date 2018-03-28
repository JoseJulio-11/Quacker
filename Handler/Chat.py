from flask import jsonify
from Handler import DictionaryBuilder as Dic
from DAO.ChatDAO import ChatDAO

dao = ChatDAO()


def getAllChats():
     #This method will return all the chats

    chat_lists = dao.getAllChats()
    result_list = []
    for row in chat_lists:
        result = Dic.build_chat_dict(row)
        result_list.append(result)
    return jsonify(Chat = result_list)


def getChatByID(cID):
    #This method will return the determined chat by its ID
    row = dao.getChatByID(cID)
    if not row:
        return jsonify(Error = " Chat not found"), 404
    else:
        chat = Dic.build_chat_dict(row)
        return jsonify(Chat = chat)


def getParticipantsByChatID(cID):
    #TTHis method returns the list of participants in a determined chat

    chat_participants = dao.getChatParticipant()
    result_list = []
    for row in chat_participants:
        result = Dic.build_participants_dict(row)
        result_list.append(result)
    return jsonify(Participants = result_list)


def getMessagesByChatID(cID):
     #This method will return the messages in a determined  chat

    chat_messages = dao.getChatMessages(cID)
    result_messages = []
    for row in chat_messages:
        result = Dic.build_message_dict(row)
        result_messages.append(result)
    return jsonify(Messages = result_messages)


def getChatByUserID(uID):
    #This method will return the chats on which the user are part of

    chats = dao.getChatByUserID(uID)
    if chats is not None:
        result_list = []
        for row in chats:
            result = Dic.build_chat_dict(row)
            result_list.append(result)
        return jsonify(Chats = result_list)
    else:
        return jsonify(Error = "Not Record Found!")


def getALlParticipants():
    #THis method will return all the participants on the application

    participants = dao.getAllParticipants()
    result_list =[]
    for row in participants:
        result = Dic.build_participants_dict(row)
        result_list.append(result)
    return jsonify(Participants = result_list)


def getChatMediaByID(cid):
    media = dao.getChatMedia(cid)
    result_list = []
    for row in media:
        result = Dic.build_media_dict(row)
        result_list.append(result)
    return jsonify(Media=result_list)

def getChatTopicByID(cid):
    media = dao.getChatTopic(cid)
    result_list = []
    for row in media:
        result = Dic.build_media_dict(row)
        result_list.append(result)
    return jsonify(Media=result_list)

#   def removeChatGroup(self,cID):
#      #THis method will remove a chat
#        dao = ReadChatDAO()
#       if not dao.getChatInfo(cID):
#            return jsonify(Error = "Chat not found"), 404
#       else:
#            #CHECKKKKKKKKKKKK!!-!-!_!_!_!_1!_!!-!:D
#            dao.getAllChats().__getitem__(cID).insert(5, False)
