from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox
from services.crud import adicionar_livro, listar_livros, atualizar_livro, deletar_livro

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gerenciamento de Livros")
        self.setGeometry(100, 100, 500, 400)
        layout = QVBoxLayout()

        self.lista_livros = QListWidget(self)
        layout.addWidget(QLabel("Livros Cadastrados:"))
        layout.addWidget(self.lista_livros)
        self.carregar_livros()

        self.titulo_input = QLineEdit(self)
        self.titulo_input.setPlaceholderText("Título do Livro")
        layout.addWidget(QLabel("Título:"))
        layout.addWidget(self.titulo_input)

        self.autor_input = QLineEdit(self)
        self.autor_input.setPlaceholderText("Autor")
        layout.addWidget(QLabel("Autor:"))
        layout.addWidget(self.autor_input)

        self.paginas_input = QLineEdit(self)
        self.paginas_input.setPlaceholderText("Número de Páginas")
        layout.addWidget(QLabel("Páginas:"))
        layout.addWidget(self.paginas_input)

        self.ano_input = QLineEdit(self)
        self.ano_input.setPlaceholderText("Ano de Publicação")
        layout.addWidget(QLabel("Ano:"))
        layout.addWidget(self.ano_input)

        self.btn_adicionar = QPushButton("Adicionar Livro", self)
        self.btn_adicionar.clicked.connect(self.adicionar_livro)
        layout.addWidget(self.btn_adicionar)

        self.btn_atualizar = QPushButton("Atualizar Livro Selecionado", self)
        self.btn_atualizar.clicked.connect(self.atualizar_livro)
        layout.addWidget(self.btn_atualizar)

        self.btn_remover = QPushButton("Remover Livro Selecionado", self)
        self.btn_remover.clicked.connect(self.remover_livro)
        layout.addWidget(self.btn_remover)

        self.setLayout(layout)

    def carregar_livros(self):
        self.lista_livros.clear()
        livros = listar_livros()
        for livro in livros:
            self.lista_livros.addItem(f"{livro['id']} - {livro['titulo']} ({livro['autor']})")

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

        livro_id = item_selecionado.text().split(" - ")[0]
        novo_titulo = self.titulo_input.text()
        novo_autor = self.autor_input.text()
        novas_paginas = self.paginas_input.text()
        novo_ano = self.ano_input.text()

        atualizar_livro(livro_id, novo_titulo, novo_autor, novas_paginas, novo_ano)
        QMessageBox.information(self, "Sucesso", "Livro atualizado!")
        self.carregar_livros()

    def remover_livro(self):
        item_selecionado = self.lista_livros.currentItem()
        if not item_selecionado:
            QMessageBox.warning(self, "Erro", "Selecione um livro para remover!")
            return

        livro_id = item_selecionado.text().split(" - ")[0]
        deletar_livro(livro_id)
        QMessageBox.information(self, "Sucesso", "Livro removido!")
        self.carregar_livros()
