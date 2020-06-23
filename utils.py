# -*- coding: utf-8 -*-

from string import ascii_letters, digits
import random


def generate_filename(lenght=6):
    """Создание рандомного имени файла.
    """
    chars = ascii_letters + digits
    filename = ''.join(random.choice(chars) for x in range(lenght))

    return filename
