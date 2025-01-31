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
        print("Nenhum contato cadastrado!")
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


contatos = []


def main():
    while True:
        print("\n==== Agenda de Contatos ==== ")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")
 
        if opcao == "1":
            adicionar_contatos(contatos)
        elif opcao == "2":
            listar_contatos(contatos)
        elif opcao == "3":
            buscar_contato(contatos)
        elif opcao == "4":
            print("Obrigado por utilizar a Agenda!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()