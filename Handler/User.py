from flask import jsonify
from DAO.UserDAO import UserDAO
from Handler import DictionaryBuilder

dao = UserDAO()


def getAllUsers():
    result = dao.getAllUsers()
    if not result:
        return jsonify(Error="No Users Found")
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_user_dict(r))
    return jsonify(Users=mapped_result)


def getAllCredentials():
    result = dao.getAllCredentials()
    if not result:
        return jsonify(Error="No Credentials Found")
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
        return jsonify(Error="No Records Found")
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_user_dict(r))
    return jsonify(UserInfo = mapped_result)


def getUserCredentials(uID):
    dao = UserDAO()
    result = dao.getUserCredentials(uID)
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_credential_dict(r))
    return jsonify(UserCredentials = mapped_result)


def getUserActivity(uID):
    dao = UserDAO()
    result = dao.getUserActivity(uID)
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_activity_dict(r))
    return jsonify(UserActivity = mapped_result)


def getUserContacts(uID):
    dao = UserDAO()
    result = dao.getUserContacts(uID)
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_contact_dict(r))
    return jsonify(UserContacts = mapped_result)


def getChatAsAdmin(uID):
    dao = UserDAO()
    result = dao.getChatsAsAdmin(uID)
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_chat_dict(r))
    return jsonify(AdminChats = mapped_result)


def getChatAsMember(uID):
    dao = UserDAO()
    result = dao.getChatAsMember(uID)
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_participants_dict(r))
    return jsonify(MemberChats=mapped_result)


def getParticipationAsContact(uID):
    dao = UserDAO()
    result = dao.getParticipationAsContact(uID)
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_contact_dict(r))
    return jsonify(MemberChats=mapped_result)


def getUserReactionsBetween(uID, bDate, aDate):
    dao = UserDAO()
    result = dao.getUserReactionsBetween(uID, bDate, aDate)
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_reacted_dict(r))
    return jsonify(UserReactions = mapped_result)


def getUserReactions(uID):
    dao = UserDAO()
    result = dao.getUserReactions(uID)
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_reacted_dict(r))
    return jsonify(UserReactions = mapped_result)


def getUserMessagesBetween(uID, bDate, aDate):
    dao = UserDAO()
    result = dao.getUserMessagesBetween(uID, bDate, aDate)
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_message_dict(r))
    return jsonify(UserMessagesBetween = mapped_result)


def getUserMessages(uID):
    dao = UserDAO()
    result = dao.getUserMessages(uID)
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_message_dict(r))
    return jsonify(UserMessages = mapped_result)


def getUserTopics(uID):
    dao = UserDAO()
    result = dao.getUserTopics(uID)
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_topic_dict(r))
    return jsonify(UserTopics = mapped_result)


def getUserTopicsBetween(uID, bDate, aDate):
    dao = UserDAO()
    result = dao.getUserTopicsBetween(uID, bDate, aDate)
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_topic_dict(r))
    return jsonify(UserTopics = mapped_result)


def getActiveUsers():
    dao = UserDAO()
    result = dao.getActiveUsers()
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_activity_dict(r))
    return jsonify(ActiveUsers = mapped_result)


def getUsersCreatedBetween(bDate, aDate):
    dao = UserDAO()
    result = dao.getUsersCreatedBetween(bDate,aDate)
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_user_dict(r))
    return jsonify(UserCreated = mapped_result)


def getUserByNameAndUsername(fName, lName, username):
    dao = UserDAO()
    result = dao.getUserByNameAndUsername(fName, lName, username)
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_credential_dict(r))
    return jsonify(Users = mapped_result)


def getUserByNameAndPhone(fName, lName, phone):
    dao = UserDAO()
    result = dao.getUserByNameAndPhone(fName, lName, phone)
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_credential_dict(r))
    return jsonify(Users = mapped_result)


def getUserByNameAndEmail(fName, lName, uemail):
    dao = UserDAO()
    result = dao.getUserByNameAndEmail(fName, lName, uemail)
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_credential_dict(r))
    return jsonify(Users = mapped_result)


def getUserByEmailAndPassword(uemail, password):
    dao = UserDAO()
    result = dao.getUserByNameAndEmail(uemail, password)
    mapped_result = []
    for r in result:
        mapped_result.append(DictionaryBuilder.build_credential_dict(r))
    return jsonify(Users = mapped_result)



