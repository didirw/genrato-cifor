#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(QApplication,QWidget,QPushButton,QLabel,QVBoxLayout)
from random import randint

def show_winer():
    num = randint(1,500000000)
    number.setText(str(num))


app = QApplication([])
Window = QWidget()
v_line = QVBoxLayout()
q =QLabel('Нажми,чтобы узнать победителя')
number=QLabel('?')
button = QPushButton('генирация')
button.clicked.connect(show_winer)


v_line.addWidget(q)
v_line.addWidget(number)
v_line.addWidget(button)


Window.setLayout(v_line)
Window.show()
app.exec()
#привязка элементов к вертикальной линии

#обработка событий

#запуск приложения