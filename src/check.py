"""
    \file check.py
    \brief Модуль для постобработки текста.
"""
import re
from num2words import num2words
from typing import Tuple


def check_text(my_text: str, right_text: str) -> Tuple[bool, dict, list, int, int]:
    """
    Основная функция проверки текста

    На первом этапе регистр всех букв в текстах делается маленьким,
    далее выполнется удаление всех знаков препинания из текстов между которыми происходит сравнение,
    далее в тексте пользователя числа заменяются словами.

    На втором этапе происходит сранение двух текстов и поиск ошибок.

    На третьем этапе высчитвается процент ошибок, а именно
    процент слов, сказанных неправильно и процент пропущенных слов, 
    а также выводится результат удачная ли была попытка.

    Возвращает результат, словарь ошибок, массив пропущенных слов,
    процент ошибок, процент пропущенных слов
    """

    my_text = my_text.lower()
    my_text = my_text.replace('ё', 'е')
    my_text = list(filter(None, re.split("\W", my_text)))
    my_text = replace_numbers(my_text)

    right_text = right_text.lower()
    right_text = right_text.replace('ё', 'е')
    right_text = list(filter(None, re.split("\W", right_text)))

    #Поиск ошибок
    error, miss_words = check_word(my_text, right_text)
    #Перевод в проценты, результат 
    per_miss_words, per_error, Result = check_mistake(error, miss_words, right_text, my_text)

    return Result, error, miss_words, per_error, per_miss_words 

def check_word(my_text: str, right_text: str) -> Tuple[dict, list]:
    """
    Функция поиска ошибок

    Первым этапом функция высчитвает максимальное количество пропущенных пользователем слов,
    далее выбирает самый короткий текст, по которому будет идти цикл

    На втором этапе в цикле функция ищеь несовпадающие или пропущенные слова и добавляет их
    соответственнов в словарь и массив

    Возвращает словарь ошибок и массив пропущенных слов
    """

    error = {}
    miss_words = []

    #Задаём максимальное количество пропущенных/лишних слов
    max_array_offset = len(right_text) - len(my_text)
    #задаем "отставание", если есть пропущенные слова
    array_offset = 0


    if max_array_offset < 0:
        #Чтобы цикл был по самому короткому тексту
        my_text, right_text = right_text, my_text
        max_array_offset = abs(max_array_offset)

    k = 0
    for i in range(len(my_text)):
        max_array_offset -= array_offset
        array_offset = 0
        if my_text[i] != right_text[k]:
            while (
                my_text[i] != right_text[k + array_offset]
                and array_offset < max_array_offset
            ):
                array_offset += 1
            if my_text[i] == right_text[k + array_offset]: 
                for j in range(k, k + array_offset):
                    miss_words.append(right_text[j])
                k += array_offset
            else:
                array_offset = 0
                error[right_text[k]] = my_text[i]
        k+=1
    return error, miss_words    

    
# Проверка на количесво ошибок
def check_mistake(error: dict, miss_words: list, right_text: str, my_text: str) -> Tuple[int, int, bool]:
    per_miss_words =(len(right_text) - len(my_text))  / len(right_text)
    per_error = len(error) / len(right_text)

    if per_miss_words > 0.1 + 0.0001 or per_error > 0.1 + 0.0001:
        return  round(100*per_miss_words), round(100*per_error), False
    else:
        return round(100*per_miss_words), round(100*per_error), True

'''
Функция замены чисел на слова

Данная функция циклом проходится по всему тексту и с помощью
библиотеки num2words заменяет числа словами
'''
# Числа записываем словами
def replace_numbers(text: str) -> str:
    for i in range(len(text)):
        if text[i].isdigit():
            text[i] = num2words(int(text[i]), lang="ru")
    return text

if __name__ == "__main__":
    my_text = "привет привет привет"

    right_text= "..Закрученным веером брызги пуская, \
мой пёс отряхнулся у самой воды, апорт сквозь запахи мая пронесся, в песок забивая следы. \
Счастливый! Дай мокрую шкуру потрогать, \
почуять как в руку уткнулся твой нос, \
вот этого полдня и брызг этих ради \
я, может, и жил-то.\
Как думаешь, пёс ?"

    #Выводитсся правильно/неправильно, все ошибки, все пропущенные слова, процент ошибок, процент пропущенных слов
    print(check_text(my_text, right_text))
