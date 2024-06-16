from models import Autor, Orientador, Curso, TrabalhoAcademico

class GerenciadorAcademico:
    def __init__(self):
        self.autores = []
        self.orientadores = []
        self.cursos = []
        self.trabalhos = []

    
    def inserir_autor(self, autor):
        self.autores.append(autor)

    def atualizar_autor(self, cpf, nome, email, curso):
        for autor in self.autores:
            if autor.cpf == cpf:
                autor.nome = nome
                autor.email = email
                autor.curso = curso
                return
        print(f"Autor com CPF {cpf} não encontrado.")

    def remover_autor(self, cpf):
        autor = next((a for a in self.autores if a.cpf == cpf), None)
        if autor:
            if any(trabalho for trabalho in self.trabalhos if autor in trabalho.autores):
                print("Não é possível remover um autor que possui trabalhos acadêmicos associados.")
                return
            self.autores.remove(autor)
        else:
            print(f"Autor com CPF {cpf} não encontrado.")

    
    def inserir_orientador(self, orientador):
        self.orientadores.append(orientador)

    def atualizar_orientador(self, cpf, nome, email, titulacao):
        for orientador in self.orientadores:
            if orientador.cpf == cpf:
                orientador.nome = nome
                orientador.email = email
                orientador.titulacao = titulacao
                return
        print(f"Orientador com CPF {cpf} não encontrado.")

    def remover_orientador(self, cpf):
        orientador = next((o for o in self.orientadores if o.cpf == cpf), None)
        if orientador:
            if any(trabalho for trabalho in self.trabalhos if trabalho.orientador == orientador):
                print("Não é possível remover um orientador que possui trabalhos acadêmicos associados.")
                return
            self.orientadores.remove(orientador)
        else:
            print(f"Orientador com CPF {cpf} não encontrado.")

  
    def inserir_curso(self, curso):
        self.cursos.append(curso)

    def atualizar_curso(self, id, nome, descricao):
        for curso in self.cursos:
            if curso.id == id:
                curso.nome = nome
                curso.descricao = descricao
                return
        print(f"Curso com ID {id} não encontrado.")

    def remover_curso(self, id):
        curso = next((c for c in self.cursos if c.id == id), None)
        if curso:
            if any(autor for autor in self.autores if autor.curso == curso):
                print("Não é possível remover um curso que possui autores associados.")
                return
            self.cursos.remove(curso)
        else:
            print(f"Curso com ID {id} não encontrado.")

    
    def inserir_trabalho(self, trabalho):
        self.trabalhos.append(trabalho)

    def atualizar_trabalho(self, titulo, descricao, resumo, data_entrega, orientador, palavras_chave):
        for trabalho in self.trabalhos:
            if trabalho.titulo == titulo:
                trabalho.descricao = descricao
                trabalho.resumo = resumo
                trabalho.data_entrega = data_entrega
                trabalho.orientador = orientador
                trabalho.palavras_chave = palavras_chave
                return
        print(f"Trabalho com título {titulo} não encontrado.")

    def remover_trabalho(self, titulo):
        trabalho = next((t for t in self.trabalhos if t.titulo == titulo), None)
        if trabalho:
            self.trabalhos.remove(trabalho)
        else:
            print(f"Trabalho com título {titulo} não encontrado.")

    
    def consultar_trabalhos_por_orientador(self, cpf_orientador):
        orientador = next((o for o in self.orientadores if o.cpf == cpf_orientador), None)
        if orientador:
            return [t for t in self.trabalhos if t.orientador == orientador]
        print(f"Orientador com CPF {cpf_orientador} não encontrado.")
        return []

    def consultar_trabalhos_por_palavra_chave(self, palavra_chave):
        return [t for t in self.trabalhos if palavra_chave in t.palavras_chave]
