"""
This Class contain DAO methods for the entities of Chats and Participants
"""
import psycopg2
from pg_config import pg_config
class ChatDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s hostaddr=%s"  % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                            pg_config['host'])
        self.conn = psycopg2._connect(connection_url)


    # ============================== Create Methods ============================= #
    def insertChat(self, cName, cDate, cTime, isGroupChat, adminID):
        # Create a chat
        cID = 5
        return cID

    def insertParticipant(self, cID, uID, pdate, ptime):
        # Insert a participant to a chat
        return cID, uID

    # ============================= Get Methods ================================= #
    def getAllChats(self):
        # This method will return all the chats
        cursor = self.conn.cursor()
        query = "select * from chats;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllActiveChats(self):
        # This method will return all the chats
        cursor = self.conn.cursor()
        query = "select * from chats where isActive=true"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result



    def getChatByUserID(self, uID):
        # This method will return the chats on which that user is in


    def getAllParticipants(self):
        # This method will give all the participants in the application
        cursor = self.conn.cursor()
        query = "select * from participants;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getChatParticipants(self,cID):
        # THis method will return the active participants of a specified chat ( active or nonactive chat)

    def getChatActivePartipants(self,cID):
        # This method will give the active participants in a desired chat


    def getChatNonActiveParticipants(self,cID):
        # This method will return the non active users in a certain chat
        if cID == 3:
            return [self.participants[5]]
        if cID == 4:
            return [self.participants[8]]
        return []

    def getChatInfo(self,cID):
        # This method will return the information of a desired chat
        if cID == 1:
            return self.chat[0]
        if cID == 2:
            return self.chat[1]
        if cID == 3:
            return self.chat[2]
        if cID == 4:
            return self.chat[3]

    def getChatWithMedia(self,mID):
        # This method will return the chat on which determined media is located in
        if mID == 1:
            return self.chat[4]
        if mID == 2:
            return self.chat[2]
        return []

    def getChatsByTopic(self,hashtag):
        # This method will return the chats on which the hashtag was sent
        if hashtag == 'mindblowing':
            return [self.chat[4]]
        if hashtag == 'doyouevenlift?':
            return [self.chat[2]]
        if hashtag == 'wtf':
            return [self.chat[4]]
        return[]

    def getChatByID(self,cID):
        # This method will return the chat given its ID
        if cID == 1:
            return self.chat[0]
        if cID == 2:
            return self.chat[1]
        if cID == 3:
            return self.chat[2]
        if cID == 4:
            return self.chat[3]
        return []

    #Returns a list with the chats of the admin user with ID uID
    def getChatsAsAdmin(self, uID):
        adminChatsList = []
        for r in self.chat:
            if uID == r[6]:
                adminChatsList.append(r)
        return adminChatsList

    def getChatsDeleted(self):
        # This method will return the deleted chats
        return [self.chat[1], self.chat[3]]

    # Returns the list of all chats which the user with ID uID is member of.
    def getChatAsMember(self, uID):
        memberChatsList = []
        for r in self.participants:
            if uID == r[1]:
                memberChatsList.append(r)
        return memberChatsList
    # ======================= Update Methods ========================== #
    def updateChat(self, cID, cName, cDate, cTime, isGroupChat, adminID):
        # This method is supposed to be used to change the chat name
        # Also to that its admin 'deletes' chats by changing it to false
        return cID

    # ======================= Delete Methods ========================= #
    def deleteChat(self, cID):
        # Remove a chat
        return cID

    def deleteParticipant(self, cID, uID):
        # Remove an user from a chat
        return cID, uID

