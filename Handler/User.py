from flask import jsonify, request
from DAO.UserDAO import UserDAO
class UserHandler:

    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_user_dict(r))
        return jsonify(Users = mapped_result)

    def getUserInfo(self, uID):
        dao = UserDAO()
        result = dao.getUserInfo(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_user_dict(r))
        return jsonify(UserInfo = mapped_result)

    def getUserCredentials(self, uID):
        dao = UserDAO()
        result = dao.getUserCredentials(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_credential_dict(r))
        return jsonify(UserCredentials = mapped_result)

    def getUserActivity(self, uID):
        dao = UserDAO()
        result = dao.getUserActivity(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_activity_dict(r))
        return jsonify(UserActivity = mapped_result)

    def getUserContacts(self, uID):
        dao = UserDAO()
        result = dao.getUserContacts(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_contact_dict(r))
        return jsonify(UserContacts = mapped_result)

    def getChatAsAdmin(self, uID):
        dao = UserDAO()
        result = dao.getChatsAsAdmin(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_chat_dict(r))
        return jsonify(AdminChats = mapped_result)

    def getChatAsMember(self, uID):
        dao = UserDAO()
        result = dao.getChatsAsMember(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_participants_dict(r))
        return jsonify(AdminChats=mapped_result)