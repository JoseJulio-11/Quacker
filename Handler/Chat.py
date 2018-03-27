import DictionaryBuilder as Dic
from DAO.ReadChatDAO import ReadChatDAO

class Chat:

    def getAllChats(self):
        #This method will return all the chats
        dao = ReadChatDAO()
        chat_lists = dao.get
