from models import Autor, Orientador, Curso, TrabalhoAcademico
from controllers import GerenciadorAcademico
from views import View

def main():
    gerenciador = GerenciadorAcademico()
    view = View()

    while True:
        view.menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cpf, nome, email, curso_id = view.obter_dados_autor()
            curso = next((c for c in gerenciador.cursos if c.id == curso_id), None)
            if curso:
                autor = Autor(cpf, nome, email, curso)
                gerenciador.inserir_autor(autor)
            else:
                print("Curso não encontrado!")
        elif opcao == "2":
            cpf, nome, email, curso_id = view.obter_dados_autor()
            curso = next((c for c in gerenciador.cursos if c.id == curso_id), None)
            if curso:
                gerenciador.atualizar_autor(cpf, nome, email, curso)
            else:
                print("Curso não encontrado!")
        elif opcao == "3":
            cpf = input("CPF do autor a ser removido: ")
            gerenciador.remover_autor(cpf)
        elif opcao == "4":
            cpf, nome, email, titulacao = view.obter_dados_orientador()
            orientador = Orientador(cpf, nome, email, titulacao)
            gerenciador.inserir_orientador(orientador)
        elif opcao == "5":
            cpf, nome, email, titulacao = view.obter_dados_orientador()
            gerenciador.atualizar_orientador(cpf, nome, email, titulacao)
        elif opcao == "6":
            cpf = input("CPF do orientador a ser removido: ")
            gerenciador.remover_orientador(cpf)
        elif opcao == "7":
            id, nome, descricao = view.obter_dados_curso()
            curso = Curso(id, nome, descricao)
            gerenciador.inserir_curso(curso)
        elif opcao == "8":
            id, nome, descricao = view.obter_dados_curso()
            gerenciador.atualizar_curso(id, nome, descricao)
        elif opcao == "9":
            id = input("ID do curso a ser removido: ")
            gerenciador.remover_curso(id)
        elif opcao == "10":
            titulo, descricao, resumo, data_entrega, cpf_orientador, palavras_chave = view.obter_dados_trabalho()
            orientador = next((o for o in gerenciador.orientadores if o.cpf == cpf_orientador), None)
            if orientador:
                autores = []
                num_autores = int(input("Número de autores: "))
                for _ in range(num_autores):
                    cpf_autor = input("CPF do autor: ")
                    autor = next((a for a in gerenciador.autores if a.cpf == cpf_autor), None)
                    if autor:
                        autores.append(autor)
                    else:
                        print(f"Autor com CPF {cpf_autor} não encontrado.")
                trabalho = TrabalhoAcademico(titulo, descricao, resumo, data_entrega, autores, orientador, palavras_chave)
                gerenciador.inserir_trabalho(trabalho)
            else:
                print("Orientador não encontrado!")
        elif opcao == "11":
            titulo, descricao, resumo, data_entrega, cpf_orientador, palavras_chave = view.obter_dados_trabalho()
            orientador = next((o for o in gerenciador.orientadores if o.cpf == cpf_orientador), None)
            if orientador:
                gerenciador.atualizar_trabalho(titulo, descricao, resumo, data_entrega, orientador, palavras_chave)
            else:
                print("Orientador não encontrado!")
        elif opcao == "12":
            titulo = input("Título do trabalho a ser removido: ")
            gerenciador.remover_trabalho(titulo)
        elif opcao == "13":
            cpf_orientador = input("CPF do orientador: ")
            trabalhos = gerenciador.consultar_trabalhos_por_orientador(cpf_orientador)
            view.mostrar_trabalhos(trabalhos)
        elif opcao == "14":
            palavra_chave = input("Palavra-chave: ")
            trabalhos = gerenciador.consultar_trabalhos_por_palavra_chave(palavra_chave)
            view.mostrar_trabalhos(trabalhos)
        elif opcao == "0":
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
