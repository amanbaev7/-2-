'''Создать простое приложение с несколькими виджетами
Описание:
Создайте приложение, в котором будут использоваться следующие виджеты:

QLineEdit — для ввода текста.
QPushButton — для выполнения действия.
QLabel — для отображения результата.
QComboBox — для выбора опции.
QCheckBox — для включения/выключения параметра.
Требования:
Интерфейс:

Поле ввода (QLineEdit) — вводит текст.
Кнопка (QPushButton) — при нажатии отображает введённый текст в QLabel.
Выпадающий список (QComboBox) — содержит несколько цветов, например: "Красный", "Зелёный", "Синий".
Флажок (QCheckBox) — изменяет шрифт текста на жирный при активации.
Логика:

При нажатии на кнопку текст из QLineEdit должен отобразиться в QLabel.
При выборе цвета из QComboBox текст в QLabel должен меняться на соответствующий цвет.
Если флажок (QCheckBox) отмечен — текст должен становиться жирным.
Если флажок снят — текст возвращается к обычному стилю.
Подсказки:
Используйте метод setStyleSheet() для изменения цвета текста в QLabel.
Для изменения шрифта можно использовать QFont и метод setFont().
Событие currentIndexChanged для QComboBox можно привязать к обновлению цвета текста.'''

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox, QCheckBox
from PyQt6.QtGui import QFont

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Простое приложение")
        
        self.layout = QVBoxLayout()
        
        self.input_field = QLineEdit()
        self.layout.addWidget(self.input_field)
        
        self.button = QPushButton("Отобразить текст")
        self.button.clicked.connect(self.update_label)
        self.layout.addWidget(self.button)
        
        self.label = QLabel("Здесь будет текст")
        self.layout.addWidget(self.label)
        
        self.color_box = QComboBox()
        self.color_box.addItems(["Красный", "Зелёный", "Синий"])
        self.color_box.currentIndexChanged.connect(self.change_color)
        self.layout.addWidget(self.color_box)
        
        self.bold_checkbox = QCheckBox("Жирный шрифт")
        self.bold_checkbox.stateChanged.connect(self.toggle_bold)
        self.layout.addWidget(self.bold_checkbox)
        
        self.setLayout(self.layout)

    def update_label(self):
        self.label.setText(self.input_field.text())
    
    def change_color(self):
        colors = {"Красный": "red", "Зелёный": "green", "Синий": "blue"}
        selected_color = self.color_box.currentText()
        self.label.setStyleSheet(f"color: {colors[selected_color]};")
    
    def toggle_bold(self):
        font = self.label.font()
        font.setBold(self.bold_checkbox.isChecked())
        self.label.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleApp()
    window.show()
    sys.exit(app.exec())

