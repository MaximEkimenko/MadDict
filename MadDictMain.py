import os
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
# импорт gui main window
from MadDictMainWindow import Ui_MainWindow
# работа с базой excel
from exl_base import get_random_line, update_line
# функции дял кнопок
from mad_dict_funcs import say_word, check_answer, answer_string_prepare

# TODO перевести на sqlite
# TODO сделать кнопку "закончить урок"
# TODO сделать статистику урока (сессии) после запуска и показывать её при выходе по кнопке "закончить"
# TODO сделать подменю с изученными словами и кнопкой, чтобы изучать их снова
# TODO сделать красивый дизайн
# TODO перевести в мобильное приложение
# TODO сделать при запуске урока ограничение в объеме интервала выбираемых слов - ограничить рандом
# TODO сделать асинхронным для одновременного произношения, переключения и ответа
# TODO сделать git


class MadDict(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.base_path = rf'{os.getcwd()}\MadDictBase.xlsx'  # база слов

        # значения по умолчанию
        # случайная строка из словаря, ряд строки
        self.random_line, self.base_row, self.words_total, self.words_studied = get_random_line(self.base_path)
        self.ui.label_question.setText(self.random_line[0])  # выбор случайного слова при запуске
        self.ui.label_repeats.setText(str(self.random_line[2]))  # количество повторов
        self.ui.label_correct.setText(str(self.random_line[3]))  # количество верных повторов
        self.ui.label_words_total.setText(str(self.words_total))  # количество слов в словаре
        self.ui.label_words_studied.setText(str(self.words_studied))  # количество слов в словаре
        self.ui.edit_input_answer.setFocus()  # фокус на полее ввода ответа
        self.ui.button_next.setEnabled(False)  # кнопка далее неактивна

        # сигналы
        self.ui.button_say.clicked.connect(self.button_say_click)  # кнопка say
        self.ui.button_check.clicked.connect(self.button_check_click)  # кнопка check клик
        self.ui.edit_input_answer.returnPressed.connect(self.button_check_click)  # кнопка check на enter
        self.ui.button_next.clicked.connect(self.button_next_click)  # кнопка next

    # слоты
    def button_say_click(self):  # произношение слова
        say_word(self.ui.label_question.text())

    def button_check_click(self):  # проверка слова
        try:
            if self.ui.edit_input_answer.text():  # если введён текст ответа
                self.ui.textedit_answer.clear()  # очистка вывода
                if check_answer(self.ui.edit_input_answer.text(), self.random_line[1]):  # если верно
                    # self.ui.textedit_answer.append('Верно!')
                    self.ui.textedit_answer.append(answer_string_prepare(self.random_line[1]))  # вывод ответов
                    self.ui.textedit_answer.setStyleSheet("background-color: #9CFFD3")  # подкраска зелёным

                    update_line(excel_file=self.base_path, col_letter='D', base_row=self.base_row,
                                value=int(self.random_line[3]) + 1)
                    if self.ui.textedit_answer:  # включение/отключение кнопки next
                        self.ui.button_next.setEnabled(True)
                    else:
                        self.ui.button_next.setEnabled(False)
                    say_word(self.random_line[0])  # повтор произношения
                else:
                    self.ui.textedit_answer.append(answer_string_prepare(self.random_line[1]))  # вывод ответов
                    self.ui.textedit_answer.setStyleSheet("background-color: #FF5555")  # подкраска красным
                    if self.ui.textedit_answer:  # включение/отключение кнопки next
                        self.ui.button_next.setEnabled(True)
                    else:
                        self.ui.button_next.setEnabled(False)
                    say_word(self.random_line[0])  # повтор произношения
            else:
                self.ui.textedit_answer.append('Введите ответ!')
        except Exception as e:
            print(e)

    def button_next_click(self):  # кнопка next
        self.ui.button_next.setEnabled(False)  # отключение после нажатия
        # новая случайная строка
        self.random_line, self.base_row, self.words_total, self.words_studied = get_random_line(self.base_path)
        self.ui.label_question.setText(self.random_line[0])  # слово
        self.ui.label_repeats.setText(str(self.random_line[2]))  # количество повторов
        self.ui.label_correct.setText(str(self.random_line[3]))  # количество верных повторов
        self.ui.label_words_total.setText(str(self.words_total))  # количество слов в словаре
        self.ui.label_words_studied.setText(str(self.words_studied))  # количество слов в словаре
        self.ui.textedit_answer.setStyleSheet("background-color: #FFFFFF")  # подкраска белым
        self.ui.textedit_answer.clear()  # очистка поля ответов
        self.ui.edit_input_answer.clear()  # очистка поля ввода
        say_word(self.random_line[0])  # произношение слова


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    window = MadDict()  # create GUI window
    window.show()  # show GUI
    sys.exit(app.exec())
