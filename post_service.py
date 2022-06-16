import json
from db_manager import mysql
class PostService:

    def __init__(self):
        self.mysql = mysql;

    def all(self):
        q = "SELECT * FROM posts order by created limit 12 "
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchall()
        return data
    
    def find(self,postId):
        q = "SELECT * FROM posts WHERE id = " + str(postId)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchone()
        return data

    def create(self,title,content,cat):
        q = "INSERT INTO posts (title,content,category) VALUES ('%s','%s','%s')" % (title, content, cat)
        print(q)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()
        lastid = cursor.lastrowid;
        return self.find(lastid)

    def update(self,postId,title,content,cat):
        q = "UPDATE posts set title='%s', content='%s', category='%s' WHERE id = %s" % (title, content, cat, str(postId))
        print(q)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()
        return self.find(postId)
    
    def delete(self,postId):
        q = "delete FROM posts WHERE id = " + str(postId)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()

    def comments(self,postId):
        q = "SELECT * FROM comments where idpost = %s  order by created desc" % str(postId)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        data = cursor.fetchone()
        return data

    def createComment(self,postId,comment):
        q = "INSERT INTO comments (idPost,comment) VALUES('%s','%s')" % (str(postId),comment)
        conn = self.mysql.connect()
        cursor =conn.cursor()
        cursor.execute(q)
        conn.commit()
        lastid = cursor.lastrowid;
        q = "SELECT * FROM comments where id = " + str(lastid)
        cursor.execute(q)
        data = cursor.fetchone()
        return data