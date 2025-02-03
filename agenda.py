import json

def adicionar_contatos(lista_contatos):
    print("\n=== Adicionar Novo Contato ===")

    nome = input("Digite o nome: ").strip()
    if not nome:
        print("Nome não pode estar vazio!")
        return
    
    telefone = input("Digite o telefone: ").strip()
    if not telefone.isdigit():
        print("Telefone deve conter apenas números: ")
        return
    
    contato = {
        "nome": nome,
        "telefone": telefone
    }

    lista_contatos.append(contato)
    print("Contato adicionado com sucesso!")

def listar_contatos(lista_contatos):
    print("\n=== Lista de Contatos ===")

    if not lista_contatos:
        print("\nNenhum contato cadastrado!")
        return
    for i, contato in enumerate(lista_contatos, 1):
        print(f"\n{i}. Nome: {contato['nome']}")
        print(f"   Telefone: {contato['telefone']}")
    

def buscar_contato(lista_contatos):
    print("\n=== Buscar Contato ===")

    if not lista_contatos:
        print("Nenhum contato cadastrado!")
        return
    
    busca = input("Digite o nome para busca: ").lower().strip()
    if not busca:
        print("Digite um nome válido!")
        return
    
    encontrados = 0
    for i, contato in enumerate(lista_contatos, 1):
        if busca in contato['nome'].lower():
            print(f"\n{i}. Nome: {contato['nome']}")
            print(f"   Telefone: {contato['telefone']}")
            encontrados += 1

    if encontrados == 0:
        print("\nNenhum contato encontrado!")

def remover_contato(lista_contatos):
    print("\n=== Remover Contato ===")

    if not lista_contatos:
        print("Nenhum contato encontrado!")
        return
    
    for i, contato in enumerate(lista_contatos, 1):
        print(f"\n{i}. Nome: {contato['nome']}")
        print(f"   Telefone: {contato['telefone']}")

    try:
        opcao = int(input("\nDigite o número do contato a ser removido: "))

        if 1 <= opcao <= len(lista_contatos):
            contato = lista_contatos[opcao - 1]
            print(f"\nContato selecionado: {contato['nome']}")

            confirmacao = input("Confirma a remoção? (S/N): ").lower().strip()
            if confirmacao == 's':
                lista_contatos.pop(opcao - 1)
                print("\nContato removido com sucesso!")
            else:
                print("\nOperação cancelada!")
        else:
            print("\nNúmero de contato inválido!")

    except ValueError:
        print("Por favor, digite um número válido!")

def editar_contato(lista_contatos):
    print("\n=== Editar Contato ===")

    if not lista_contatos:
        print("Nenhum contato cadastrado!")
        return
    
    for i, contato in enumerate(lista_contatos, 1):
        print(f"\n{i}. Nome: {contato["nome"]}")
        print(f"   Telefone: {contato["telefone"]}")

    try:

        numero_contato = int(input("\nDigite o número do contato a ser editado: "))

        if 1 <= numero_contato <= len(lista_contatos):
            contato = lista_contatos[numero_contato - 1]
            print(f"\nContato selecionado: {contato['nome']}")

            print("\n=== Opções de Edição ===")
            print("1. Editar nome")
            print("2. Editar telefone")
            print("3. Voltar")

            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "1":
                novo_nome = input("Digite o novo nome: ").strip()
                if novo_nome:
                    lista_contatos[numero_contato -1]["nome"] = novo_nome
                    print("\nNome editado com sucesso!")
                else:
                    print("\nNome inválido!")

            elif opcao == "2":
                novo_telefone = input("Digite o novo telefone: ").strip()
                if novo_telefone.isdigit():
                    lista_contatos[numero_contato -1]["telefone"] = novo_telefone
                    print("\nTelefone editado com sucesso!")
                else:
                    print("\nTelefone inválido!")

            elif opcao == "3":
                print("\nOperação cancelada!")

            else:
                print("\nOpção inválida!")

        else:
            print("\nNúmero de contato inválido!")

    except ValueError:
        print("Por favor, digite um número válido!")

def salvar_contatos(lista_contatos):
    try:
        with open('contatos.json', 'w') as arquivo:
            json.dump(lista_contatos, arquivo, indent=4)
            print("\nContatos salvos com sucesso!")
    except Exception as e:
        print(f"\nErro ao salvar contatos: {e}")

def carregar_contatos():
    try:
        with open('contatos.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("\nNenhum arquivo de contatos encontrado. Iniciando com lista vazia.")
        return []
    except json.JSONDecodeError:
        print("\nArquivo de contatos corrompido. Iniciando com lista vazia.")
        return []



contatos = []

def main():
    contatos = carregar_contatos()
    while True:
        print("\n==== Agenda de Contatos ==== ")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Remover contato")
        print("5. Editar contato")
        print("6. Sair")

        opcao = input("\nEscolha uma opção: ")
 
        if opcao == "1":
            adicionar_contatos(contatos)
        elif opcao == "2":
            listar_contatos(contatos)
        elif opcao == "3":
            buscar_contato(contatos)
        elif opcao == "4":
            remover_contato(contatos)
        elif opcao == "5":
            editar_contato(contatos)
        elif opcao == "6":
            salvar_contatos(contatos)
            print("Obrigado por utilizar a agenda!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()