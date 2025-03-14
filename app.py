import sys
import os
from PyQt6.QtWidgets import QApplication
from ui.login import LoginWindow
from ui.main import MainWindow

def main():
    app = QApplication(sys.argv)

    login_window = LoginWindow()
    main_window = MainWindow()

    login_window.login_successful_signal.connect(main_window.show)

    login_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()