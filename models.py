from typing import List

class Curso:
    def __init__(self, id: str, nome: str, descricao: str):
        self.id = id
        self.nome = nome
        self.descricao = descricao

class Autor:
    def __init__(self, cpf: str, nome: str, email: str, curso: Curso):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.curso = curso

class Orientador:
    def __init__(self, cpf: str, nome: str, email: str, titulacao: str):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.titulacao = titulacao

class TrabalhoAcademico:
    def __init__(self, titulo: str, descricao: str, resumo: str, data_entrega: str, autores: List[Autor], orientador: Orientador, palavras_chave: List[str]):
        self.titulo = titulo
        self.descricao = descricao
        self.resumo = resumo
        self.data_entrega = data_entrega
        self.autores = autores
        self.orientador = orientador
        self.palavras_chave = palavras_chave
