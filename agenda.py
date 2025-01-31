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

contatos = []

def main():
    while True:
        print("\n==== Agenda de Contatos ==== ")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Remover contato")
        print("5. Sair")

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
            print("Obrigado por utilizar a agenda!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()