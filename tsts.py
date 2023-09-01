from PyQt6 import QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("FirstTry")
window.resize(300, 400)

label = QtWidgets.QLabel('<center>Hello Wordl!</center>')
btnQuit = QtWidgets.QPushButton("&закрыть окно")

vbox = QtWidgets.QVBoxLayout()

vbox.addWidget(label)
vbox.addWidget(btnQuit)

window.setLayout(vbox)

btnQuit.clicked.connect(app.quit)

window.show()


sys.exit(app.exec())
