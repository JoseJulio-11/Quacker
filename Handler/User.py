from flask import jsonify, request
from DAO.UserDAO import ReadUserDAO
class UserHandler:

    def getAllUsers(self):
        dao = ReadUserDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_user_dict(r))
        return jsonify(Users = mapped_result)

    def getUserInfo(self, uID):
        dao = ReadUserDAO()
        result = dao.getUserInfo(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_user_dict(r))
        return jsonify(UserInfo = mapped_result)

    def getUserCredentials(self, uID):
        dao = ReadUserDAO()
        result = dao.getUserCredentials(uID)
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_credential_dict(r))
        return jsonify(UserCredentials = mapped_result)

    def get