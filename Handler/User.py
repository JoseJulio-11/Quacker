from flask import jsonify, request
from DAO.UserDAO import UserDAO
from Handler.DictionaryBuilder import DictionaryBuilder
class UserHandler:

    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_user_dict(r))
        return jsonify(Users = mapped_result)

    def getAllCredentials(self):
        dao = UserDAO()
        result = dao.getAllCredentials()
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_credential_dict(r))
        return jsonify(Credentials = mapped_result)

    def getAllContacts(self):
        dao = UserDAO()
        result = dao.getAllContacts()
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_contact_dict(r))
        return jsonify(COntacts = mapped_result)

    def getUserInfo(self, uID):
        dao = UserDAO()
        result = dao.getUserInfo(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_user_dict(r))
        return jsonify(UserInfo = mapped_result)

    def getUserCredentials(self, uID):
        dao = UserDAO()
        result = dao.getUserCredentials(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_credential_dict(r))
        return jsonify(UserCredentials = mapped_result)

    def getUserActivity(self, uID):
        dao = UserDAO()
        result = dao.getUserActivity(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_activity_dict(r))
        return jsonify(UserActivity = mapped_result)

    def getUserContacts(self, uID):
        dao = UserDAO()
        result = dao.getUserContacts(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_contact_dict(r))
        return jsonify(UserContacts = mapped_result)

    def getChatAsAdmin(self, uID):
        dao = UserDAO()
        result = dao.getChatsAsAdmin(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_chat_dict(r))
        return jsonify(AdminChats = mapped_result)

    def getChatAsMember(self, uID):
        dao = UserDAO()
        result = dao.getChatAsMember(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_participants_dict(r))
        return jsonify(MemberChats=mapped_result)

    def getParticipationAsContact(self, uID):
        dao = UserDAO()
        result = dao.getParticipationAsContact(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_contact_dict(r))
        return jsonify(MemberChats=mapped_result)

    def getUserReactionsBetween(self, uID, bDate, aDate):
        dao = UserDAO()
        result = dao.getUserReactionsBetween(uID, bDate, aDate)
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_reacted_dict(r))
        return jsonify(UserReactions = mapped_result)

    def getUserReactions(self, uID):
        dao = UserDAO()
        result = dao.getUserReactions(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_reacted_dict(r))
        return jsonify(UserReactions = mapped_result)

    def getUserMessagesBetween(self, uID, bDate, aDate):
        dao = UserDAO()
        result = dao.getUserMessagesBetween(uID, bDate, aDate)
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_message_dict(r))
        return jsonify(UserMessagesBetween = mapped_result)

    def getUserMessages(self, uID):
        dao = UserDAO()
        result = dao.getUserMessages(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_message_dict(r))
        return jsonify(UserMessages = mapped_result)

    def getUserTopics(self, uID):
        dao = UserDAO()
        result = dao.getUserTopics(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_topic_dict(r))
        return jsonify(UserTopics = mapped_result)

    def getUserTopicsBetween(self, uID, bDate, aDate):
        dao = UserDAO()
        result = dao.getUserTopicsBetween(uID, bDate, aDate)
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_topic_dict(r))
        return jsonify(UserTopics = mapped_result)

    def getActiveUsers(self):
        dao = UserDAO()
        result = dao.getActiveUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_activity_dict(r))
        return jsonify(ActiveUsers = mapped_result)

    def getUsersCreatedBetween(self, bDate, aDate):
        dao = UserDAO()
        result = dao.getUsersCreatedBetween(bDate,aDate)
        mapped_result = []
        for r in result:
            mapped_result.append(DictionaryBuilder.build_user_dict(r))
        return jsonify(UserCreated = mapped_result)


