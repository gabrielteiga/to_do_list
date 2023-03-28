from controler import ConnectorMysql as Login


def title_todolist():
    print('*************************')
    print('****** TO DO LIST *******')
    print('*************************')


def client_request():
    request = input(
        """\nWhat do you wanna do?
        1 - New Task.
        2 - Update date's task.
        3 - Details of a task.
        4 - Delete a task.
        5 - Exit
        Answer: """
    )
    if request.isdigit():
        return int(request)
    else:
        input('Input a NUMBER! Press any key to continue...')


def main():
    title_todolist()
    cnx = Login()
    while True:
        cnx.show_tasks()
        request = client_request()
        if request == 1:
            cnx.inserting_new_task()
        elif request == 2:
            cnx.updating_a_task()
        elif request == 3:
            cnx.details_of_a_task()
        elif request == 4:
            cnx.deleting_a_task()
        elif request == 5:
            print('\nSee you soon!\n')
            break
        else:
            print('Invalid request!', end='\n\n')
    cnx.close_connector()


if __name__ == '__main__':
    main()
