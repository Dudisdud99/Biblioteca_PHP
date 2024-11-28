# Biblioteca simples com livros e autores

import os
import numpy as np
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

# variaveis globais

livros = []
autores = []

# Classes

# -- Classe Autor

class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade


    # set

    def set_nacionalidade(self, nacionalidade):
        self.nacionalidade = nacionalidade
    
    def set_nome(self, nome):
        self.nome = nome

    # get

    def get_nome(self):
        return self.nome

    def get_nacionalidade(self):
        return self.nacionalidade
    
    # Funções

    def exibir_autor(self):
        print("Nome: ", self.nome)
        print("Nacionalidade: ", self.nacionalidade)

# -- Classe Livro

class Livro:
    def __init__(self, titulo, isbn, ano_publicacao, status, autor):
        self.titulo = titulo
        self.isbn = isbn 
        self.ano_publicacao = ano_publicacao 
        self.status = status # Status de disponibilidade (ex: disponível, emprestado)
        self.autor = autor

    # set

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor

    def set_isbn(self, isbn):
        self.isbn = isbn

    def set_ano_publicacao(self, ano_publicacao):
        self.ano_publicacao = ano_publicacao

    def set_status(self, status):
        self.status = status

    # get

    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def get_isbn(self):
        return self.isbn
    
    def get_ano_publicacao(self):
        return self.ano_publicacao
    
    def get_status(self):
        return self.status

    # Funções

    def exibir_livro(self):
        print("Título: ", self.titulo)
        print("Autor: ", self.autor)
        print("ISBN: ", self.isbn)
        print("Ano de Publicação: ", self.ano_publicacao)
        print("Status: ", self.status)

# funções do sistema

def limpar_terminal():
    os.system('clear')

def main():
    while True:
        opcao = menu_inicio()
        match(opcao):
            case 1:
                listar_autores()
                op_autor()
            case 2:
                listar_livros()
                op_livro()
            case 0:
                print("Obrigado por utilizar o sistema de biblioteca!")
                break
            case default:
                print("Opção inválida!")

def op_autor():
    while True:
        opcao = menu_op_autor()
        match(opcao):
            case 1:
                cadastrar_autor()
            case 2:
                editar_autor()
            case 3:
                excluir_autor()
            case 4:
                listar_autores()
            case 0:
                break
            case default:
                print("Opção inválida!")

def op_livro():
    while True:
        opcao = menu_op_livro()
        match(opcao):
            case 1:
                cadastrar_livro()
            case 2:
                editar_livro()
            case 3:
                excluir_livro()
            case 4:
                atualizar_status()
            case 5:
                listar_livros()
            case 0:
                break
            case default:
                print("Opção inválida!")

# -- Funções de autor

def listar_autores():
    print("Autores cadastrados:")
    for autor in autores:
        autor.exibir_autor()

def cadastrar_autor():
    limpar_terminal()
    panel = Panel("Preencha as informações do novo autor", title="Cadastro de Autor", border_style="bold green")
    console.print(panel)
    
    nome = Prompt.ask("Digite o nome do autor")
    nacionalidade = Prompt.ask("Digite a nacionalidade do autor")
    
    console.print(f"\n[bold]Informações do Autor:[/bold]\nNome: {nome}\nNacionalidade: {nacionalidade}\nData de Nascimento: {data_nascimento}", style="bold blue")

    autor = Autor(nome, nacionalidade)
    autores.append(autor)

def editar_autor():
    for autor in autores:
        nome = input("Digite o nome do autor que deseja editar (0 - sair): ")
        if autor.get_nome() == nome:
            nome = input("Digite o novo nome do autor: ")
            nacionalidade = input("Digite a nova nacionalidade do autor: ")
            autor.set_nacionalidade(nacionalidade)
            autor.set_nome(nome)
            console.print("[green]Autor editado com sucesso!")
            break
        elif nome == '0':
            break
        else:
            console.print("[red]Autor não encontrado!")

def excluir_autor():
    for autor in autores:
        nome = input("Digite o nome do autor que deseja excluir (0 - sair): ")
        if autor.get_nome() == nome:
            autores.remove(autor)
            console.print("[green]Autor excluído com sucesso!")
            break
        elif nome == '0':
            break
        else:
            console.print("[red]Autor não encontrado!")

