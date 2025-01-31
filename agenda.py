def adicionar_contatos():

    contatos = []
    contato = {
        "nome": "Rick",
        "telefone": "11976004453"
    }

def listar_contatos():

def buscar_contato():


def main():
    while True:
        print("\n==== Agenda de Contatos ==== ")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")

        try:

            if opcao == "4":
                print("Obrigado por utilizar a Agenda!")
                break
                
            if opcao == "1":
                entrada_usuario = adicionar_contatos()
                continue
            
            if opcao == "2":
                entrada_usuario = listar_contatos()
                continue

            if opcao == "3":
                entrada_usuario = buscar_contato()
                continue

        except ValueError:
            print("Opção inválida!")

if __name__ == "__main__":
    main()