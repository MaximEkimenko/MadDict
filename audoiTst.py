import pyaudio
import wave
from pydub import AudioSegment, silence
chunk = 512 # Запись кусками по битам сэмпла
sample_format = pyaudio.paInt16 # 16 бит на выборку
channels = 1 # моно канал 
rate = 16000 # Запись со скоростью 44100 выборок(samples) в секунду
seconds = 5# TODO как вычислить время длительности записи по длине строки?
path = r'D:\АСУП\Python\Projects\MadDict\audio' + '\\' #путь к файлу 
filename = path + r'output_sound.wav'      # + word + '.wav' # имя файла
p = pyaudio.PyAudio() # Создать интерфейс для PortAudio
print('Recording...', filename)

stream = p.open(format=sample_format, # создание потока
                channels=channels,
                rate=rate,
                frames_per_buffer=chunk,
                input_device_index=1, # индекс устройства с которого будет идти запись звука 
                input=True)
frames = [] # Инициализировать массив для хранения кадров
# Хранить данные в блоках в течение seconds секунд
for i in range(0, int(rate / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)
# Остановить и закрыть поток
stream.stop_stream(); stream.close()
# Завершить интерфейс PortAudio
p.terminate()
print('Finished recording! ',filename)
# Сохранить записанные данные в виде файла WAV
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(rate)
wf.writeframes(b''.join(frames))
wf.close()

# обрезание пустоты в файле записи (сокращение файла)
sound = AudioSegment.from_file(filename, format="wav") # открытие только что записанного файла
timeList = silence.detect_nonsilent(sound,silence_thresh=-200,seek_step=5) # получение НЕ пустот в начало, конец в мс
# сохранение в тот же файл среза без пустот
sliceRez = sound[timeList[0][0]:timeList[0][1]+500] 
sliceRez.export(filename, format="wav")







