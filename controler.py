import mysql.connector
from dbTodo import insert_data_tbTodo, update_data_tbTodo, select_data_tbTodo


class ConnectorMysql:
    def __init__(self):
        user, pwd, host, db = self.login_local_host()
        self.cnx = self.create_connector(user, pwd, host, db)
        self.user = user.lower()
        self.host = host.lower()
        self.database = db.lower()
        self.cursor = self.cnx.cursor()

    @staticmethod
    def login_local_host():
        user = str(input('User: '))
        pwd = str(input('Password: '))
        host = str(input('Host: '))
        db = str(input('Database: '))
        return user, pwd, host, db

    @staticmethod
    def create_connector(user, pwd, host, db):
        try:
            cnx = mysql.connector.connect(
                user=f'{user}',
                password=f'{pwd}',
                host=f'{host}',
                database=f'{db}'
            )
            return cnx
        except:
            print("Script didn't find the database")

    def view_tasks(self):
        data_query = select_data_tbTodo()
        self.cursor.execute(data_query)
        tasks = self.cursor.fetchall()
        return tasks

    def insert_task(self, task_creation_date, description, endline):
        data_query = insert_data_tbTodo(task_creation_date, description, endline)
        self.cursor.execute(data_query)
        self.commit()

    def update_date(self, val):
        data_query = update_data_tbTodo()
        self.cursor.execute(data_query, val)
        self.commit()

    def commit(self):
        self.cnx.commit()
        print('New commit!\nUser: {}'.format(self.user))

    def close_connector(self):
        self.cursor.close()
        self.cnx.close()

