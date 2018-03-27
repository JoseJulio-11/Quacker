from flask import jsonify
import DictionaryBuilder as Dic
from DAO.ReadChatDAO import ReadChatDAO


class Chat:

    def getAllChats(self):
        #This method will return all the chats
        dao = ReadChatDAO()
        chat_lists = dao.getAllChats()
        result_list = []
        for row in chat_lists:
            result = Dic.build_chat_dic(row)
            result_list.append(result)
        return jsonify(Chat = result_list)

    def removeChatGroup(self,cID):
        #THis method will remove a chat
        dao = ReadChatDAO()
        if not dao.getChatInfo()

