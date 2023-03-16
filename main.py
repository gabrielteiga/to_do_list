from controler import ConnectorMysql as Login
import datetime


def title_todolist():
    print('*************************')
    print('****** TO DO LIST *******')
    print('*************************')


def load_tasks(cnx):
    tasks = cnx.get_all_tasks()
    return tasks


def show_tasks(cnx):
    tasks = load_tasks(cnx)
    for task in tasks:
        print(task)


def client_request():
    request = int(input(
        """\nWhat do you wanna do?
        1 - New Task.
        2 - Update date's task.
        3 - Delete a task.
        4 - Details of a task.
        5 - Exit
        Answer: """
    ))
    return request


def inserting(cnx):
    task = input('What do you need to do? ')
    deadline = input("What's the deadline(YYYY-MM-DD)? ")
    val = (datetime.date.today(), task, deadline)
    cnx.insert_task(val)


def updating(cnx):
    task = str(input("What's task id? "))
    new_deadline = str(input("New deadline(YYYY-MM-DD)? "))
    val = (new_deadline, task)
    cnx.update_date(val)


def deleting(cnx):
    id_task = tuple(input("What's the task id? "))
    print('Deleting task {}'.format(id_task))
    cnx.delete_data(id_task)


def get_task(cnx):
    id_task = tuple(input("What's the task id? "))
    task = cnx.get_details_task(id_task)
    task.details()


def main():
    title_todolist()
    cnx = Login()
    while True:
        show_tasks(cnx)
        request = client_request()
        if request == 1:
            inserting(cnx)
        elif request == 2:
            updating(cnx)
        elif request == 3:
            deleting(cnx)
        elif request == 4:
            get_task(cnx)
        elif request == 5:
            print('\nSee you soon!\n')
            break
        else:
            print('Invalid request!')
    cnx.close_connector()


if __name__ == '__main__':
    main()
