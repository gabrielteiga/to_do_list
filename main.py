from controler import ConnectorMysql as Login
import datetime


def header():
    print('*************************')
    print('****** TO DO LIST *******')
    print('*************************')


def load_tasks(cnx):
    tasks = cnx.view_tasks()
    return tasks


def inserting(cnx):
    task = input('Qual a tarefa? ')
    endline = input('Qual o prazo final? ')
    cnx.insert_task(datetime.date.today(), task, endline)


def updating(cnx):
    try:
        task = str(input("Qual o numero da task? "))
        new_endline = str(input("Qual o prazo final? "))
        val = (new_endline, task)
        cnx.update_date(val)
    except:
        raise ValueError('O número da task não foi encontrada!')


def deleting(cnx):
    id_task = tuple(input('Qual o número da task que deseja excluir? '))
    print('Deletando task {}'.format(id_task))
    cnx.delete_data(id_task)


def client_request():
    request = int(input(
        """\nO que deseja fazer?
        1 - Incluir nova tarefa.
        2 - Alterar data tarefa.
        3 - Excluir tarefa.
        4 - Sair do programa.
        Resposta: """
    ))
    return request


def show_tasks(cnx):
    tasks = load_tasks(cnx)
    for task in tasks:
        if task[2] < datetime.date.today():
            print('\033[31m' + 'Task {}(ATRASADO): {}.\nendline: {}'.format(task[0], task[1], task[2]) + '\033[0m')
        elif task[2] == datetime.date.today():
            print('\033[33m' + 'Task {}: {}.\nendline: {}'.format(task[0], task[1], task[2]) + '\033[0m')
        else:
            print('\033[32m' + 'Task {}: {}.\nendline: {}'.format(task[0], task[1], task[2]) + '\033[0m')


def main():
    header()
    cnx = Login()
    print('')
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
            print('Saindo do programa')
            break
        else:
            raise ValueError('Requisição não existente!')
    cnx.close_connector()


if __name__ == '__main__':
    main()
