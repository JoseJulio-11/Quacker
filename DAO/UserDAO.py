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
        return self.users

    #Returns the list of all credentials
    def getAllCredentials(self):
        return self.credentials

    #Returns the list of all contacts
    def getAllContacts(self):
        return self.contacts

    #Returns the list of all activity in the app
    def getAllActivity(self):
        return self.activity

    #Returns the list of all users that are active
    def getAllUsersByActivity(self):
        activeUsers = []
        for r in self.activity:
            if r[3]:
                activeUsers.append(r)
        return activeUsers

    #Returns a list with the personal information of the user with ID uID
    def getUserInfo(self, uID):
        for r in self.users:
            if uID == r[0]:
                return r
        else:
            return []

    #Returns a list with the credentials of the user with ID uID
    def getUserCredentials(self, uID):
        for r in self.credentials:
            if uID == r[0]:
               return r
        else:
            return []

    #Returns a list with the activity of the user with ID uID
    def getUserActivity(self, uID):
       for r in self.activity:
            if uID == r[0]:
                return r
       return []

    #Returns a list with the contacts of the user with ID uID
    def getUserContacts(self, uID):
        contactList = []
        for r in self.contacts:
            if uID == r[0]:
                contactList.append(r)
        return contactList

    #Returns the list of members with ID uID that are contacts of another member.
    def getParticipationAsContact(self, uID):
        userContactOfAnotherUser = []
        for r in self.contacts:
            if uID == r[1]:
                userContactOfAnotherUser.append(r)
        return userContactOfAnotherUser

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
        # List containing user record with full name
        userRecords = []
        # List containing the user with the provided email
        desiredUser = []
        for r in self.users:
            if fName == r[1] and lName == r[2]:
                userRecords.append(r)
        for j in self.credentials:
            if uemail == j[3]:
                desiredUser.append(j)
        return desiredUser

    # Returns the user with name and phone specfied
    def getUserByNameAndPhone(self, fName, lName, uphone):
        # List containing user record with full name
        userRecords = []
        # List containing the user with the provided phone
        desiredUser = []
        for r in self.users:
            if fName == r[1] and lName == r[2]:
                userRecords.append(r)
        for j in self.credentials:
            if uphone == j[4]:
                desiredUser.append(j)
        return desiredUser

    # Returns the user with name and username specified
    def getUserByNameAndUsername(self, fName, lName, username):
        # List containing user record with full name
        userRecords = []
        # List containing the user with the provided username
        desiredUser = []
        for r in self.users:
            if fName == r[1] and lName == r[2]:
                userRecords.append(r)
        for j in self.credentials:
            if username == j[1]:
                desiredUser.append(j)
        return desiredUser

    # Returns the user with username and password specified
    def getUserByUsernameAndPassword(self, username, password):
        # List containing user record with username
        userRecord = []
        for r in self.credentials:
            if username == r[1] and password == r[2]:
                userRecord.append(r)
        return userRecord

    # Returns the user with email and password specified
    def getUserByEmailAndPassword(self, uemail, password):
        # List containing user record with full name
        userRecord = []
        for r in self.credentials:
            if uemail == r[3] and password == r[2]:
                userRecord.append(r)
        return userRecord

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