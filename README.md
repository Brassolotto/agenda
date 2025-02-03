# Agenda de Contatos em Python

## 📝 Descrição
Uma aplicação de linha de comando para gerenciar contatos, permitindo adicionar, listar, buscar, editar e remover contatos, com persistência de dados em arquivo JSON.

## 🚀 Funcionalidades
- Adicionar novos contatos
- Listar todos os contatos
- Buscar contatos por nome
- Editar contatos existentes
- Remover contatos
- Salvar contatos em arquivo
- Carregar contatos automaticamente

## 📋 Dados Armazenados
- Nome do contato
- Número de telefone

## 🔧 Como executar
1. Clone este repositório:
```bash
git clone https://github.com/Brassolotto/agenda.git
```

2. Navegue até o diretório do projeto:
```bash
cd agenda-contatos
```

3. Execute o programa:
```bash
python agenda.py
```

## 📋 Pré-requisitos
- Python 3.6 ou superior
- Não requer bibliotecas externas

## 💻 Como usar
1. Escolha uma opção do menu:
   - 1: Adicionar contato
   - 2: Listar contatos
   - 3: Buscar contato
   - 4: Editar contato
   - 5: Remover contato
   - 6: Sair

2. Siga as instruções na tela para cada operação

## 🗃️ Armazenamento
- Os contatos são salvos em `contatos.json`
- Carregamento automático ao iniciar
- Salvamento automático ao sair
- Formato JSON para fácil leitura/edição

## ⚙️ Estrutura do Código
```
agenda.py
├── Função adicionar_contatos()
├── Função listar_contatos()
├── Função buscar_contato()
├── Função editar_contato()
├── Função remover_contato()
├── Função salvar_contatos()
├── Função carregar_contatos()
└── Função main()
```

## 🔍 Exemplo de Uso
```
=== Agenda de Contatos ===
1. Adicionar contato
2. Listar contatos
3. Buscar contato
4. Editar contato
5. Remover contato
6. Sair

Escolha uma opção: 
```

## ⚠️ Tratamento de Erros
- Validação de entradas
- Verificação de arquivo corrompido
- Tratamento de arquivo inexistente
- Validação de números de telefone
- Confirmação antes de alterações

## 🤝 Contribuindo
Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## ✨ Melhorias Futuras
- [ ] Adicionar mais campos (email, endereço, etc)
- [ ] Implementar categorias de contatos
- [ ] Adicionar backup automático
- [ ] Implementar interface gráfica
- [ ] Adicionar foto do contato
- [ ] Exportar contatos em diferentes formatos

## 📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor
Seu Nome
- GitHub: [@seu-usuario](https://github.com/Brassolotto)
- LinkedIn: [@seu-linkedin](https://linkedin.com/in/ricardo-brassolotto)

---
⌨️ com ❤️ por [Rick Brassolotto] 😊