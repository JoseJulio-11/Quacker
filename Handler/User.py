from flask import jsonify
from DAO.UserDAO import UserDAO
from Handler import DictionaryBuilder
import datetime

dao = UserDAO()


def getAllUsers():
    result = dao.getAllUsers()
    if not result:
        return jsonify(Error ="No Users Found")
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_user_dict(r))
    return jsonify(Users = mapped_result)


def getAllCredentials():
    result = dao.getAllCredentials()
    if not result:
        return jsonify(Error ="No Credentials Found")
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_credential_dict(r))
    return jsonify(Credentials=mapped_result)

def getAllContacts():
    result = dao.getAllContacts()
    if not result:
        return jsonify(Error="No Contacts Found")
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_contact_dict(r))
    return jsonify(Contacts=mapped_result)

def getAllActivity():
    result = dao.getAllActivity()
    if not result:
        return jsonify(Error="No Activity Found")
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_activity_dict(r))
    return jsonify(Activity=mapped_result)

def getUserInfo(uID):
    result = dao.getUserInfo(uID)
    if not result:
        return jsonify(Error ="No User Found")
    result = DictionaryBuilder.build_user_dict(result)
    return jsonify(UserInfo = result)

def getUserCredentials(uID):
    result = dao.getUserCredentials(uID)
    if not result:
        return jsonify(Error = "No Credentials Found")
    result = DictionaryBuilder.build_credential_dict(result)
    return jsonify(UserCredentials = result)

def getUserActivity(uID):
    result = dao.getUserActivity(uID)
    if not result:
        return jsonify(Error = "No Activity Found")
    result = DictionaryBuilder.build_activity_dict(result)
    return jsonify(UserActivity = result)

def getUserContacts(uID):
    result = dao.getUserContacts(uID)
    if not result:
        return jsonify(Error = "No Contacts Found")
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_contact_dict(r))
    return jsonify(UserContacts = mapped_result)

def getActiveUsers():
    result = dao.getAllUsersByActivity()
    if not result:
        return jsonify(Error="No Active Users Found")
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_user_dict(r))
    return jsonify(ActiveUsers=mapped_result)

def getUsersCreatedBetween(bDate, aDate):
    result = dao.getUsersCreatedBetween(bDate,aDate)
    if not result:
        return jsonify(Error = "No Users Found")
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_user_dict(r))
    return jsonify(UserCreated = mapped_result)

def getUserByNameAndUsername(fName, lName, username):
    result = dao.getUserByNameAndUsername(fName, lName, username)
    if not result:
        return jsonify(Error = "No User Found")
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_credential_dict(r))
    return jsonify(Users = mapped_result)

def getUserByNameAndPhone(fName, lName, phone):
    result = dao.getUserByNameAndPhone(fName, lName, phone)
    if not result:
        return jsonify(Error = "No User Found")
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_credential_dict(r))
    return jsonify(Users = mapped_result)

def getUserByNameAndEmail(fName, lName, uemail):
    result = dao.getUserByNameAndEmail(fName, lName, uemail)
    if not result:
        return jsonify(Error="No User Found")
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_credential_dict(r))
    return jsonify(Users = mapped_result)


def getUserByEmailAndPassword(uemail, password):
    result = dao.getUserByEmailAndPassword(uemail, password)
    if not result:
        return jsonify(Error="No User Found")
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_credential_dict(r))
    return jsonify(Users = mapped_result)

def getUsersByLikedMessage(mid):
    result = dao.getUsersByLikedMessage(mid)
    if not result:
        return jsonify(Error="No Users Found")
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_reacted_user_dict(r))
    return jsonify(Users = mapped_result)

def getUsersByDislikedMessage(mid):
    result = dao.getUsersByDislikedMessage(mid)
    if not result:
        return jsonify(Error = "No Users Found")
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_user_dict(r))
    return jsonify(Users = mapped_result)

def getMembersByChatID(cid):
    result = dao.getMembersByChatID(cid)
    if not result:
        return jsonify(Error = "No Members Found")
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_user_dict(r))
    return jsonify(Users = mapped_result)

