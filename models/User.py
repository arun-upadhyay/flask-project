from models.dou import Dou


class User:
    def __init__(self):
        dou = Dou()
        self.conn = dou.getDb()

    def get_user(self, username, password):
        sql = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password);
        users = self.conn.execute(sql)

        for user in users:
            if user[1] == username and user[2] == password:
                return True
        return False

    def get_user_by_id(self, id):
        sql = "SELECT * FROM users WHERE id = {}".format(id)
        cur = self.conn.cursor()
        cur.execute(sql)
        user = cur.fetchone()
        if user is not None:
            return {
                'id': user[0],
                'username': user[1],
                'password': user[2]
            }
        else:
            return False

    def add_user(self, username, password):
        sql = "INSERT INTO users(username, password) VALUES ('{}', '{}')".format(username, password);
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        print("Record has been successfully added")

    def get_all_users(self):
        sql = "SELECT * FROM  users "
        return self.conn.execute(sql)

    def delete_user(self, id):
        sql = "DELETE FROM users WHERE id = {}".format(id);
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        print("Record has been successfully deleted")
        return True

    def update_user(self, username, password, userId):
        sql = "UPDATE users SET username='{}', password='{}'  WHERE id ={}".format(username, password, userId);
        print(sql)
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        print("Record has been successfully deleted")
        return True
