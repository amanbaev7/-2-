# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
# import sys

# class MyWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setup_ui()
        
#     def setup_ui(self):
#         self.setWindowTitle("пример QPushButton")
#         self.resize(300, 200)
        
        
#         button = QPushButton("нажми меня", self)
#         button.move(100, 80)
        
#         button.clicked.connect(self.button_clicked)
        
        
#     def button_clicked(self):
#         print("нажата кнопка")
        
# app = QApplication(sys.argv)
# window = MyWidget()
# window.show()
# sys.exit(app.exec())

  
  
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        self.setWindowTitle("пример QPushButton")
        self.resize(300, 200)
        
        
        self.text_input = QLineEdit(self)
        self.text_input.move(50, 50)
        
        button = QPushButton("показать текст", self)
        button.move(50, 90)
        button.clicked.connect(self.show_text)
        
    def show_text(self):
        text = self.text_input.text()
        print("введенный текст:", text)
        
app = QApplication(sys.argv)
window = MyWidget()
window.show()  
sys.exit(app.exec())

        

        
        