"""
This Class contain DAO methods for the entities of Chats and Participants
"""
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
        return self.chat[0:4]

    def getChatByUserID(self, uID):
        # This method will return the chats on which that user is in
        if uID == 1:
            return [self.chat[2]]
        if uID == 2:
            return self.chat[1:4]
        if uID == 3:
            return []
        if uID == 4:
            return [self.chat[3], self.chat[0]]
        if uID == 5:
            return [self.chat[2]]
        if uID == 6:
            return []
        return []

    def getAllParticipants(self):
        # This method will give all the participants in the application
        return self.participants

    def getChatParticipants(self,cID):
        # THis method will return the active participants of a specified chat ( active or nonactive chat)
        if cID == 1:
            return self.participants[0:3]
        elif cID == 2:
            return self.participants[3:5]
        elif cID == 3:
            return self.participants[5:8]
        elif cID == 4:
            return self.participants[8:10]
        return []

    def getChatActivePartipants(self,cID):
        # This method will give the active participants in a desired chat
        if cID == 1:
            return self.participants[0:3]
        elif cID == 2:
            return self.participants[3:5]
        elif cID == 3:
            return self.participants[6:8]
        elif cID == 4:
            return [self.participants[9]]
        return []

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

