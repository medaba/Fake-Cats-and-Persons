# -*- coding: utf-8 -*-

# Скрипт для получения фотографий несуществующих людей/котов.
# Фотографии создаются на стороннем сервисе с помощью нейросети
# а мы их просто скачиваем по API.
# Сервис генерирует по 1 фото в 3 сек., поэтому в ф-ях стоит пауза 3 сек.


import asyncio
from thisapidoesnotexist import get_cat, get_person
from argparse import ArgumentParser

from utils import generate_filename


parser = ArgumentParser(description="ThisApiDoesNotExist")

parser.add_argument(
    '-a', '--amount',
    type=int,
    required=True,
    metavar='',
    help=('количество фотографий.')
)

parser.add_argument(
    '-c', '--cats',
    action='store_true',
    help=('разрешить закачку нейрокотов.')
)

parser.add_argument(
    '-p', '--people',
    action='store_true',
    help=('разрешить закачку несуществующих людей.')
)

args = parser.parse_args()


async def get_cats(amount):
    """Получить фото несуществующих котов
       и сохранить их в папку "cats/".

       Количество фоток задается параметром amount.
       """
    for i in range(amount):
        cat = get_cat()
        cat.save_image(f"cats/{generate_filename()}")
        await asyncio.sleep(3)


async def get_persons(amount):
    """Получить фото несуществующих людей
       и сохранить их в папку "persons/".

       Количество фоток задается параметром amount.
       """
    for i in range(amount):
        person = get_person()
        person.save_image(f"persons/{generate_filename()}")
        await asyncio.sleep(3)


async def main(amount, cats=False, persons=False):
    tasks = []
    if cats:
        tasks.append(get_cats(amount))
    if persons:
        tasks.append(get_persons(amount))

    if not tasks:
        raise ValueError

    # TODO: добавить в jupyter описание для asyncio.gather и asyncio.wait
    # await asyncio.gather(get_cats(amount), get_persons(amount))
    # await asyncio.wait([get_cats(amount), get_persons(amount)])
    await asyncio.wait(tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(args.amount, args.cats, args.people))
