def build_user_dict(userInfo):
    # UID, FNAME, LNAME, CDATE, CTIME, PSEUDONYM
    user = {}
    user["uID"] = userInfo[0]
    user["fName"] = userInfo[1]
    user["lName"] = userInfo[2]
    user["cDate"] = userInfo[3]
    user["cTime"] = userInfo[4]
    user["pseudonym"] = userInfo[5]
    return user

def build_credential_dict(userCredential):
    # UID, Username, Password, UEmail, UPhone
    cred = {}
    cred["uID"] = userCredential[0]
    cred["username"] = userCredential[1]
    cred["password"] = userCredential[2]
    cred["uEmail"] = userCredential[3]
    cred["uPhone"] = userCredential[4]
    return cred

def build_activity_dict(userActicity):
    # AID, lastAccessToDBDate, lastAccessToDBTime, isActive
    activity = {}
    activity["aID"] = userActicity[0]
    activity["lastDBAccessDate"] = userActicity[1]
    activity["lastDBAccessTime"] = userActicity[2]
    activity["isActive"] = userActicity[3]
    return activity

def build_contact_dict(userContact):
    # ownerid, memberid
    contact = {}
    contact["ownerID"] = userContact[0]
    contact["memberID"] = userContact[1]
    return contact

def build_chat_dict(chat):
    # cid, cname, cdate, ctime, isgroupchat, isactive, adminid
    chatRecord = {}
    chatRecord["cID"] = chat[0]
    chatRecord["cName"] = chat[1]
    chatRecord["cDate"] = chat[2]
    chatRecord["cTime"] = chat[3]
    chatRecord["isGroupChat"] = chat[4]
    chatRecord["isActive"] = chat[5]
    chatRecord["adminID"] = chat[6]
    return chatRecord

def build_participants_dict(chatParticipant):
    # cid, uid, pdate, ptime
    participant = {}
    participant["cID"] = chatParticipant[0]
    participant["uID"] = chatParticipant[1]
    participant["pDate"] = chatParticipant[2]
    participant["pTime"] = chatParticipant[3]
    return participant

def build_message_dict(chatMessage):
    # mid, text, cdate, ctime, cid, uid, isdeleted, rid
    Message = {}
    Message["mID"] = chatMessage[0]
    Message["text"] = chatMessage[1]
    Message["cDate"] = chatMessage[2]
    Message["cTime"] = chatMessage[3]
    Message["cID"] = chatMessage[4]
    Message["uID"] = chatMessage[5]
    Message["isDeleted"] = chatMessage[6]
    Message["rID"] = chatMessage[7]
    return Message

def build_reacted_dict(messageReaction):
    # uid, mid, rdate, rtime, vote
    reaction = {}
    reaction["uID"] = messageReaction[0]
    reaction["mID"] = messageReaction[1]
    reaction["rDate"] = messageReaction[2]
    reaction["rTime"] = messageReaction[3]
    reaction["vote"] = messageReaction[4]
    return reaction

def build_topic_dict(messageTopic):
    # hashtag, mid
    topic = {}
    topic["hashtag"] = messageTopic[0]
    topic["mID"] = messageTopic[1]
    return topic

def build_media_dict(messageMedia):
    # mid, mediaid, isVideo, location
    media = {}
    media["mID"] = messageMedia[0]
    media["mediaID"] = messageMedia[1]
    media["rDate"] = messageMedia[2]
    media["rTime"] = messageMedia[3]
    return media