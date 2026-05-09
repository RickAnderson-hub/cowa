class Inventory:
    def __init__(self, items: list = None, registry: dict = None):
        self._items: list[str] = list(items) if items else []
        self._registry: dict = registry or {}

    def add(self, item_id: str) -> bool:
        if item_id not in self._items:
            self._items.append(item_id)
            return True
        return False

    def remove(self, item_id: str) -> bool:
        if item_id in self._items:
            self._items.remove(item_id)
            return True
        return False

    def has(self, item_id: str) -> bool:
        return item_id in self._items

    def to_list(self) -> list[str]:
        return list(self._items)

    def display(self):
        from display import print_inventory
        print_inventory(self._items, self._registry)

    def item_name(self, item_id: str) -> str:
        return self._registry.get(item_id, {}).get("name", item_id)
