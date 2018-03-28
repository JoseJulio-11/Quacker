
class ChatDAO:

    def __init__(self):
        # UID, FNAME, LNAME, CDATE, CTIME, PSEUDONAME
        self.users = [[1, "Jack", "Hammer", "2018-1-1", "08:00:00", "The Nail"],
                      [2, "Sam", "Master", "2018-1-1", "16:00:00", "Miss Master"],
                      [3, "Barbara", "Berry", "2018-1-5", "12:00:00", "Barb"],
                      [4, "Jimmy", "Newton", "2018-2-1", "14:35:40", "Newton"],
                      [5, "Timmy", "Turner", "2017-12-31", "10:15:55", "THe Corner"],
                      [6, "Mary", "Johnson", "2017-1-1", "15:00:00", "Marge"]]

        # UID, Username, Password, UEmail, UPhone
        self.credentials = [[1, "Jackhammer", "TheHammer32", "jackhammer1@gmail.com", "7873431298"],
                            [2, "sammymaster1", "MasterKey64", "smaster1@gmail.com", "7872984532"],
                            [3, "berryberry", "barb_wire", "barb.berry141@gmail.com", "7877651243"],
                            [4, "jimnewton", "newton100", "jimmy.newton78@gmail.com", "9395673214"],
                            [5, "timtim", "fairlyodd12", "timmy.turner12@gmail.com", "5463126732"],
                            [6, "mary64", "maryjesus25", "mary.johnson25@gmail.com", "8763417641"]]

        # aID, lastAccessToDBDate, lastAccessToDBTime, isActive
        self.activity = [[1, "2018-3-21", "10:30:56", True],
                         [2, "2018-3-21", "10:20:25", True],
                         [3, "2018-3-21", "10:40:10", True],
                         [4, "2018-3-17", "13:17:12", False],
                         [5, "2018-3-21", "10:20:30", True],
                         [6, "2018-2-05", "11:33:10", False]]
        # ownerid, memberid
        self.contacts = [[1, 2], [1, 4], [1, 5],
                         [4, 2], [4, 1],
                         [3, 2],
                         [5, 1], [5, 2],
                         [6, 2], [6, 3]]

        # cid, cname, cdate, ctime, isgroupchat, isactive, adminid
        self.chat = [[1, "Machos", "2018-1-15", "16:02:13", True, True, 1],
                     [2, "BFF", "2018-1-10", "06:04:13", False, True, 3],
                     [3, "Gals", "2018-1-20", "12:43:41", True, False, 6],
                     [4, "Jimmy4Life?", "2018-1-25", "16:34:27", False, False, 4]]

        # cid, uid, pdate, ptime
        self.participants = [[1, 1, "2018-1-15", "16:02:13"], [1, 4, "2018-1-15", "16:02:13"],
                             [1, 5, "2018-1-17", "13:14:54"], [2, 3, "2018-1-10", "06:04:13"],
                             [2, 2, "2018-1-10", "06:04:13"], [3, 6, "2018-1-20", "12:43:41"],
                             [3, 2, "2018-1-20", "12:43:41"], [3, 3, "2018-1-20", "12:43:41"],
                             [4, 4, "2018-1-25", "16:34:27"], [4, 2, "2018-1-25", "16:34:27"]]

        # mid, text, cdate, ctime, cid, uid, isdeleted, rid
        self.messages = [[1, "Hey", "2018-1-20", "16:43:41", 3, 6, True, None],
                         [2, "Whats Up?", "2018-1-20", "16:44:41", 3, 2, True, None],
                         [3, "OMG Look at this Vid!!!", "2018-1-20", "16:45:41", 3, 3, True, None],
                         [4, "Wow!!!!! #MindBlowing", "2018-1-20", "16:46:41", 3, 2, True, 3],
                         [5, "More like ew! #WTF", "2018-1-20", "16:47:41", 3, 6, True, 3],
                         [6, "Yo Dudes!", "2018-1-17", "15:32:13", 1, 1, False, None],
                         [7, "Hey Man wanna go to the gym?", "2018-1-17", "15:33:13", 1, 5, False, None],
                         [8, "Already went, look at my ripped muscles Pic!!!", "2018-1-17", "15:34:13", 1, 4, False, None],
                         [9, "Nouce Dude! #DoYouEvenLift?", "2018-1-17", "15:35:13", 1, 5, False, 8],
                         [10, "Hey wanna go out 2nite?", "2018-1-25", "16:35:27", 4, 1, True, None],
                         [11, "Hey!!!", "2018-1-10", "08:13:45", 2, 3, False, None],
                         [12, "YO", "2018-1-10", "08:17:45", 2, 2, True, None]]

        # hashtag, mid
        self.topic = [["mindblowing", 4], ["wtf", 5], ["doyouevenlift?", 9]]

        # uid, mid, rdate, rtime, vote
        self.reacted = [[2, 3, "2018-1-20", "16:46:31", 1],
                        [6, 3, "2018-1-20", "16:47:28", -1],
                        [1, 8, "2018-1-17", "15:34:53", 1]]

        # mid, mediaid, isVideo, location
        self.media = [[3, 1, True, "c://localhost/videos/weirdVid.mov"],
                      [9, 2, False, "c://localhost/photo/muscle.jpeg"]]
    def getAllChats(self):
       #This method will return all the chats
        return self.chat[0:4]

    def getChatMessages(self,cID):
       #TODO THis method will return the messafes on a determined chat
        if cID == 1:
            return self.messages[5:10]
        if cID == 2:
            return self.messages[10:13]
        if cID == 3:
            return self.messages[0:6]
        if cID == 4:
            return self.messages[]

    def geActivetChatMessages(self,cID,isDeleted):
       #This method will only return all the messages in all the active single chats
       #Wether they are deleted or not
        if cID == 2 and not isDeleted:
           return self.messages[11]
        if cID == 2 and isDeleted:
            return self.messages[11]

    def getNonActiveChatMessages(self, cID,isDeleted):
        #This method will return all the messages in single chats that are inactive
        #There is no example of a not deleted message on a inactive chat!!!!!!!!!
        if cID == 4 and isDeleted:
            return self.messages[9]
        return[]

    def getActiveGroupChatMessages(self,cID,isDeleted):
        #This method will give all the messages on a group chat, deleted or not
        if cID == 1 and isDeleted:
            return[]
        elif cID == 1 and not isDeleted:
            return self.messages[5:9]
        return[]

    def getNonActiveGroupChatMessages(self,cID,isDeleted):
        if cID == 3 and isDeleted:
            return self.messages[0:5]
        return[]

    def getActiveChatMessagesBetween(self,cID,isGroup,isDeleted,bDate,aDate):
        #This method will return the messages in a chat between established the
        #dates of group/single chat and deleted/notDeleted messages

        bDate = [int(bDate[0:4]), int(bDate[5:7]), int(bDate[8:10])]
        aDate = [int(aDate[0:4]), int(aDate[5:7]), int(aDate[8:10])]

        if cID == 1 and isGroup and not isDeleted:
            if bDate[0] <=2018 and bDate[1] <=1 and bDate[2] <= 17 and aDate[0]>=2018 and aDate[1]>=1 and aDate[2]>=17:
                return self.messages[5:9]
            return []
        if cID == 2 and isGroup and isDeleted:
            if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[2] >= 10:
                return self.messages[11]
            return[]

        if cID == 2 and not isGroup and not isDeleted:
            if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[2] >= 10:
                return self.messages[10]
            return[]


    def getNonActiveChatMessagesBeteween(self,cID,isGroup,isDeleted,bDate,aDate):
        # This method will return the messages in a non-active chat between the established the
        # dates of group/single chat and deleted/notDeleted messages

        bDate = [int(bDate[0:4]), int(bDate[5:7]), int(bDate[8:10])]
        aDate = [int(aDate[0:4]), int(aDate[5:7]), int(aDate[8:10])]

        if cID == 3 and isGroup and isDeleted:
            if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[2] >= 20:
                return self.messages[0:5]
            return[]
        if cID == 4 and not isGroup and isDeleted:
            if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[2] >= 20:
                return self.messages[9]
            return[]

    def getChatParticipant(self,cID):
        #THis method will return the active participants of a specified chat ( active or nonactive chat)
         if cID == 1:
            return self.participants[0:3]
         elif cID == 2:
            return self.participants[3:5]
         elif cID == 3:
             return self.participants[5:8]
         elif cID == 4:
             return self.participants[8:10]
         return[]

    def getChatActivePartipant(self,cID):
        #This method will give the active participants in a desired chat
        if cID == 1:
            return self.participants[0:3]
        elif cID == 2:
            return self.participants[3:5]
        elif cID == 3:
            return self.participants[6:8]
        elif cID == 4:
            return self.participants[9]
        return[]

    def getChatNonActiveParticipant(self,cID):
      #THis method will return the non active users in a certain chat
        if cID == 1:
            return[]
        if cID == 2:
            return[]
        if cID == 3:
            return self.participants[5]
        if cID == 4:
            return self.participants[8]
        return[]

    def getChatInfo(self,cID):
        #This method will return the information of a desired chat
        if cID == 1:
            return self.chat[0]
        if cID == 2:
            return self.chat[1]
        if cID == 3:
            return self.chat[2]
        if cID == 4:
            return self.chat[3]

    def getChatTopic(self,cID):
        #This method will return the topics of a active chat
        if cID == 1:
            return self.topic[2]
        if cID == 3:
            return self.topic[0,2]
        return[]

    def getChatMedia(self,cID):
        #THis method will return the media sended in that determined chat
        if cID == 1:
            return self.media[2]
        if cID == 3:
            return self.media[1]
        return[]

    def getChatReactions(self,cID):
        #It will return the reactions based on the chat
        if cID == 3:
            return self.reacted[0,2]
        if cID == 1:
            return self.reacted[3]
        return[]

    def getChatRepliedMessages(self,cID):
        #THis method will give the list of replied messages in a determined chat
        if cID == 3:
            return self.messages[5:6]
        elif cID == 1:
            return self.messages[10]
        return[]

    def getChatMessagesRepliedWithMedia(self,cID):
        #This method is supposed to return the messages that contain a media
        #and at the same time is being replied, and viceversa
        if cID == 3:
            return self.messages[5:6]
        if cID == 1:
            return self.messages[10]
        return[]

    def getChatMessageWithReplyAndReaction(self,cID):
        #This method will select the messages in a defined chat that have reaction and reply
        if cID == 3:
            return self.messages[4]
        if cID == 1:
            return self.messages[9]
        return[]
    def getChatMessagesWithReplyReactionMedia(self,cID):
        #This method will return the messages on a desired chat that have reaction,media and reply
        if cID == 3:
            return self.messages[4]
        return[]

    def getChatTopicsBetween(self,cID,bDate,aDate):
        #This method will return the messages on a desired chat that have media
        #between the stablished dates, regardless if there is a Active or non-Active chat
        bDate = [int(bDate[0:4]), int(bDate[5:7]), int(bDate[8:10])]
        aDate = [int(aDate[0:4]), int(aDate[5:7]), int(aDate[8:10])]

        if cID == 3:
            if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[2] >= 20:
                return self.messages[5:6]

        if cID == 1:
            if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[2] >= 17:
                return[10]
        return[]

    def getChatReactionsBetween(self,cID,bDate,aDate):
        #This method will return the reactions of a chat between a determined date
        bDate = [int(bDate[0:4]), int(bDate[5:7]), int(bDate[8:10])]
        aDate = [int(aDate[0:4]), int(aDate[5:7]), int(aDate[8:10])]
        if cID == 3:
            if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[ 2] >= 20:
                return self.reacted[0, 2]
        if cID == 1:
            if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[ 2] >= 17:
                 return self.reacted[3]
        return []

    def getChatRepliedMessagesBetween(self,cID,bDate,aDate):
        #THis method will give the replies in a chat between a determined date
        bDate = [int(bDate[0:4]), int(bDate[5:7]), int(bDate[8:10])]
        aDate = [int(aDate[0:4]), int(aDate[5:7]), int(aDate[8:10])]
        if cID == 3:
            if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[ 2] >= 20:
                 return self.messages[5:6]
        elif cID == 1:
            if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[ 2] >= 17:
             return self.messages[10]
        return []

    def getChatMessagesRepliedWithMediaBetween(self,cID,bDate,aDate):
        #This method is supposed to return the messages that contain a media
        #and at the same time is being replied, and viceversa between a specified date
        bDate = [int(bDate[0:4]), int(bDate[5:7]), int(bDate[8:10])]
        aDate = [int(aDate[0:4]), int(aDate[5:7]), int(aDate[8:10])]
        if cID == 3:
            if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[ 2] >= 20:
                return self.messages[5:6]
        if cID == 1:
            if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[ 2] >= 17:
                return self.messages[10]
        return[]


    def getChatMessageWithReplyAndReactionBetween(self,cID,bDate,aDate):
        #This method will select the messages in a defined chat that have reaction and reply between a specified date
        bDate = [int(bDate[0:4]), int(bDate[5:7]), int(bDate[8:10])]
        aDate = [int(aDate[0:4]), int(aDate[5:7]), int(aDate[8:10])]
        if cID == 3:
            if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[ 2] >= 20:
                return self.messages[4]
        if cID == 1:
            if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[ 2] >= 17:
                return self.messages[9]
        return[]
    def getChatMessagesWithReplyReactionMediaBetween(self,cID,bDate,aDate):
        #This method will return the messages on a desired chat that have reaction,media and reply between a date
        bDate = [int(bDate[0:4]), int(bDate[5:7]), int(bDate[8:10])]
        aDate = [int(aDate[0:4]), int(aDate[5:7]), int(aDate[8:10])]
        if cID == 3:
            if bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 20 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[ 2] >= 20:
                return self.messages[4]
        return[]

    def getChatWithMedia(self,mID):
        #THis method will return the chat on which determined media is located in
        if mID == 1:
            return self.chat[4]
        if mID == 2:
            return self.chat[2]
        return[]

    def getChatByTopic(self,hashtag):
        #This method will return the chat on which the hashtag was seneded
        if hashtag == 'mindblowing':
            return self.chat[4]
        if hashtag == 'doyouevenlift?':
            return self.chat[2]
        if hashtag == 'wtf':
            return self.chat[4]
        return[]

    def getChatOriginalMessages(self,cID):
        #THis method will return the messages that have been replied in a determined chat
        if cID == 3:
            return self.messages[5:6]
        if cID == 1:
            return self.messages[10]
        return[]
    def getLikedMessagesByChat(self,cID):
        #This method will return the liked messages on a determined chat
        if cID == 3:
            return self.messages[4]
        if cID == 1:
            return self.messages[9]
        return[]
    def getUnlikedMessagesByChat(self,cID):
        #This method will return the unliked messages in a determined chat
        if cID == 3:
            return self.messages[4]
        return[]

    def getChatByID(self,cID):
        #This method will return the chat given its ID
        #I THINK we should get a chat by NAME instead of by chatID
        if cID == 1:
            return self.chat[2]
        if cID == 2:
            return self.chat[3]
        if cID == 3:
            return self.chat[4]
        if cID == 4:
            return self.chat[5]
        return[]

    def getChatDeleted(self):
        #This method will return the deleted chats
        return [self.chat[3], self.chat[5]]


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

