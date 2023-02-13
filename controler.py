import mysql.connector

class ConnectorMysql:
    def __init__(self):
        user, pwd, host, db = self.login_local_host()
        self.cnx = self.create_connector(user, pwd, host, db)
        self.user = user.lower()
        self.host = host.lower()
        self.database = db.lower()
        self.cursor = self.cnx.cursor()

    def login_local_host(self):
        user = str(input('User: '))
        pwd = str(input('Password: '))
        host = str(input('Host: '))
        db = str(input('Database: '))
        return user, pwd, host, db

    def create_connector(self, user, pwd, host, db):
        try:
            cnx = mysql.connector.connect(
                user = f'{user}',
                user = f'{pwd}',
                user = f'{host}',
                user = f'{db}'
            )
            return cnx
        except:
            print("Script didn't find the database")

    def view_tasks(self):
        from dbTodo import select_data_tbTodo
        data_query = select_data_tbTodo()
        self.cursor.execute(data_query)
        tasks = self.cursor.fetchall()
        for task in tasks:
            print(task)

    def insert_task(self, task_creation_date, description, endline):
        from dbTodo import insert_data_tbTodo
        data_query = insert_data_tbTodo(task_creation_date, description, endline)
        self.cursor.execute(data_query)

    def uptade_date(self, val):
        from dbTodo import update_data_tbTodo
        data_query = update_data_tbTodo()
        self.cursor.execute(data_query, val)

    def commit(self):
        self.cnx.commit()
        print('New commit!\nUser: {}').format(
            self.user
        )

    def close_connector(self):
        self.cursor.close()
        self.cnx.close()