def verificar_autor(autor_nome):
    for autor in autores:
        if autor.get_nome() == autor_nome:
            return True
    else:
        console.print("[red]Autor não encontrado!")
        op = input("Deseja cadastrar o autor? (s/n): ")
        if op == 's':
            nome = autor_nome
            nacionalidade = input("Digite a nacionalidade do autor: ")
            autor_ob = Autor(nome, nacionalidade)
            autores.append(autor_ob)
        else:
            return False

# -- Funções de livro

def listar_livros():
    print("Livros cadastrados:")
    for livro in livros:
        livro.exibir_livro()
        
def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    isbn = input("Digite o ISBN do livro: ")
    ano_publicacao = input("Digite o ano de publicação do livro: ")
    status = input("Digite o status do livro: ")
    autor = input("Digite o nome do autor do livro: ")
    livro = Livro(titulo, isbn, ano_publicacao, status, autor)
    livros.append(livro)
    console.print("[green]Livro cadastrado com sucesso!")
    verificar_autor(autor)

def editar_livro():
    for livro in livros:
        titulo = input("Digite o título do livro que deseja editar (0 - sair): ")
        if livro.get_titulo() == titulo:
            titulo = input("Digite o novo título do livro: ")
            isbn = input("Digite o novo ISBN do livro: ")
            ano_publicacao = input("Digite o novo ano de publicação do livro: ")
            status = input("Digite o novo status do livro: ")
            autor = input("Digite o novo autor do livro: ")
            livro.set_titulo(titulo)
            livro.set_isbn(isbn)
            livro.set_ano_publicacao(ano_publicacao)
            livro.set_status(status)
            livro.set_autor(autor)
            console.print("[green]Livro editado com sucesso!")
            verificar_autor(autor)
            break
        elif titulo == '0':
            break
        else:
            console.print("[red]Livro não encontrado!")

def excluir_livro():
    for livro in livros:
        titulo = input("Digite o título do livro que deseja excluir (0 - sair): ")
        if livro.get_titulo() == titulo:
            livros.remove(livro)
            console.print("[green]Livro excluído com sucesso!")
            break
        elif titulo == '0':
            break
        else:
            console.print("[red]Livro não encontrado!")

def atualizar_status():
    for livro in livros:
        titulo = input("Digite o título do livro que deseja atualizar o status (0 - sair): ")
        if livro.get_titulo() == titulo:
            status = input("Digite o novo status do livro: ")
            livro.set_status(status)
            console.print("[green]Status atualizado com sucesso!")
            break
        elif titulo == '0':
            break
        else:
            console.print("[red]Livro não encontrado!")

# menus

def menu_inicio():
    limpar_terminal()
    menu = """
    Bem-vindo ao sistema de biblioteca!

    1 - Listar autores
    2 - Listar livros
    0 - Sair
    """
    panel = Panel(menu, title="Menu Inicial", border_style="bold")
    console.print(panel)
    opcao = Prompt.ask("Digite a opção desejada", choices=["1", "2", "0"])
    return int(opcao)

def menu_op_livro():
    limpar_terminal()
    menu = """
    1 - Cadastrar livro
    2 - Editar livro
    3 - Excluir livro
    4 - Atualizar status
    5 - Relistar livros
    0 - Voltar
    """
    panel = Panel(menu, title="Menu de Livros", border_style="bold blue")
    console.print(panel)
    opcao = Prompt.ask("Digite a opção desejada", choices=["1", "2", "3", "4", "5", "0"])
    return int(opcao)

def menu_op_autor():
    limpar_terminal()
    menu = """
    1 - Cadastrar autor
    2 - Editar autor
    3 - Excluir autor
    4 - Relistar autores
    0 - Voltar
    """
    panel = Panel(menu, title="Menu de Autores", border_style="bold purple")
    console.print(panel)
    opcao = Prompt.ask("Digite a opção desejada", choices=["1", "2", "3", "4", "0"])
    return int(opcao)

main()