# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel
# app = QApplication(sys.argv)
# window = QWidget()
# window.setWindowTitle("пример PyQt6")
# window.resize(300, 200)

# ladel = QLabel ("привет мир", parent=window)
# ladel.move(100, 60)
    
       
# window.show()
# sys.exit(app.exec())

# """код номер 1"""


"""код номер 2"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self): 
        self.setWindowTitle("окно через класс")
        self.resize(300, 150)

        label = QLabel("окно создано через класс", self)
        label.move(10, 200)
    
    
def fort():
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    fort()
    