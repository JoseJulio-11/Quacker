from flask import jsonify
from DAO.UserDAO import UserDAO
from Handler import DictionaryBuilder

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
        mapped_result.append(DictionaryBuilder.build_user_dict(r))
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

def loginUser(username,password):
    user= dao.loginUser(username,password)
    if not user:
        return jsonify(Error = "Wrong username or password")
    else:
       return 