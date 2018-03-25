
class CreateDAO:
    def insertUser(self, fname, lname, ctime, cdate, pseudonym):
        cursor = self.conn.cursor()
        query = "insert into parts(fname, lname, ctime, cdate, pseudonym) values (%s, %s, %s, %s, %s) returning uid;"
        cursor.execute(query, (fname, lname, ctime, cdate, pseudonym))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def insertCredentials(self, username, password, uemail, uphone):
        cursor = self.conn.cursor()
        query = "insert into parts(username, password, uemail, uphone) values (%s, %s, %s, %s) returning pid;"
        cursor.execute(query, (username, password, uemail, password, uphone))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    def insertActive(self, isActive, lastDbAccessDate, lastDbAccessTime):
        cursor = self.conn.cursor()
        query = "insert into parts(isActive, lastDbAccessDate, lastDbAccessTime) values (%s, %s, %s) returning aid;"
        cursor.execute(query, (isActive, lastDbAccessDate, lastDbAccessTime))
        aid = cursor.fetchone()[0]
        self.conn.commit()
        return aid

    def insertMessage(self, text, cdate, ctime, isDeleted):
        cursor = self.conn.cursor()
        query = "insert into parts(text, cdate, ctime, isDeleted) values (%s, %s, %s, %s) returning mid;"
        cursor.execute(query, (text, cdate, ctime, isDeleted))
        mid = cursor.fetchone()[0]
        self.conn.commit()
        return mid

    def insertContact(self, ownerid, memberid):
        cursor = self.conn.cursor()
        query = "insert into parts(ownerid, memberid) values (%s, %s) returning pid;"
        cursor.execute(query, (ownerid, memberid))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid

    def insertChat(self, cname, cdate, ctime, isgroupchat, isActive, adminid):
        cursor = self.conn.cursor()
        query = "insert into parts(cname, cdate, ctime, isgroupchat, isActive, adminid) values (%s, %s, %s, %s, %s, %s) returning pid;"
        cursor.execute(query, (cname, cdate, ctime, isgroupchat, isActive, adminid))
        cid = cursor.fetchone()[0]
        self.conn.commit()
        return cid

    def insertTopic(self, hashtag):
        cursor = self.conn.cursor()
        query = "insert into parts(hastag) values (%s) returning tid;"
        cursor.execute(query, (hashtag))
        tid = cursor.fetchone()[0]
        self.conn.commit()
        return tid

    def insertParticipant(self, cid, uid, pdate, ptime):
        cursor = self.conn.cursor()
        query = "insert into parts(cid, uid, pdate, ptime) values (%s, %s, %s, %s) returning paid;"
        cursor.execute(query, (cid, uid, pdate, ptime,))
        paid = cursor.fetchone()[0]
        self.conn.commit()
        return paid

    def insertReacted(self, uid, mid, rdate, rtime, vote):
        cursor = self.conn.cursor()
        query = "insert into parts(uid, mid, rdate, vote) values (%s, %s, %s, %s, %s) returning rid;"
        cursor.execute(query, (uid, mid, rdate, rtime, vote))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    def insertMedia(self, mid, isvideo, location):
        cursor = self.conn.cursor()
        query = "insert into media(mid, isvideo, location) values (%s, %s, %s) returning medid;"
        cursor.execute(query, (mid, isvideo, location))
        medid = cursor.fetchone()[0]
        self.conn.commit()
        return medid