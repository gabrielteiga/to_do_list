import mysql.connector
from task_object import Task
from dbTodo import *


class ConnectorMysql:
    def __init__(self):
        user, pwd = self.login_local_host()
        self.cnx = self.create_connector(user, pwd)
        self.user = user.lower()
        self.host = 'localhost'
        self.database = 'todo'
        self.cursor = self.cnx.cursor()

    @staticmethod
    def login_local_host():
        user = str(input('User: '))
        pwd = str(input('Password: '))
        print('')
        return user, pwd


    @staticmethod
    def create_connector(user, pwd):
        cnx = mysql.connector.connect(
            user=f'{user}',
            password=f'{pwd}',
            host=f'localhost'
        )
        cursor = cnx.cursor()
        data_query = show_databases()
        cursor.execute(data_query)
        for database in cursor:
            if database[0] == 'todo':
                cnx = mysql.connector.connect(
                    user=f'{user}',
                    password=f'{pwd}',
                    host='localhost',
                    database='todo'
                )
                return cnx
            
        data_query = create_todo()
        cursor.execute(data_query)
        
        data_query = use_todo()
        cursor.execute(data_query)

        data_query = create_tbtodo()
        cursor.execute(data_query)
        
        cnx = mysql.connector.connect(
            user=f'{user}',
            password=f'{pwd}',
            host='localhost',
            database='todo'
        )
        return cnx
    

    def get_all_tasks(self):
        data_query = select_data_tbTodo()
        self.cursor.execute(data_query)
        list_of_tasks = self.cursor.fetchall()
        tasks = []
        for job in list_of_tasks:
            task = Task(job)
            tasks.append(task)
        return tuple(tasks)

    def get_details_task(self, val):
        data_query = select_task_tbTodo()
        self.cursor.execute(data_query, val)
        job = self.cursor.fetchone()
        task = Task(job)
        return task

    def insert_task(self, val):
        data_query = insert_data_tbTodo()
        self.cursor.execute(data_query, val)
        self.commit()

    def update_date(self, val):
        data_query = update_data_tbTodo()
        self.cursor.execute(data_query, val)
        self.commit()

    def delete_data(self, id_task):
        data_query = delete_task_tbTodo()
        self.cursor.execute(data_query, id_task)
        self.commit()
        print('\nTask {} deleted!\n'.format(id_task))

    def commit(self):
        self.cnx.commit()
        print('\nNew commit!\nUser: {}\n'.format(self.user))

    def close_connector(self):
        self.cursor.close()
        self.cnx.close()
