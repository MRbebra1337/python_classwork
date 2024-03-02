class Cat:
    def __init__(self, name: str = "MEGAKOT", age: int = 0, milk: int = 100):
        self.name = name
        self.age = age
        self.milk = milk

    def eat(self, food: int):
            self.milk -= food
            if self.milk < 0:
                self.milk = 0
            print(f"{self.name} drank. Milk: {self.milk}")