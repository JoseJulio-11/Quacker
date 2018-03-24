
class UpdateDAO:

    def __init__(self):
        print('alejandra')

    def updateUser(self, uID, fName, lName, ctime,cdate,pseudonym):
        return uID
        #the user has the option of updating its own information


    def updateChat(self,cID,cName, cDate,cTime,adminID):
        return cID
         # This method is supposed to change the name of the chat,
         # delete the chat by the admid
         # the chat will be sta


    def updateCredential(self,uID,username,password,uemail,uphone):
        return uID
        #the user can edit its credential when needed


    def updateAtive(self,aid,isActive,lasDbAccessDate,lastDbAccessTime,uID):
        return isActive
        # After 30 days of last time active in the app the user  will be stablish as
        # inactive


    def updateParticipant(self,cID,uID,pdate,ptime,):
        return uID,cID
        # the user can abandone a group chat that its part of
        # the admi of the group can remove a user from that group chat

    def updateReacted(self,uID,mID,rdate,rtime,vote):
        return vote,mID
        #It will change the reaction of the messege, 0 not reacted,1 liked,
        # -1 disliked


    def updateMedia(self,mID,medID,isVideo,location):
        return mID,medID
        #the user can delete a media messege sent by him/her


    def updateMessege(self,mID,text,cdate,ctime,uid,cid,isDeleted,rid):
        return  mID
        #it will update a messege by saying if it deleted or not