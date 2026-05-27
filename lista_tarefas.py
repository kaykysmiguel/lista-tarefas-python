print("Lista de tarefas em Python")

lista = []

while True:

    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefa")
    print("3 - Remover tarefas")
    print("4 - Sair")

    opcao = input("Qual opção deseja escolher ? ")

    if opcao == "1":
        tarefa = input("Qual o nome da tarefa ? ")
        lista.append(tarefa)

    elif opcao == "2":
        for tarefa in lista:
            print("Essas são suas tarefas :", tarefa)

    elif opcao == "3":
        tarefa = input("Qual tarefa deseja remover ? ")

        if tarefa in lista:
          lista.remove(tarefa)
          print("Tarefa removida")

        else:
            print("Tarefa não encontrada")

    elif opcao == "4":
        print("Sistema encerrado")
        break

    else: 
        print("Opção invalida")
