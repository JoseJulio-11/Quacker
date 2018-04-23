"""
This Class contains DAO methods for the entities of Messages, Medias, Topics and Reacted
"""
from pg_config import pg_config
import psycopg2

class MessagesDAO:

    def __init__(self):
       connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                           pg_config['user'],
                                                           pg_config['passwd'])
       self.conn = psycopg2._connect(connection_url)

    # ====================== Create Method ================================================== #
    def insertMessage(self, text, cdate, ctime, uid, cid, isDeleted, rid):
        # Create a message to a chat
        mID = 13
        return mID

    def insertReacted(self, uID, mID, rdate, rtime, vote):
        # Create an user reaction to a message
        return uID, mID

    def insertTopic(self, mID, hashtag):
        # Create a topic in a message
        return mID, hashtag

    def insertMedia(self, mID, isVideo, location):
        # Add media to a message
        medID = 3
        return mID, medID

    # ====================== Get Message Records ============================================ #
    # =============== Single Record Queries ==================== #
    def getMessageInfo(self, mID):
        cursor = self.conn.cursor()
        query = "select * from messages where mid = %s;"
        cursor.execute(query, (mID, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRepliedMessage(self, mID):
        cursor = self.conn.cursor()
        query = "select * from messages where mid = (select rid from messages where mid = %s);"
        cursor.execute(query, (mID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ========================= Methods Independent On Time ======================= #
    # ============== Methods For Get Messages ============ #
    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "Select * from Messages;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReplyMessages(self):
        cursor = self.conn.cursor()
        query = "select * from messages where rid is not NULL;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRepliedMessages(self):
        cursor = self.conn.cursor()
        query = "select * from messages where mid in (Select rid from messages where rid is not NULL);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessagesWithMedia(self):
        cursor = self.conn.cursor()
        query = "select * from messages where mid in (Select mid from medias);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessagesWithReactions(self):
        cursor = self.conn.cursor()
        query = "select * from messages where mid in (Select mid from reacted);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessagesWithTopics(self):
        cursor = self.conn.cursor()
        query = "select * from messages where mid in (Select mid from topics);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllActiveMessages(self, isDeleted):
        cursor = self.conn.cursor()
        query = "Select * from Messages where isDeleted = %s;"
        cursor.execute(query, (isDeleted, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ============ Get Messages by chat type ================== #
    def getAllMessagesInChatType(self, isGroupChat):
        cursor = self.conn.cursor()
        query = "select mid, text, mtime, messages.uid, cid, isdeleted, " \
                "rid from chats inner join messages using(cid) where isgroupchat = %s;"
        cursor.execute(query, (isGroupChat, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllActiveMessagesInChatType(self, isGroupChat, isDeleted):
        cursor = self.conn.cursor()
        query = "select mid, text, mtime, messages.uid, cid, isdeleted, " \
                "rid from chats inner join messages using(cid) where isdeleted = %s" \
                " and isgroupchat = %se;"
        cursor.execute(query, (isDeleted, isGroupChat, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReplyMessagesInChatType(self, isGroupChat):
        cursor = self.conn.cursor()
        query = "select mid, text, mtime, messages.uid, cid, isdeleted, " \
                "rid from chats inner join messages using(cid) where isGroupChat = %s " \
                "and rid is not NULL;"
        cursor.execute(query, (isGroupChat,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllRepliedMessagesInChatType(self, isGroupChat):
        cursor = self.conn.cursor()
        query = "select mid, text, mtime, messages.uid, cid, isdeleted, rid " \
                "from chats inner join messages using(cid) where isGroupChat = %s " \
                "and mid in (select rid from messages);"
        cursor.execute(query, (isGroupChat,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessagesWithMediaInChatType(self, isGroupChat):
        cursor = self.conn.cursor()
        query = "select mid, text, mtime, messages.uid, cid, isdeleted, rid" \
                " from messages inner join chats using(cid) where mid in (Select mid from medias)" \
                "and isGroupChat = %s;"
        cursor.execute(query, (isGroupChat, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessagesWithReactionsInChatType(self, isGroupChat):
        cursor = self.conn.cursor()
        query = "select mid, text, mtime, messages.uid, cid, isdeleted, rid" \
                " from messages inner join chats using(cid) where mid in (Select mid from reacted)" \
                "and isGroupChat = %s;"
        cursor.execute(query, (isGroupChat,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMessagesWithTopicsInChatType(self, isGroupChat):
        cursor = self.conn.cursor()
        query = "select mid, text, mtime, messages.uid, cid, isdeleted, rid" \
                " from messages inner join chats using(cid) where mid in (Select mid from topics)" \
                "and isGroupChat = %s;"
        cursor.execute(query, (isGroupChat,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ============== Get Messages in chats ================== #
    def getAllChatMessages(self, cID):
        cursor = self.conn.cursor()
        query = "select * from messages where cid = %s;"
        cursor.execute(query, (cID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllChatActiveMessages(self, cID, isDeleted):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "isdeleted = %s and cid = %s;"
        cursor.execute(query, (isDeleted, cID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllChatReplyMessages(self,cID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "rid is not NULL and cid = %s;"
        cursor.execute(query, (cID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllChatRepliedMessages(self,cID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select rid from messages) and cid = %s;"
        cursor.execute(query, (cID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllChatMessagesWithMedia(self,cID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select mid from media) and cid = %s;"
        cursor.execute(query, (cID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllChatMessagesWithTopic(self,cID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select mid from topics) and cid = %s;"
        cursor.execute(query, (cID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllChatMessagesWithReactions(self,cID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select mid from reacted) and cid = %s;"
        cursor.execute(query, (cID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllChatMessagesWithLikes(self,cID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select mid from reacted where vote = 1) and cid = %s;"
        cursor.execute(query, (cID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllChatMessagesWithDisikes(self,cID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select mid from reacted where vote = -1) and cid = %s;"
        cursor.execute(query, (cID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ========= Get Messages By User ================== #
    def getAllUserMessages(self, uID):
        cursor = self.conn.cursor()
        query = "select * from messages where uid = %s;"
        cursor.execute(query, (uID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserActiveMessages(self, uID, isDeleted):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "isdeleted = %s and uid = %s;"
        cursor.execute(query, (isDeleted, uID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserReplyMessages(self, uID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "rid is not NULL and uid = %s;"
        cursor.execute(query, (uID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserRepliedMessages(self, uID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select rid from messages) and uid = %s;"
        cursor.execute(query, (uID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserMessagesWithMedia(self, uID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select rid from medias) and uid = %s;"
        cursor.execute(query, (uID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserMessagesWithTopic(self, uID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select rid from topics) and uid = %s;"
        cursor.execute(query, (uID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserMessagesWithReactions(self, uID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select rid from reacted) and uid = %s;"
        cursor.execute(query, (uID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserMessagesWithLikes(self, uID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select rid from reacted with vote = 1) and uid = %s;"
        cursor.execute(query, (uID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserMessagesWithDisikes(self, uID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select rid from reacted with vote = -1) and uid = %s;"
        cursor.execute(query, (uID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ========= Get Messages by Chat and User ========== #
    def getAllUserMessagesInChat(self, uID, cID):
        cursor = self.conn.cursor()
        query = "select * from messages where uid = %s and cid = %s;"
        cursor.execute(query, (uID, cID))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserActiveMessagesInChat(self, uID, isDeleted, cID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "isdeleted = %s and uid = %s and cid = %s;"
        cursor.execute(query, (isDeleted, uID, cID))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserReplyMessagesInChat(self, uID, cID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "rid is not NULL and uid = %s and cid = %s;"
        cursor.execute(query, (uID, cID))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserRepliedMessagesInChat(self, uID, cID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select rid from messages) and uid = %s and cid = %s;"
        cursor.execute(query, (uID, cID))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserMessagesWithMediaInChat(self, uID, cID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select rid from medias) and uid = %s and cid = %s;"
        cursor.execute(query, (uID, cID, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserMessagesWithTopicInChat(self, uID, cID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select rid from topics) and uid = %s and cid = %s;"
        cursor.execute(query, (uID,cID, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserMessagesWithReactionsInChat(self, uID, cID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select rid from reacted) and uid = %s and cid = %s;"
        cursor.execute(query, (uID, cID, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserMessagesWithLikesInChat(self, uID, cID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select rid from reacted with vote = 1) and uid = %s and cid = %s;"
        cursor.execute(query, (uID,cID, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllUserMessagesWithDisikesInChat(self, uID, cID):
        cursor = self.conn.cursor()
        query = "select * from messages where " \
                "mid in (select rid from reacted with vote = -1) and uid = %s;"
        cursor.execute(query, (uID,cID, ))
        result = []
        for row in cursor:
            result.append(row)
        return result
    # ===================== Get Topics ========================= #

    def getAllTopics(self):
        cursor = self.conn.cursor()
        query = "select * from topics);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTopicsInMessage(self, mID):
        cursor = self.conn.cursor()
        query = "select * from topics where mid = %s);"
        cursor.execute(query, (mID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTopicsInChat(self, cID):
        cursor = self.conn.cursor()
        query = "select * from topics where cid = %s);"
        cursor.execute(query, (cID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTopicsByUser(self, uID):
        cursor = self.conn.cursor()
        query = "select * from topics where uid = %s);"
        cursor.execute(query, (uID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTopicsByUserInChat(self, uID, cID):
        cursor = self.conn.cursor()
        query = "select * from topics where uid = %s and cid = %s);"
        cursor.execute(query, (uID,cID))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # =================================== Get Reactions =================================== #


    def getMessageReaction(self, mID):
        if mID == 3:
            return self.reacted[0:2]
        elif mID == 8:
            return [self.reacted[2]]
        else:
            return []

    def getMessageLike(self, mID):
        if mID == 3:
            return [self.reacted[0]]
        elif mID == 8:
            return [self.reacted[2]]
        else:
            return []

    def getMessageDislike(self, mID):
        if mID == 3:
            return [self.reacted[1]]
        else:
            return []

    def getAllReactions(self):
        return self.reacted

    def getAllLikeReactions(self):
        result = []
        result.append(self.reacted[0])
        result.append(self.reacted[2])
        return result

    def getAllDislikeReactions(self):
        result = []
        result.append(self.reacted[1])
        return result

    def getAllLikeReactionsBetween(self, bDate, aDate):
        result = []
        if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate >= 20:
             result.append(self.reacted[0])
        if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 17 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate >= 20:
             result.append(self.reacted[2])
        return result

    def getAllDislikeReactionsBetween(self, bDate, aDate):
        result = []
        if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate >= 20:
             result.append(self.reacted[1])
        return result

    def getChatReactions(self, cID):
        # It will return the reactions based on the chat
        if cID == 3:
            return self.reacted[0:2]
        if cID == 1:
            return [self.reacted[3]]
        return []

    def getChatReactionsBetween(self,cID,bDate,aDate):
        # This method will return the reactions of a chat between a determined date

        bDate = [int(bDate[0:4]), int(bDate[5:7]), int(bDate[8:10])]
        aDate = [int(aDate[0:4]), int(aDate[5:7]), int(aDate[8:10])]

        if cID == 3:
            if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[ 2] >= 20:
                return self.reacted[0:2]
        if cID == 1:
            if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[ 2] >= 17:
                return [self.reacted[3]]
        return []

    # Returns the list of reactions between the
    # date and time specified of the user with ID uID
    def getUserReactionsBetween(self, uID, bDate, aDate):
        bDate = [int(bDate[0:4]), int(bDate[5:7]), int(bDate[8:10])]
        aDate = [int(aDate[0:4]), int(aDate[5:7]), int(aDate[8:10])]
        if uID == 2 and bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[
            1] >= 1 and aDate[2] >= 20:
            return [self.reacted[0]]
        elif uID == 6 and bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[
            1] >= 1 and aDate[2] >= 20:
            return [self.reacted[1]]
        elif uID == 1 and bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 17 and aDate[0] >= 2018 and aDate[
            1] >= 1 and aDate[2] >= 17:
            return [self.reacted[2]]
        else:
            return []

    # Returns the list of reactions of the user with ID uID
    def getUserReactions(self, uID):
        if uID == 2:
            return [self.reacted[0]]
        elif uID == 6:
            return [self.reacted[1]]
        elif uID == 1:
            return [self.reacted[2]]
        else:
            return []

    # =================================== Get Media ============================= #
    def getMessageMedia(self, mID):
        if mID == 3:
            return self.media[0]
        elif mID == 9:
            return self.media[1]
        else:
            return []

    def getMedia(self, mediaID):
        if mediaID == 1:
            return self.media[0]
        elif mediaID == 2:
            return self.media[1]
        else:
            return []

    def getAllMedia(self):
        return self.media

    def getAllMediaBetween(self, bDate, aDate):
        result = []
        if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate >= 20:
            result.append(self.reacted[0])
        if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 17 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate >= 20:
            result.append(self.media[1])
        return result

    def getChatMedia(self, cID):
        # This method will return the media sended in that determined chat
        if cID == 1:
            return [self.media[0]]
        if cID == 3:
            return [self.media[1]]
        return []

    def getUserMedia(self, uID):
        # This method will return the media sended in that determined chat
        if uID == 3:
            return [self.media[0]]
        if uID == 4:
            return [self.media[1]]
        return []

    # ============================== Update Methods =============================== #
    def updateMessage(self, mID, text, cdate, ctime, uid, cid, isDeleted, rid):
        # it will update a message by saying if it deleted or not
        return mID

    def updateReacted(self, uID, mID, rdate, rtime, vote):
        # It will change the reaction of the message, 1 liked, -1 disliked
        return uID, mID


    def updateTopic(self, mID, hashtag):
        # Update a topic record
        return mID, hashtag

    def updateMedia(self, mID, medID, isVideo, location):
        # The application may need to change a media's location
        return mID, medID

    # ============================== Delete Methods =============================== #
    def deleteMessage(self, mID):
        # Delete a message
        return mID

    def deleteReacted(self, uID, mID):
        # Delete a made reaction
        return uID, mID

    def deleteTopic(self, hashtag, mID):
        # Delete a topic hashtag
        return hashtag, mID

    def deleteMedia(self, mID):
        # The application may need to change a media's location
        medID = 3
        return mID, medID


