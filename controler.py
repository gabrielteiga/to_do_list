import mysql.connector
from datetime import date
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
    

    def load_tasks(self):
        tasks = self.get_all_tasks()
        return tasks


    def show_tasks(self):
        tasks = self.load_tasks()
        for task in tasks:
            print(task)


    def inserting_new_task(self):
        task = input('What do you need to do? ')
        deadline = input("What's the deadline(YYYY-MM-DD)? ")
        val = (date.today(), task, deadline)
        self.insert_task(val)


    def updating_a_task(self):
        id_task = str(input("What's task id? "))
        new_deadline = str(input("New deadline(YYYY-MM-DD)? "))
        val = (new_deadline, id_task)
        self.update_date(val)


    def details_of_a_task(self):
        id_task = tuple(input("What's the task id? "))
        task = self.get_task(id_task)
        task.details()


    def deleting_a_task(self):
        id_task = tuple(input("What's the task id? "))
        print('\nDeleting task {}...'.format(id_task[0]))
        self.delete_data(id_task)


    def get_all_tasks(self):
        data_query = select_data_tbTodo()
        self.cursor.execute(data_query)
        list_of_tasks = self.cursor.fetchall()
        tasks = []
        for job in list_of_tasks:
            task = Task(job)
            tasks.append(task)
        return tuple(tasks)


    def get_task(self, val):
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
        print('Task {} deleted!\n'.format(id_task[0]))


    def commit(self):
        self.cnx.commit()
        print('\nNew commit!\nUser: {}\n'.format(self.user))


    def close_connector(self):
        self.cursor.close()
        self.cnx.close()
