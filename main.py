from controler import ConnectorMysql
import datetime

def header():
    print('*************************')
    print('****** TO DO LIST *******')
    print('*************************')


def load_tasks(cnx):
    tasks = cnx.view_tasks()
    return tasks

def run():
    cnx = ConnectorMysql()

    while True:
        tasks = load_tasks(cnx)
        for task in tasks:
            if task[2] < datetime.date.today():
                print('\033[31m' + 'Task {}(ATRASADO): {}.\nendline: {}\n'.format(task[0], task[1], task[2]) + '\033[0m')
            elif task[2] == datetime.date.today():
                print('\033[33m' + 'Task {}: {}.\nendline: {}\n'.format(task[0], task[1], task[2]) + '\033[0m')
            else:
                print('\033[32m' + 'Task {}: {}.\nendline: {}\n'.format(task[0], task[1], task[2]) + '\033[0m')
        break

    cnx.close_connector()

if __name__ == '__main__':
    run()

    # request = int(input(
    #     """\nO que deseja fazer?
    #     1 - Incluir nova pendencia.
    #     2 - Alterar data pendencia
    #     3 - Excluir pendencia
    #     3 - Sair do programa.
    #     Resposta: """
    # ))
    # if request == 1:
    #     cnx.insert_task('2022-05-22', 'Teste', '2022-05-23')
    # elif request == 2:
    #     val = ("2024-11-20","3")
    #     cnx.update_date(val)
    # elif request == 3:
    #     id_task = str(input('Qual o número da task que deseja excluir? '))
    #     print('Deletando task {}'.format(id_task))
    #     cnx.delete_data(id_task)
    # elif request == 4:
    #     print('Saindo do programa')
    #     break
    # else:
    #     raise ValueError('Requisição não existente!')
