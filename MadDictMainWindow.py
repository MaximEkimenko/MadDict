# Form implementation generated from reading ui file 'D:\АСУП\Python\Projects\MadDict\MadDictMainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 448)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_question = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        self.label_question.setFont(font)
        self.label_question.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_question.setObjectName("label_question")
        self.horizontalLayout.addWidget(self.label_question)
        self.button_say = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_say.setObjectName("button_say")
        self.horizontalLayout.addWidget(self.button_say)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.edit_input_answer = QtWidgets.QLineEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.edit_input_answer.setFont(font)
        self.edit_input_answer.setObjectName("edit_input_answer")
        self.verticalLayout.addWidget(self.edit_input_answer)
        self.button_check = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.button_check.setFont(font)
        self.button_check.setObjectName("button_check")
        self.verticalLayout.addWidget(self.button_check)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.textedit_answer = QtWidgets.QTextEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.textedit_answer.setFont(font)
        self.textedit_answer.setObjectName("textedit_answer")
        self.horizontalLayout_2.addWidget(self.textedit_answer)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.button_next = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.button_next.setFont(font)
        self.button_next.setObjectName("button_next")
        self.verticalLayout_3.addWidget(self.button_next)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_repeats = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_repeats.setFont(font)
        self.label_repeats.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_repeats.setObjectName("label_repeats")
        self.horizontalLayout_3.addWidget(self.label_repeats)
        self.label_correct = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_correct.setFont(font)
        self.label_correct.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_correct.setObjectName("label_correct")
        self.horizontalLayout_3.addWidget(self.label_correct)
        self.label_words_total = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_words_total.setFont(font)
        self.label_words_total.setObjectName("label_words_total")
        self.horizontalLayout_3.addWidget(self.label_words_total)
        self.label_words_studied = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_words_studied.setFont(font)
        self.label_words_studied.setObjectName("label_words_studied")
        self.horizontalLayout_3.addWidget(self.label_words_studied)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 655, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_question.setText(_translate("MainWindow", "TextLabel"))
        self.button_say.setText(_translate("MainWindow", "say"))
        self.button_check.setText(_translate("MainWindow", "check"))
        self.button_next.setText(_translate("MainWindow", "next"))
        self.label_repeats.setText(_translate("MainWindow", "TextLabel"))
        self.label_correct.setText(_translate("MainWindow", "TextLabel"))
        self.label_words_total.setText(_translate("MainWindow", "TextLabel"))
        self.label_words_studied.setText(_translate("MainWindow", "TextLabel"))
