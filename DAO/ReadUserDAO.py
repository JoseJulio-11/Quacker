
class ReadUserDAO:

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
                         [8, "Already went, look at my ripped muscles Pic!!!", "2018-1-17", "15:34:13", 1, 4, False,
                          None],
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

    #Returns the list of all users
    def getAllUsers(self):
        return self.users

    #Returns a list with the personal information of the user with ID uID
    def getUserInfo(self, uID):
        for r in self.users:
            if uID == r[0]:
                return r
        return []

    #Returns a list with the credentials of the user with ID uID
    def getUserCredentials(self, uID):
        for r in self.credentials:
            if uID == r[0]:
                return r
        return []

    #Returns a list with the activity of the user with ID uID
    def getUserActivity(self, uID):
        for r in self.activity:
            if uID == r[4]:
                return r
        return []

    #Returns a list with the contacts of the user with ID uID
    def getUserContacts(self, uID):
        contactList = []
        for r in self.contacts:
            if uID == r[0]:
                contactList.append(r)
        return contactList

    #Returns a list with the chats of the admin user with ID uID
    def getChatsAsAdmin(self, uID):
        adminChatsList = []
        for r in self.chat:
            if uID == r[6]:
                adminChatsList.append(r)
        return adminChatsList

    #Returns the list of all chats which the user with ID uID is member of.
    def getChatAsMember(self, uID):
        memberChatsList = []
        for r in self.participants:
            if uID == r[1]:
                memberChatsList.append(r)
        return memberChatsList

    #Returns the list of members with ID uID that are contacts of another member.
    def getParticipationAsContact(self, uID):
        if uID == 1:
            return [self.contacts[4], self.contacts[6]]
        elif uID == 2:
            return [self.contacts[0],self.contacts[3], self.contacts[5]]
        elif uID == 3:
            return self.contacts[9]
        elif uID == 4:
            return self.contacts[1]
        elif uID == 5:
            return self.contacts[2]
        else:
            return []

    #Returns the list of reactions between the
    #date and time specified of the user with ID uID
    def getUserReactionsBetween(self, uID, bDate, aDate):
        bDate = [int(bDate[0:4]), int(bDate[5:7]), int(bDate[8:10])]
        aDate = [int(aDate[0:4]), int(aDate[5:7]), int(aDate[8:10])]
        if uID == 2 and bDate[0] <=2018 and bDate[1] <=1 and bDate[2] <=20 and aDate[0] >=2018 and aDate[1]>=1 and aDate[2]>=20:
            return self.reacted[0]
        elif uID == 6 and bDate[0] <=2018 and bDate[1] <=1 and bDate[2] <=20 and aDate[0] >=2018 and aDate[1]>=1 and aDate[2]>=20:
            return self.reacted[1]
        elif uID == 1 and bDate[0] <=2018 and bDate[1] <=1 and bDate[2] <=17 and aDate[0] >=2018 and aDate[1]>=1 and aDate[2]>=17:
            return self.reacted[2]
        else:
            return []

    #Returns the list of messages posted by user with ID uID
    def getUserMessagesBetween(self, uID, bDate, aDate):
        bDate = [int(bDate[0:4]), int(bDate[5:7]), int(bDate[8:10])]
        aDate = [int(aDate[0:4]), int(aDate[5:7]), int(aDate[8:10])]
        if uID == 6 and bDate[0] <=2018 and bDate[1] <=1 and bDate[2] <=20 and aDate[0] >=2018 and aDate[1]>=1 and aDate[2]>=20:
            return [self.reacted[0], self.reacted[4]]
        elif uID == 2 and bDate[0] <=2018 and bDate[1] <=1 and bDate[2] <=20 and aDate[0] >=2018 and aDate[1]>=1 and aDate[2]>=20:
            return [self.reacted[1], self.reacted[3]]
        elif uID == 2 and bDate[0] <=2018 and bDate[1] <=1 and bDate[2] <=10 and aDate[0] >=2018 and aDate[1]>=1 and aDate[2]>=10:
            return self.reacted[11]
        elif uID == 3 and bDate[0] <=2018 and bDate[1] <=1 and bDate[2] <=10 and aDate[0] >=2018 and aDate[1]>=1 and aDate[2]>=10:
            return self.reacted[10]
        elif uID == 3 and bDate[0] <=2018 and bDate[1] <=1 and bDate[2] <=20 and aDate[0] >=2018 and aDate[1]>=1 and aDate[2]>=20:
            return self.reacted[2]
        elif uID == 1 and bDate[0] <=2018 and bDate[1] <=1 and bDate[2] <=17 and aDate[0] >=2018 and aDate[1]>=1 and aDate[2]>=17:
            return [self.reacted[5], self.reacted[9]]
        elif uID == 5 and bDate[0] <=2018 and bDate[1] <=1 and bDate[2] <=17 and aDate[0] >=2018 and aDate[1]>=1 and aDate[2]>=17:
            return [self.reacted[6], self.reacted[8]]
        elif uID == 4 and bDate[0] <=2018 and bDate[1] <=1 and bDate[2] <=17 and aDate[0] >=2018 and aDate[1]>=1 and aDate[2]>=17:
            return self.reacted[7]
        else:
            return []

    #Returns the list of all active users
    def getActiveUser(self):
        activeUsersList = []
        for r in self.activity:
            if r[3]:
                activeUsersList.append(r)
        return activeUsersList

    #Returns the list of all users created between the provided dates
    def getUsersCreatedBetween(self, bDate, aDate):
        bDate = [int(bDate[0:4]), int(bDate[5:7]), int(bDate[8:10])]
        aDate = [int(aDate[0:4]), int(aDate[5:7]), int(aDate[8:10])]
        if bDate[0] <=2018 and bDate[1] <=1 and bDate[2] <=1 and aDate[0] >=2018 and aDate[1]>=1 and aDate[2]>=1:
            return [self.users[0], self.users[1]]
        elif bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 5 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[2] >= 5:
            return self.users[2]
        elif bDate[0] <= 2018 and bDate[1] <= 2 and bDate[2] <= 1 and aDate[0] >= 2018 and aDate[1] >= 2 and aDate[2] >= 1:
            return self.users[3]
        elif bDate[0] <= 2017 and bDate[1] <= 12 and bDate[2] <= 31 and aDate[0] >= 2017 and aDate[1] >= 12 and aDate[2] >= 31:
            return self.users[4]
        elif bDate[0] <= 2017 and bDate[1] <= 1 and bDate[2] <= 1 and aDate[0] >= 2017 and aDate[1] >= 1 and aDate[2] >= 1:
            return self.users[5]
        else:
            return []


    #Returns the list of topics posted by the user with ID uID
    def getUserTopicsBetween(self, uID, bDate, aDate):
        messagesList = []
        bDate = [int(bDate[0:4]), int(bDate[5:7]), int(bDate[8:10])]
        aDate = [int(aDate[0:4]), int(aDate[5:7]), int(aDate[8:10])]
        for r in self.messages:
            if uID == r[5]:
                messagesList.append(r)
        if messagesList[0] == 5 and bDate[0] <=2018 and bDate[1] <=1 and bDate[2] <=20 and aDate[0] >=2018 and aDate >=1 and aDate >=20:
            return self.topic[1]
        elif messagesList[0] == 4 and bDate[0] <=2018 and bDate[1] <=1 and bDate[2] <=20 and aDate[0] >=2018 and aDate >=1 and aDate >=20:
            return self.topic[0]
        elif messagesList[0] == 9 and bDate[0] <=2018 and bDate[1] <=1 and bDate[2] <=17 and aDate[0] >=2018 and aDate >=1 and aDate >=17:
            return self.topic[2]
        else:
            return []









