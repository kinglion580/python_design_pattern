
class FlyBehavior:
    def fly(self):
        pass


class QuackBehavior:
    def quack(self):
        pass


class FlyWithWing(FlyBehavior):
    def fly(self):
        print("i'm flying")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("i can't fly")


class Quack(QuackBehavior):
    def quack(self):
        print('quack')


class MuteQuack(QuackBehavior):
    def quack(self):
        print("silence")


class Squeak(QuackBehavior):
    def quack(self):
        print("spueak")


class Duck:
    flybehavior = FlyBehavior()
    quackbehavior = QuackBehavior()

    def swim(self):
        print('duck swim')

    def display(self):
        pass

    def perform_fly(self):
        self.flybehavior.fly()

    def perform_quack(self):
        self.quackbehavior.quack()


class MyDuck(Duck):
    flybehavior = FlyWithWing()
    quackbehavior = Quack()

    def display(self):
        print("This is my duck")


myduck = MyDuck()
myduck.display()
myduck.swim()
myduck.perform_fly()
myduck.perform_quack()
