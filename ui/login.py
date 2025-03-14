from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtCore import pyqtSignal
from services.auth import login_usuario
from ui.styles import get_styles

class LoginWindow(QWidget):
    login_successful_signal = pyqtSignal() 
    show_register_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet(get_styles())

        layout = QVBoxLayout()

        titulo_label = QLabel("Faça seu Login")
        titulo_label.setStyleSheet("font-size: 18px; font-weight: bold; text-align: center;")
        layout.addWidget(titulo_label)

        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Email")
        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_input)

        self.senha_input = QLineEdit(self)
        self.senha_input.setPlaceholderText("Senha")
        self.senha_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(QLabel("Senha:"))
        layout.addWidget(self.senha_input)

        self.btn_login = QPushButton("Login", self)
        self.btn_login.clicked.connect(self.fazer_login)
        layout.addWidget(self.btn_login)

        self.btn_registrar = QPushButton("Registrar", self)
        self.btn_registrar.clicked.connect(self.mostrar_registro)
        layout.addWidget(self.btn_registrar)

        self.setLayout(layout)

    def fazer_login(self):
        email = self.email_input.text()
        senha = self.senha_input.text()

        if not email or not senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos!")
            return

        sucesso, mensagem = login_usuario(email, senha)
        if sucesso:
            QMessageBox.information(self, "Sucesso", "Login realizado com sucesso!")
            self.login_successful_signal.emit()
            self.close()
        else:
            QMessageBox.warning(self, "Erro", mensagem)

    def mostrar_registro(self):
        self.show_register_signal.emit()
