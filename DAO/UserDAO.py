"""
This Class contain DAO methods for the entities of Users, Activities, Credentials and Contacts
"""
from pg_config import pg_config
import psycopg2
class UserDAO:


    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    # ============================== Create Methods =========================== #
    def insertUser(self, fName, lName, ctime, cdate, pseudonym):
        # Create a new user
        uID = 7
        return uID

    def insertCredential(self, uID, username, password, uemail, cuphone):
        # Create credentials for user
        return uID, username

    def insertActivity(self, isActive, lasDbAccessDate, lastDbAccessTime, uID):
        # Create activity for user
        aid = uID
        return aid

    def insertContact(self, ownerid, memberid):
        #Create contacts for user
        return ownerid, memberid

    # =================================== Read Methods =============================== #
    #Returns the list of all users
    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Returns the list of all credentials
    def getAllCredentials(self):
        cursor = self.conn.cursor()
        query = "select * from credentials;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Returns the list of all contacts
    def getAllContacts(self):
        cursor = self.conn.cursor()
        query = "select * from contacts;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Returns the list of all activity in the app
    def getAllActivity(self):
        cursor = self.conn.cursor()
        query = "select * from activities;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Returns the list of all users that are active
    def getAllUsersByActivity(self):
        cursor = self.conn.cursor()
        query = "select uid from activities where isactive = 't';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Returns a list with the personal information of the user with ID uID
    def getUserInfo(self, uID):
        cursor = self.conn.cursor()
        query = "select * from users where uid = %s;"
        cursor.execute(query, (uID,))
        result = cursor.fetchone()
        return result

    #Returns a list with the credentials of the user with ID uID
    def getUserCredentials(self, uID):
        cursor = self.conn.cursor()
        query = "select * from credentials where uid = %s;"
        cursor.execute(query, (uID,))
        result = cursor.fetchone()
        return result

    #Returns a list with the activity of the user with ID uID
    def getUserActivity(self, uID):
        cursor = self.conn.cursor()
        query = "select * from activities where uid = %s;"
        cursor.execute(query, (uID,))
        result = cursor.fetchone()
        return result

    #Returns a list with the contacts of the user with ID uID
    def getUserContacts(self, uID):
        cursor = self.conn.cursor()
        query = "select memberid from contacts where uid = %s;"
        cursor.execute(query, (uID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Returns the list of members with ID uID that are contacts of another member.
    def getParticipationAsContact(self, uID):
        cursor = self.conn.cursor()
        query = "select uid from contacts where memberid = %s;"
        cursor.execute(query, (uID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Returns the list of all users created between the provided dates
    def getUsersCreatedBetween(self, bDate, aDate):
        bDate = [int(bDate[0:4]), int(bDate[5:7]), int(bDate[8:10])]
        aDate = [int(aDate[0:4]), int(aDate[5:7]), int(aDate[8:10])]
        if bDate[0] <=2018 and bDate[1] <=1 and bDate[2] <=1 and aDate[0] >=2018 and aDate[1]>=1 and aDate[2]>=1:
            return [self.users[0], self.users[1]]
        elif bDate[0] <= 2018 and bDate[1] <= 1 and bDate[2] <= 5 and aDate[0] >= 2018 and aDate[1] >= 1 and aDate[2] >= 5:
            return [self.users[2]]
        elif bDate[0] <= 2018 and bDate[1] <= 2 and bDate[2] <= 1 and aDate[0] >= 2018 and aDate[1] >= 2 and aDate[2] >= 1:
            return [self.users[3]]
        elif bDate[0] <= 2017 and bDate[1] <= 12 and bDate[2] <= 31 and aDate[0] >= 2017 and aDate[1] >= 12 and aDate[2] >= 31:
            return [self.users[4]]
        elif bDate[0] <= 2017 and bDate[1] <= 1 and bDate[2] <= 1 and aDate[0] >= 2017 and aDate[1] >= 1 and aDate[2] >= 1:
            return [self.users[5]]
        else:
            return []

    # Returns the user with name and email specified
    def getUserByNameAndEmail(self, fName, lName, uemail):
        cursor = self.conn.cursor()
        query = "select uid from users natural inner join credentials where fname = %s AND lname = %s AND uemail = %s;"
        cursor.execute(query, (fName, lName, uemail))
        result = cursor.fetchone()
        return result

    # Returns the user with name and phone specfied
    def getUserByNameAndPhone(self, fName, lName, uphone):
        cursor = self.conn.cursor()
        query = "select uid from users natural inner join credentials where fname = %s AND lname = %s AND uphone = %s;"
        cursor.execute(query, (fName, lName, uphone))
        result = cursor.fetchone()
        return result

    # Returns the user with name and username specified
    def getUserByNameAndUsername(self, fName, lName, username):
        cursor = self.conn.cursor()
        query = "select uid from users natural inner join credentials where fname = %s AND lname = %s AND username = %s;"
        cursor.execute(query, (fName, lName, username))
        result = cursor.fetchone()
        return result

    # Returns the user with username and password specified
    def getUserByUsernameAndPassword(self, username, password):
        cursor = self.conn.cursor()
        query = "select uid from credentials where username = %s AND password = %s;"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        return result

    # Returns the user with email and password specified
    def getUserByEmailAndPassword(self, uemail, password):
        cursor = self.conn.cursor()
        query = "select uid from credentials where uemail = %s AND password = %s;"
        cursor.execute(query, (uemail, password))
        result = cursor.fetchone()
        return result

    # Returns the users who liked the message with ID mid
    def getUsersByLikedMessage(self, mid):
        cursor = self.conn.cursor()
        query = "select uid from reacted where mid = %s AND vote = %s;"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Returns the users who disliked the message with ID mid
    def getUsersByDislikedMessage(self, mid):
        cursor = self.conn.cursor()
        query = "select uid from reacted where mid = %s AND vote = %s;"
        cursor.execute(query, (mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Returns the users that are members of the chat with ID cid
    def getMembersByChatID(self, cid):
        cursor = self.conn.cursor()
        query = "select uid from participants where cid = %s;"
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Returns the user that is admin of the chat with ID cid
    def getAdminByChatID(self, cid):
        cursor = self.conn.cursor()
        query = "select uid from chats where cid = %s;"
        cursor.execute(query, (cid,))
        result = cursor.fetchone()
        return result

    # =========================== Update Methods ================================= #
    def updateUser(self, uID, fName, lName, ctime, cdate, pseudonym):
        # the user has the option of updating its own information
        return uID

    def updateCredential(self, uID, username, password, uemail, cuphone):
        # the user can edit its credential when needed
        return uID, username

    def updateActivity(self, aid, isActive, lasDbAccessDate, lastDbAccessTime):
        # This method is used to update the user last db access
        # After 30 days of last time active in the app the user will be establish as inactive
        # Also if the user decides to close the account it will be set to false
        return aid

    def updateContact(self, uID, ownerid, memberid):
        # the user can update its contact list when needed
        return uID, ownerid, memberid

    # =================================== Delete Methods ============================= #
    def deleteUser(self, uID):
        # Remove an user from the database
        return uID

    def deleteCredential(self, uID):
        # Remove an user's credentials
        username = "stub"
        return uID, username

    def deleteActivity(self, uID):
        # Remove an user's activity
        aID = 7
        return uID, aID

    def deleteContact(self, ownerid, memberid):
        # Remove the desired contact from the contact's list.
        return ownerid, memberid