class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happiness = 10

    def feed(self):
        self.hunger -= 1
        self.happiness += 1
        print(f"{self.name} ситий(а) і щасливий(а)!")

    def play(self):
        self.happiness += 2
        print(f"{self.name} весело грає!")

    def sleep(self):
        print(f"{self.name} спить...")

    def mood(self):
        if self.hunger > 3:
            print(f"{self.name} голодний(а)")
        if self.happiness < 5:
            print(f"{self.name} нещасливий(а)")

pet = Cat("Мурзик")

pet.feed()
pet.play()
pet.mood()