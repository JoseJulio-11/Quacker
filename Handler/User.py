from flask import jsonify, request
from DAO.UserDAO import ReadUserDAO
class UserHandler:

    def getAllUsers(self):
        dao = ReadUserDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_user_dict(r))
        return jsonify(UserDAO = mapped_result)

    def getUserInfo(self):
        dao = ReadUserDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.build_user_dict(r))
        return jsonify(UserDAO=mapped_result)