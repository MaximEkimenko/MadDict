import os
import pyaudio
import wave


def say_word(file_name: str) -> None:
    """
    Запускает аудио с именем file_name
    :param file_name: строка имени файла
    :return:
    """
    file_path = rf'{os.getcwd()}\audio'  # путь к папке хранения audio файлов
    audio_file = wave.open(file_path + '\\' + file_name + '.wav')  # открытие файла
    FORMAT = audio_file.getsampwidth()  # глубина звука
    CHANNELS = audio_file.getnchannels()  # количество каналов
    RATE = int(audio_file.getframerate() / 2)  # частота дискретизации
    N_FRAMES = audio_file.getnframes()  # кол-во отсчетов
    audio = pyaudio.PyAudio()  # объект работы с аудио
    # поток для записи на устройство вывода - динамик
    out_stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, output=True)
    out_stream.write(audio_file.readframes(N_FRAMES))  # воспроизведение
    audio.terminate()  # закрытие объекта


def check_answer(answer: str, right_answer: str) -> bool:
    """
    Проверяет наличие ответа answer в строке right_answer
    :param answer: предлагаемый ответ
    :param right_answer: строка верных ответов
    :return: bool
    """
    right_answer_list = right_answer.split(',')
    answer = answer.strip().lower()
    if answer in right_answer_list:
        return True
    else:
        return False


def answer_string_prepare(right_answer: str) -> str:
    """
    Подготавливает строку ответов к выводу на экран
    :param right_answer: строка ответов
    :return: right_answer
    """
    right_answer_list = right_answer.split(",")  # список из строки
    right_answer_list = set(right_answer_list)  # удаление повторов
    right_answer = '\n'.join(right_answer_list)  # объединение в строку
    return right_answer


if __name__ == '__main__':
    # say_word('A good rule of thumb')
    # print(check_answer(answer='навлечь на себя',
    #                    right_answer='нести,подвергаться,навлечь на себя,навлекать на себя'))
    answer_string_prepare('обобщать,обобщать,распространять,делать общие выводы,сводить к общим законам,'
                          'говорить в общей форме,говорить неопределенно,придавать неопределенность,'
                          'вводить в общее употребление')
