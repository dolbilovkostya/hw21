from entity.abstract_storage import AbstractStorage


class Store(AbstractStorage):
    def __init__(self, items: dict, capacity: int = 100):
        self.__items = items
        self.__capacity = capacity
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_free_space() < amount:
            print('Не хватает места')
            return

    def remove(self, name: str, amount: int) -> None:
        pass

    def get_free_space(self) -> int:
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items
