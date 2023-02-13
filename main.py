from controler import ConnectorMysql


def header():
    print('*************************')
    print('****** TO DO LIST *******')
    print('*************************')


def load_tasks(cnx):
    login = cnx
    tasks = login.view_tasks()
    print(type(tasks))
    return tasks


cnx = ConnectorMysql()
cnx.insert_task('2022-05-22', 'Testando conexao', '2022-05-23')
tasks = load_tasks(cnx)

while True:
    for task in tasks:
        print(task)
        print(type(task))
    break

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
