import json
from colorama import init, Fore, Style

init(autoreset=True)

def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo)

def exibir_menu():
    print(Fore.CYAN + "╔═════════════════════════╗")
    print(Fore.CYAN + "║ " + Fore.GREEN + "Gerenciador de Tarefas" + Fore.CYAN + "  ║")
    print(Fore.CYAN + "╠═════════════════════════╣")
    print(Fore.CYAN + "║ " + Fore.WHITE + "1. " + Fore.GREEN + "Criar nova tarefa" + Fore.CYAN + "    ║")
    print(Fore.CYAN + "║ " + Fore.WHITE + "2. " + Fore.YELLOW + "Visualizar tarefas" + Fore.CYAN + "   ║")
    print(Fore.CYAN + "║ " + Fore.WHITE + "3. " + Fore.BLUE + "Atualizar tarefa" + Fore.CYAN + "     ║")
    print(Fore.CYAN + "║ " + Fore.WHITE + "4. " + Fore.MAGENTA + "Remover tarefa" + Fore.CYAN + "       ║")
    print(Fore.CYAN + "║ " + Fore.WHITE + "5. " + Fore.RED + "Filtrar tarefas" + Fore.CYAN + "      ║")
    print(Fore.CYAN + "║ " + Fore.WHITE + "0. " + Fore.WHITE + "Sair do programa" + Fore.CYAN + "     ║")
    print(Fore.CYAN + "╚═════════════════════════╝")

def criar_tarefa():
    print(Fore.CYAN + "╔═════════════════════════════════════╗")
    titulo = input("    Digite o título da tarefa: ")
    descricao = input("    Digite a descrição da tarefa: ")
    status = input("    Digite o status da tarefa: ")
    print(Fore.CYAN + "╚═════════════════════════════════════╝")

    return {'titulo': titulo, 'descricao': descricao, 'status': status}

def visualizar_tarefas(tarefas):
    if not tarefas:
        print(Fore.YELLOW + "Nenhuma tarefa encontrada.")
    else:
        print(Fore.WHITE + "╔══════════════════════════════════════════════════════════════════════")
        for i, tarefa in enumerate(tarefas, start=1):
            print(Fore.WHITE + f"║   {Fore.WHITE}Tarefa {i}:" )
            print(f"║   {Fore.WHITE}Título: {tarefa['titulo']}")
            print(f"║   {Fore.WHITE}Descrição: {tarefa['descricao']}")
            print(f"║   {Fore.WHITE}Status: {tarefa['status']}")
            print(Fore.WHITE + "╠══════════════════════════════════════════════════════════════════════")
        print("╚══════════════════════════════════════════════════════════════════════")

def atualizar_tarefa(tarefas):
    if not tarefas:
        print(Fore.YELLOW + "Nenhuma tarefa encontrada.")
    else:
        visualizar_tarefas(tarefas)
        tarefa_index = int(input("Digite o número da tarefa que deseja atualizar: ")) - 1
        if 0 <= tarefa_index < len(tarefas):
            tarefa = tarefas[tarefa_index]
            titulo = input("Digite o novo título da tarefa: ")
            descricao = input("Digite a nova descrição da tarefa: ")
            status = input("Digite o novo status da tarefa: ")
            tarefa['titulo'] = titulo
            tarefa['descricao'] = descricao
            tarefa['status'] = status
            print(Fore.GREEN + "Tarefa atualizada com sucesso.")
        else:
            print(Fore.RED + "Número de tarefa inválido.")

def remover_tarefa(tarefas):
    if not tarefas:
        print(Fore.YELLOW + "Nenhuma tarefa encontrada.")
    else:
        visualizar_tarefas(tarefas)
        tarefa_index = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        if 0 <= tarefa_index < len(tarefas):
            tarefa_removida = tarefas.pop(tarefa_index)
            print(Fore.GREEN + "Tarefa removida:")
            print(f"Título: {tarefa_removida['titulo']}")
            print(f"Descrição: {tarefa_removida['descricao']}")
            print(f"Status: {tarefa_removida['status']}")
            print()
        else:
            print(Fore.RED + "Número de tarefa inválido.")

def filtrar_tarefas(tarefas):
    status = input("Digite o status pelo qual deseja filtrar as tarefas: ")
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa['status'].lower() == status.lower()]
    if not tarefas_filtradas:
        print(Fore.YELLOW + "Nenhuma tarefa encontrada com o status informado.")
    else:
        print(Fore.YELLOW + f"Tarefas com o status '{status}':")
        print(Fore.CYAN + "╔═════════════════════════════════╗")
        for i, tarefa in enumerate(tarefas_filtradas, start=1):
            print(Fore.CYAN + f"║   {Fore.WHITE}Tarefa {i}:{Fore.CYAN}                   ║")
            print(f"║   {Fore.WHITE}Título: {tarefa['titulo']}{Fore.CYAN}         ║")
            print(f"║   {Fore.WHITE}Descrição: {tarefa['descricao']}{Fore.CYAN}    ║")
            print(f"║   {Fore.WHITE}Status: {tarefa['status']}{Fore.CYAN}           ║")
            print(Fore.CYAN + "╠═════════════════════════════════╣")
        print(Fore.CYAN + "╚═════════════════════════════════╝")

tarefas = carregar_tarefas()

while True:
    exibir_menu()
    print(Fore.WHITE + "╔═════════════════════════╗")
    opcao = input(f"║   {Fore.CYAN}opcão: ") 
    print(Fore.WHITE + "╚═════════════════════════╝")

    if opcao == '1':
        nova_tarefa = criar_tarefa()
        tarefas.append(nova_tarefa)
        print(Fore.GREEN + "Tarefa criada com sucesso.")
    elif opcao == '2':
        visualizar_tarefas(tarefas)
    elif opcao == '3':
        atualizar_tarefa(tarefas)
    elif opcao == '4':
        remover_tarefa(tarefas)
    elif opcao == '5':
        filtrar_tarefas(tarefas)
    elif opcao == '0':
        salvar_tarefas(tarefas)
        print(Fore.CYAN + "Programa encerrado.")
        break
    else:
        print(Fore.RED + "Opção inválida. Digite um número válido.")
