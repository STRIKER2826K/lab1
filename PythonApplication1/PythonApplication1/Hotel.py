class Hotel:
    def __init__(self, name: str, allplace: int, ocplace: int, price: float):
        self.name = name
        self.allplace = allplace
        self.ocplace = ocplace
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_allplace(self) -> int:
        return self.allplace

    def get_ocplace(self) -> int:
        return self.ocplace

    def get_price(self) -> float:
        return self.price

    def revenue(self) -> float:
        return self.price * self.ocplace
