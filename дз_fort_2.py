'''Создайте своё первое окно с помощью PyQt6. Используйте класс и метод setup_ui() для настройки интерфейса.

В окне должно быть:

Заголовок окна — любой, придумайте свой.
Размер окна — 400x200.
Два элемента QLabel:
Первый — с текстом "Добро пожаловать!"
Второй — с вашим именем или вымышленным ником.
Разместите их в разных частях окна (например, один слева сверху, другой справа снизу).'''

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self): 
        self.setWindowTitle("Моё первое окно")
        self.resize(400, 200)

        label1 = QLabel("Добро пожаловать!", self)
        label1.move(10, 10)

        label2 = QLabel("amanbaev_7", self)
        label2.move(300, 150)
def fort():
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    fort()
        
        