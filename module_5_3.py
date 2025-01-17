class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __eq__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
    def __add__(self, other):
        return self.number_of_floors + other
    def __radd__(self, other):
        return self.number_of_floors + other
    def __iadd__(self, other):
        return self.number_of_floors + other
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1.number_of_floors == h2.number_of_floors)

h1.number_of_floors = h1.number_of_floors + 10
print(h1)
print(h1.number_of_floors == h2.number_of_floors)

h1.number_of_floors += 10
print(h1)

h2.number_of_floors = 10 + h2.number_of_floors
print(h2)

print(h1.number_of_floors > h2.number_of_floors)
print(h1.number_of_floors >= h2.number_of_floors)
print(h1.number_of_floors < h2.number_of_floors)
print(h1.number_of_floors <= h2.number_of_floors)
print(h1.number_of_floors != h2.number_of_floors)
