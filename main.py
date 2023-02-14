from controler import ConnectorMysql
import datetime

def header():
    print('*************************')
    print('****** TO DO LIST *******')
    print('*************************')


def load_tasks(cnx):
    tasks = cnx.view_tasks()
    return tasks


cnx = ConnectorMysql()
# cnx.insert_task('2022-05-22', 'Testando conexao', '2022-05-23')
# val = ("2024-11-20","3")
# cnx.update_date(val)

while True:
    tasks = load_tasks(cnx)
    for task in tasks:
        if task[2] <= datetime.date.today():
            print('\033[31m' + 'Task {}(ATRASADO): {}.\nendline: {}\n'.format(task[0], task[1], task[2]) + '\033[0m')
        else:
            print('\033[32m' + 'Task {}: {}.\nendline: {}\n'.format(task[0], task[1], task[2]) + '\033[0m')
        
# se datetime.date.today()

    break

cnx.close_connector()
    #     if pendencia.limit > datetime.date.today():
    #         print('Pendencia no prazo!')
    #     if pendencia.limit == datetime.date.today():
    #         print('Pendencia em alerta!')
    #     else:
    #         print('Pendencia atrasada!')
    #
    # request = int(input(
    #     """\nO que deseja fazer?
    #     1 - Incluir nova pendencia.
    #     2 - Excluir pendencia.
    #     3 - Sair do programa.
    #     Resposta: """
    # ))
    # if request == 1:
    #     print('Incluir nova pendencia')
    # elif request == 2:
    #     print('Excluir pendencia')
    # elif request == 3:
    #     print('Saindo do programa')
    #     break
    # else:
    #     raise ValueError('Requisição não existente!')
