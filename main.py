from controler import ConnectorMysql as Login
import datetime


def title_todolist():
    print('*************************')
    print('****** TO DO LIST *******')
    print('*************************')


def load_tasks(cnx):
    tasks = cnx.get_all_tasks()
    return tasks


def inserting(cnx):
    task = input('What do you need to do? ')
    deadline = input("What's the deadline(YYYY-MM-DD)? ")
    val = (datetime.date.today(), task, deadline)
    cnx.insert_task(val)


def updating(cnx):
    try:
        task = str(input("What's task id? "))
        new_deadline = str(input("New deadline(YYYY-MM-DD)? "))
        val = (new_deadline, task)
        cnx.update_date(val)
    except:
        raise ValueError("Task not found!")


def deleting(cnx):
    id_task = tuple(input("What's the task id? "))
    print('Deleting task {}'.format(id_task))
    cnx.delete_data(id_task)


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


def show_tasks(cnx):
    tasks = load_tasks(cnx)
    for task in tasks:
        if task[2] < datetime.date.today():
            print('\033[31m' + 'Task {}(ATRASADO): {}.\ndeadline: {}'.format(task[0], task[1], task[2]) + '\033[0m')
        elif task[2] == datetime.date.today():
            print('\033[33m' + 'Task {}: {}.\ndeadline: {}'.format(task[0], task[1], task[2]) + '\033[0m')
        else:
            print('\033[32m' + 'Task {}: {}.\ndeadline: {}'.format(task[0], task[1], task[2]) + '\033[0m')


def get_task(cnx):
    id_task = tuple(input("What's the task id? "))
    task = cnx.get_details_task(id_task)
    print(
        f"\nTask n°{task[0]}\nTask created in: {task[1]}\nTask: {task[2]}\ndeadline: {task[3]}\n"
    )


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
            print('See you soon!')
            break
        else:
            raise ValueError('Invalid request!')
    cnx.close_connector()


if __name__ == '__main__':
    main()
