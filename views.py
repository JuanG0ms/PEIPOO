class View:
    def menu(self):
        print("1. Inserir Autor")
        print("2. Atualizar Autor")
        print("3. Remover Autor")
        print("4. Inserir Orientador")
        print("5. Atualizar Orientador")
        print("6. Remover Orientador")
        print("7. Inserir Curso")
        print("8. Atualizar Curso")
        print("9. Remover Curso")
        print("10. Inserir Trabalho Acadêmico")
        print("11. Atualizar Trabalho Acadêmico")
        print("12. Remover Trabalho Acadêmico")
        print("13. Consultar Trabalhos por Orientador")
        print("14. Consultar Trabalhos por Palavra-Chave")
        print("0. Sair")

    def obter_dados_autor(self):
        cpf = input("CPF: ")
        nome = input("Nome: ")
        email = input("Email: ")
        curso_id = input("ID do Curso: ")
        return cpf, nome, email, curso_id

    def obter_dados_orientador(self):
        cpf = input("CPF: ")
        nome = input("Nome: ")
        email = input("Email: ")
        titulacao = input("Titulação: ")
        return cpf, nome, email, titulacao

    def obter_dados_curso(self):
        id = input("ID: ")
        nome = input("Nome: ")
        descricao = input("Descrição: ")
        return id, nome, descricao

    def obter_dados_trabalho(self):
        titulo = input("Título: ")
        descricao = input("Descrição: ")
        resumo = input("Resumo: ")
        data_entrega = input("Data de Entrega: ")
        cpf_orientador = input("CPF do Orientador: ")
        palavras_chave = input("Palavras-Chave (separadas por vírgula): ").split(",")
        return titulo, descricao, resumo, data_entrega, cpf_orientador, palavras_chave

    def mostrar_trabalhos(self, trabalhos):
        for trabalho in trabalhos:
            print(f"Título: {trabalho.titulo}, Orientador: {trabalho.orientador.nome}, Data de Entrega: {trabalho.data_entrega}")
