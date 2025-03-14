import sys
import os
from PyQt6.QtWidgets import QApplication
from ui.login import LoginWindow
from ui.register import RegisterWindow

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

def main():
    app = QApplication(sys.argv)

    login_window = LoginWindow()
    register_window = RegisterWindow()

    login_window.show_register_signal.connect(register_window.show)
    register_window.show_login_signal.connect(login_window.show)

    login_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
