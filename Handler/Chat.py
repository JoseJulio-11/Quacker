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
    #TODO verify if the row returns a None
    row = dao.getChatByID(cID)
    if not row:
        return jsonify(Error = " Chat not found"), 404
    else:
        chat = Dic.build_chat_dict(row)
        return jsonify(Chat = chat)


def getParticipantsByChatID(cID):
    #TTHis method returns the list of participants in a determined chat
    #TODO verify if the chat_participants returns None
    chat_participants = dao.getChatParticipant()
    result_list = []
    for row in chat_participants:
        result = Dic.build_participants_dict(row)
        result_list.append(result)
    return jsonify(Participants = result_list)


def getMessagesByChatID(cID):
     #This method will return the messages in a determined  chat
    #TODO verify if the chat_messages return a None
    chat_messages = dao.getChatMessages(cID)
    result_messages = []
    for row in chat_messages:
        result = Dic.build_message_dict(row)
        result_messages.append(result)
    return jsonify(Messages = result_messages)


def getChatByUserID(uID):
    #This method will return the chats on which the user are part of
    #TODO verify if it returns a NONE
    chats = dao.getChatByUserID(uID)
    result_list = []
    for row in chats:
        result = Dic.build_chat_dict(row)
        result_list.append(result)
    return jsonify(Chats = result_list)


def getALlParticipants():
    #THis method will return all the participants on the application
    #TODO verify if it returns a None
    participants = dao.getAllParticipants()
    result_list =[]
    for row in participants:
        result = Dic.build_participants_dict(row)
        result_list.append(result)
    return jsonify(Participants = result_list)


#   def removeChatGroup(self,cID):
#      #THis method will remove a chat
#        dao = ReadChatDAO()
#       if not dao.getChatInfo(cID):
#            return jsonify(Error = "Chat not found"), 404
#       else:
#            #CHECKKKKKKKKKKKK!!-!-!_!_!_!_1!_!!-!:D
#            dao.getAllChats().__getitem__(cID).insert(5, False)
