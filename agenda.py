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

def listar_contatos():
    return None

def buscar_contato():
    return None


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