def getAdminByChatID(cid):
    result = dao.getAdminByChatID(cid)
    if not result:
        return jsonify(Error = "No Admin Found")
    mapped_result = DictionaryBuilder.build_user_dict(result)
    return jsonify(Users = mapped_result)


def searchAllUser(json):
    if len(json) != 3:
        return jsonify(Error = " Malformed post request, missing or extra data")
    else:
        fname = json['fname']
        lname = json['lname']
        search = json['search']
        result = dao.searchAllUsers(fname, lname, search)
        if not result:
            return jsonify(Error="No Active Users Found")
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_user_dict(r))
        return jsonify(Users = mapped_result)


def searchAllContact(uid, json):
    if len(json) != 3:
        return jsonify(Error = " Malformed post request, missing or extra data")
    else:
        fname = json['fname']
        lname = json['lname']
        search = json['search']
        result = dao.searchAllContact(uid, fname, lname, search)
        if not result:
            return jsonify(Error="No Active Users Found")
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_user_dict(r))
        return jsonify(Users = mapped_result)


def getUsersPerDay():
    today = datetime.datetime.now()
    weekBefore = today - datetime.timedelta(days=6)
    oneDay = datetime.timedelta(days=1)
    userperday = dict()
    userperday['1'] = usersPerDayHelper(weekBefore, oneDay)
    userperday['2'] = usersPerDayHelper(weekBefore+oneDay, oneDay)
    userperday['3'] = usersPerDayHelper(weekBefore+oneDay+oneDay, oneDay)
    userperday['4'] = usersPerDayHelper(weekBefore+oneDay+oneDay+oneDay, oneDay)
    userperday['5'] = usersPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay, oneDay)
    userperday['6'] = usersPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay+oneDay, oneDay)
    userperday['7'] = usersPerDayHelper(weekBefore+oneDay+oneDay+oneDay+oneDay+oneDay+oneDay, oneDay)
    return jsonify(Users=userperday)


def usersPerDayHelper(day, oneday):
    usersinday = []
    topics = dao.getUsersPerDay(day - oneday, day)
    for row in topics:
        result = DictionaryBuilder.build_dash_user_dict(row)
        print(result)
        usersinday.append(result)
    return usersinday


def loginUser(json):
    username = json['username']
    print(username)
    password = json['password']
    print(password)

    if username and password:
        user = dao.loginUser(username, password)
        if user:
            return jsonify(User=user)
        else:
            return jsonify(Error="Wrong username or password")

    else:
        return jsonify(Error="Wrong username or password")

def addUser(json):
    #This method adds a need user of the app to the system
    if len(json)!= 7:
        return jsonify(Error="Missing information for registration")
    else:
        fname = json['fname']
        lname = json['lname']
        pseudonym = json['pseudonym']
        username = json['username']
        password = json['password']
        uemail = json['uemail']
        uphone = json['uphone']

        if fname and lname and pseudonym and username and password and uemail and uphone:
            test = dao.getUserByUsernameOrEmail(username, uemail)
            if test:
                return jsonify(Error= 'User already exists.' )
            uid = dao.addUser(fname,lname,pseudonym)
            void = dao.addCredentials(uid, username, password, uemail, uphone)
            utime = dao.addActivity(uid)
            if uid:
                result = DictionaryBuilder.build_user_dict([uid, fname, lname, utime, pseudonym])
                return jsonify(User = result)
            else:
                return jsonify(Error = 'InsertFailed')
        else:
            return jsonify(Error='Unexpected attributes in post request'), 400

def addContact(json):
    #This method will add a user to the contaact list of another user
    if len(json)!=2:
        return jsonify(Error="Missing or extra information given")
    else:
        uid = json['uid']
        newContact = json['memberid']

        if uid and newContact:
            uid = dao.addContact(uid, newContact)
            if uid:
                return jsonify(Success="Contact Added")
            else:
                return jsonify(Error="Contact already added")
        else:
            return jsonify(Error="Wrong information given")