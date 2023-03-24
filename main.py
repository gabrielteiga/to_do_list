from controler import ConnectorMysql as Login
import datetime


def title_todolist():
    print('*************************')
    print('****** TO DO LIST *******')
    print('*************************')


def client_request():
    request = int(input(
        """\nWhat do you wanna do?
        1 - New Task.
        2 - Update date's task.
        3 - Details of a task.
        4 - Delete a task.
        5 - Exit
        Answer: """
    ))
    return request


def deleting(cnx):
    id_task = tuple(input("What's the task id? "))
    print('\nDeleting task {}'.format(id_task[0]))
    cnx.delete_data(id_task)


def get_task(cnx):
    id_task = tuple(input("What's the task id? "))
    task = cnx.get_task(id_task)
    task.details()


def main():
    title_todolist()
    cnx = Login()
    while True:
        cnx.show_tasks()
        request = client_request()
        if request == 1:
            cnx.inserting()
        elif request == 2:
            cnx.updating()
        elif request == 3:
            get_task(cnx)
        elif request == 4:
            deleting(cnx)
        elif request == 5:
            print('\nSee you soon!\n')
            break
        else:
            print('Invalid request!')
    cnx.close_connector()


if __name__ == '__main__':
    main()
