from entity.store import Store


store = Store(
    items={
        "печенька": 25,
        "собачка": 25,
        "елка": 25,
        "пончик": 3,
        "зонт": 5,
        "ноутбук": 1,
    }
)

shop = Shop(
    items={
        "печенька": 2,
        "собачка": 2,
        "елка": 2,
        "пончик": 1,
        "зонт": 1,
    }
)

storages = {
    "магазин": shop,
    "склад": store,
}


def main():
    print('\nДобрый день!\n')

    while True:
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')
        break


main()
