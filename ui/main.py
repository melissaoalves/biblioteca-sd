from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem,
    QMessageBox, QGridLayout, QHBoxLayout
)
from services.crud import adicionar_livro, listar_livros, atualizar_livro, deletar_livro
from ui.styles import get_styles
from PyQt6.QtCore import pyqtSignal

class MainWindow(QWidget):
    voltar_login_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gerenciamento de Livros")
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet(get_styles())

        main_layout = QVBoxLayout()

        titulo_label = QLabel("Gerenciamento de Livros")
        titulo_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        main_layout.addWidget(titulo_label)

        self.lista_livros = QListWidget(self)
        main_layout.addWidget(QLabel("Livros Cadastrados:"))
        main_layout.addWidget(self.lista_livros)
        self.carregar_livros()

        form_layout = QGridLayout()

        self.titulo_input = QLineEdit(self)
        self.titulo_input.setPlaceholderText("Título do Livro")
        form_layout.addWidget(QLabel("Título:"), 0, 0)
        form_layout.addWidget(self.titulo_input, 0, 1)

        self.autor_input = QLineEdit(self)
        self.autor_input.setPlaceholderText("Autor")
        form_layout.addWidget(QLabel("Autor:"), 1, 0)
        form_layout.addWidget(self.autor_input, 1, 1)

        self.paginas_input = QLineEdit(self)
        self.paginas_input.setPlaceholderText("Número de Páginas")
        form_layout.addWidget(QLabel("Páginas:"), 2, 0)
        form_layout.addWidget(self.paginas_input, 2, 1)

        self.ano_input = QLineEdit(self)
        self.ano_input.setPlaceholderText("Ano de Publicação")
        form_layout.addWidget(QLabel("Ano:"), 3, 0)
        form_layout.addWidget(self.ano_input, 3, 1)

        main_layout.addLayout(form_layout)

        btn_layout = QHBoxLayout()
        self.btn_adicionar = QPushButton("Adicionar Livro", self)
        self.btn_adicionar.clicked.connect(self.adicionar_livro)
        btn_layout.addWidget(self.btn_adicionar)

        self.btn_atualizar = QPushButton("Atualizar", self)
        self.btn_atualizar.clicked.connect(self.atualizar_livro)
        btn_layout.addWidget(self.btn_atualizar)

        self.btn_remover = QPushButton("Remover", self)
        self.btn_remover.clicked.connect(self.remover_livro)
        btn_layout.addWidget(self.btn_remover)

        main_layout.addLayout(btn_layout)

        self.btn_sair = QPushButton("Sair", self)
        self.btn_sair.clicked.connect(self.voltar_para_login)
        main_layout.addWidget(self.btn_sair)

        self.setLayout(main_layout)

    def voltar_para_login(self):
        self.close()
        self.voltar_login_signal.emit() 

    def carregar_livros(self):
        self.lista_livros.clear()
        livros = listar_livros()

        for livro in livros:
            livro_id = livro.get("id")
            titulo = livro.get("titulo", "Título Desconhecido")
            autor = livro.get("autor", "Autor Desconhecido")
            ano = livro.get("ano", "Ano Desconhecido")
            paginas = livro.get("paginas", "Páginas Desconhecidas")

            item_texto = f"{titulo} ({autor}) - Ano: {ano} | Páginas: {paginas}"
            
            list_item = QListWidgetItem(item_texto)  
            list_item.setData(32, livro_id)

            self.lista_livros.addItem(list_item)


    def adicionar_livro(self):
        titulo = self.titulo_input.text()
        autor = self.autor_input.text()
        paginas = self.paginas_input.text()
        ano = self.ano_input.text()

        if not titulo or not autor or not paginas or not ano:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos!")
            return

        adicionar_livro(titulo, autor, paginas, ano)
        QMessageBox.information(self, "Sucesso", "Livro cadastrado com sucesso!")
        self.carregar_livros()

    def atualizar_livro(self):
        item_selecionado = self.lista_livros.currentItem()
        if not item_selecionado:
            QMessageBox.warning(self, "Erro", "Selecione um livro para atualizar!")
            return

        livro_id = item_selecionado.data(32)
        novo_titulo = self.titulo_input.text()
        novo_autor = self.autor_input.text()
        novas_paginas = self.paginas_input.text()
        novo_ano = self.ano_input.text()

        sucesso, mensagem = atualizar_livro(livro_id, novo_titulo, novo_autor, novas_paginas, novo_ano)

        if sucesso:
            QMessageBox.information(self, "Sucesso", "Livro atualizado!")
            self.carregar_livros()
        else:
            QMessageBox.warning(self, "Erro", mensagem)

    def remover_livro(self):
        item_selecionado = self.lista_livros.currentItem()
        if not item_selecionado:
            QMessageBox.warning(self, "Erro", "Selecione um livro para remover!")
            return

        livro_id = item_selecionado.data(32)
        sucesso, mensagem = deletar_livro(livro_id)

        if sucesso:
            QMessageBox.information(self, "Sucesso", "Livro removido!")
            self.carregar_livros()
        else:
            QMessageBox.warning(self, "Erro", mensagem)