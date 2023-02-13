import datetime

def mostra_cabecalho():
    print('*************************')
    print('****** TO DO LIST *******')
    print('*************************')


lista_de_pendencias = carrega_pendencias()
mostra_cabecalho()
while True:
    for pendencia in lista_de_pendencias:
        if pendencia.limit > datetime.date.today():
            print('Pendencia em verde')
        if pendencia.limit == datetime.date.today():
            print('Pendencia em amarelo')
        else:
            print('Pendencia em vermelho')

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
