from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def wear(self):
        print("clothing")


class Engineer(Person):
    def __init__(self, name, skill):
        super().__init__(name)
        self.__skill = skill

    def get_skill(self):
        return self.__skill

    def wear(self):
        print("I am a " + self.get_skill() + "engineer" + self._name, end=", ")
        super().wear()


class Teacher(Person):
    def __init__(self, name, title):
        super().__init__(name)
        self.__title = title

    def get_title(self):
        return self.__title

    def wear(self):
        print("I am " + self._name + self.get_title(), end=", ")
        super().wear()


class ClothingDecorator(Person):
    def __init__(self, person):
        self._decorated = person

    def wear(self):
        self._decorated.wear()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass


class CasualPantDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("a yellow casual pant")


class BeltDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("a black belt")


class LeatherShoesDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("a casual leather shoes")


class KnittedSweaterDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("a red knitted sweater")


class WhiteShirtDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("a white shirt")


class GlassesDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("a black glasses")


def test_decorator():
    tony = Engineer("Tony", "client")
    pant = CasualPantDecorator(tony)
    belt = BeltDecorator(pant)
    shoes = LeatherShoesDecorator(belt)
    shirt = WhiteShirtDecorator(shoes)
    sweater = KnittedSweaterDecorator(shirt)
    glasses = GlassesDecorator(sweater)
    glasses.wear()

    print()
    decorate_teacher = GlassesDecorator(WhiteShirtDecorator(LeatherShoesDecorator(Teacher("wells", "Doctor"))))
    decorate_teacher.wear()
