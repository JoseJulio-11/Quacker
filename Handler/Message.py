from flask import jsonify
import Handler.DictionaryBuilder as Dic
from DAO.MessagesDAO import MessagesDAO
dao = MessagesDAO()

def getMessagesByID(self, mID):
#This method return the message requested by its ID
    row = dao.getMessageInfo(mID)
    if not row:
        return jsonify(Error = " Message not found"), 404
    else:
        message = Dic.build_message_dic(row)
        return jsonify(Message = message)
def getReactionsByMessage(self,mID):
    #THis method return the reaction of a determined message
    row = dao.getMessageReaction(mID)
    if not row:
        return jsonify(Error = " Message does not contain reaction"), 404
    else:
        reaction = Dic.built_react_dic(mID)
        return jsonify(Reaction = reaction)
