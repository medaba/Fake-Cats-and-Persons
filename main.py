# -*- coding: utf-8 -*-


# Скрипт для получения фотографий несуществующих людей/котов.
# Фотографии создаются с помощью запроса к API нейросети,
# которая генерирует по одному фото в три секунды.


import time
from thisapidoesnotexist import get_cat, get_person

from utils import generate_filename


def get_cats(amount):
    """Получить фото несуществующих котов
       и сохранить их в папку "cats/".

       Количество фоток задается параметром amount.
       """
    for i in range(amount):
        cat = get_cat()
        cat.save_image(f"cats/{generate_filename()}")
        time.sleep(3)


def get_persons(amount):
    """Получить фото несуществующих людей
       и сохранить их в папку "persons/".

       Количество фоток задается параметром amount.
       """
    for i in range(amount):
        person = get_person()
        person.save_image(f"persons/{generate_filename()}")
        time.sleep(3)


if __name__ == '__main__':
    get_cats(10)
    # get_persons(10)
