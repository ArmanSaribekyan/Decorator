import json
from collections import Counter
from datetime import datetime
from typing import Callable


def fabric_decor_log(log_file):
    def decor_log(function: Callable):
        def new_function(*args, **kwargs):
            with open(log_file, 'a+', encoding='utf-8') as f:
                f.write(f'Datetime of function call: {datetime.now()},\n')
                f.write(f'Function name: {function.__name__},\n')
                f.write(f'Arguments: {args} и {kwargs},\n')
                f.write(f'Return value: {function(*args, **kwargs)};\n\n')
            # return function()
        return new_function
    return decor_log


@fabric_decor_log('logger.txt')
def top():
    with open("newsafr.json", encoding="utf-8") as f:
        json_data = json.load(f)

    descriptions = json_data["rss"]["channel"]["items"]

    list_of_descriptions = []  # список для слов, в которых больше 6 букв

    for description in descriptions:
        news = description["description"].split()
        for word in news:
            if len(word) > 6:
                list_of_descriptions.append(word)

    top = Counter(list_of_descriptions)
    print("Топ 10 самых часто встречающихся в новостях слов длиннее"
          " 6 символов:")
    for num_, word_count in enumerate(top.most_common(10), 1):
        # Возвращаем список из 10 наиболее распространенных слов
        # и их количество от наиболее к наименее распространенным
        print(f'{str(num_)} - {word_count[0]} ({word_count[1]} слов)')

if __name__ == '__main__':
    top()
