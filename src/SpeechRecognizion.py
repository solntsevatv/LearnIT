"""
    \file SpeechRecognizion.py
    \brief Модуль для распознавания текста.
"""
import speech_recognition as speech_recog
import requests

# Константы
FOLDER_ID = "b1gutqa0oss26suk1ra9"  # Идентификатор каталога
YANDEX_API_KEY = "AQVN16bFsGY7plN0WCv-vAVpHtuEBESvNj27YZt-" #Api-Key для соединения с Яндексом
SIZE_AUDIO = 1024 ** 2

req_params = "&".join(["topic=general", "folderId=%s" % FOLDER_ID,
    "lang=ru-RU", "format=lpcm", "sampleRateHertz=48000"])
url_base = "https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?{}".format(req_params)

def read_audio(SIZE_AUDIO: int, record_d: bytes) -> bytes:
    """
    Функция создания последовательности маленьких аудио из большого аудио.

    Функция принимает на вход размер одного маленького аудио и само аудио.
    Возвращается генератор из коротких аудио нужной размерности.

    Предназначается для отправления коротких сообщений Яндексу
    """

    while True:
        Audio = record_d[:SIZE_AUDIO]
        record_d = record_d[SIZE_AUDIO:]

        yield Audio

        if not bytes:
            break

def Record() -> None:
    """
    Функция записи аудио

    Функция ничего не принимает на вход. Она начинает запись сообщения человека, после чего
    записывает его голос во временный файл.
    """
    
    recog = speech_recog.Recognizer()
    mic = speech_recog.Microphone()

    with mic as audio_file:
        audio = recog.listen(audio_file)
        with open("audio.wav", "wb") as file_wav:
            file_wav.write(audio.get_wav_data())

def Speech_to_Text() -> str:
    """
    Функция расшифровки голосового сообщения в текст

    Функция открывает временный файл, откуда считывает информацию, после чего отправляет её на сервера Яндекс.
    Потом она обрабатывает ответы Яндекса и возвращает всё это единым текстом.
    """

    with open("audio.wav", "rb") as f:
        record_data = f.read()

    record_data = read_audio(SIZE_AUDIO, record_data)
    params = "&".join(
        ["topic=general",
         "folderId=%s" % FOLDER_ID,
         "lang=ru-RU",
         "format=lpcm",
         "sampleRateHertz=48000"])

    url_base = "https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?{}".format(params)
    text = ""
    for records in record_data:
        url_request = requests.post(url_base, headers={"Authorization": "Api-Key {}".format(YANDEX_API_KEY)}, data=records).json()
        if url_request.get("result") is not None:
            text+=(url_request.get("result") + " ")
        else:
            break
    return text
