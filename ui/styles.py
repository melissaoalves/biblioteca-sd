def get_styles():
    return """
        QWidget {
            background-color: #f4f4f4;
            font-size: 14px;
            font-family: Arial;
        }
        QPushButton {
            background-color: #2E86C1;
            color: white;
            padding: 8px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #1F618D;
        }
        QLineEdit {
            border: 1px solid #1F618D;
            padding: 5px;
            border-radius: 4px;
            color: #1F618D;  /* Cor do texto dentro do input */
        }
        QLabel {
            font-weight: bold;
            color: #1F618D;  /* Cor do texto */
        }
        QListWidget {
            background-color: white;
            border: 1px solid #ccc;
            padding: 5px;
            color: #1F618D;  /* Cor do texto na lista */
        }
    """
