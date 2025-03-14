from PyQt6.QtWidgets import QApplication
from ui.login import LoginWindow
from ui.register import RegisterWindow
from ui.main import MainWindow

def main():
    app = QApplication([])

    login_window = LoginWindow()
    register_window = RegisterWindow()
    main_window = MainWindow()

    login_window.show_register_signal.connect(register_window.show)
    register_window.show_login_signal.connect(login_window.show)
    login_window.login_successful_signal.connect(main_window.show)
    login_window.login_successful_signal.connect(login_window.close)
    main_window.voltar_login_signal.connect(login_window.show)

    login_window.show()
    app.exec()

if __name__ == "__main__":
    main()