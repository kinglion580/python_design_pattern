class PizzaIngredientFactory:
    def create_dough(self):
        pass

    def create_sauce(self):
        pass

    def create_veggies(self):
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_veggies(self):
        veggies = [Garlic(), Onion()]
        return veggies


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_veggies(self):
        veggies = [BlackOlives(), Eggplant()]
        return veggies


class Dough:
    pass


class ThickCrustDough(Dough):
    def __str__(self):
        return "ThickCrust style extra thick crust dough"


class ThinCrustDough(Dough):
    def __str__(self):
        return "ThinCrust style extra thin crust dough"


class Sauce:
    def __str__(self):
        pass


class MarinaraSauce(Sauce):
    def __str__(self):
        return "Marinara Sauce"


class PlumTomatoSauce(Sauce):
    def __str__(self):
        return "Plum Tomato Sauce"


class Veggies:
    pass


class Garlic(Veggies):
    def __str__(self):
        return "Garlic"


class Onion(Veggies):
    def __str__(self):
        return "Onion"


class BlackOlives(Veggies):
    def __str__(self):
        return "Black Olives"


class Eggplant(Veggies):
    def __str__(self):
        return "Eggplant"


class Pizza:
    _name = ""
    dough = ""
    sauce = ""
    veggies = []

    def prepare(self):
        pass

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        result = "---- " + self.name + " ----\n"
        if self.dough:
            result.join(self.dough)
        if self.sauce:
            result.join(self.sauce)
        if self.veggies:
            result.join(",".join(self.veggies) + "\n")


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing " + self.name)
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()


class PepperoniPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing " + self.name)
        dough = self.ingredient_factory.create_dough()
        veggies = self.ingredient_factory.create_veggies()


class PizzaStore:
    def create_pizza(self, type_) -> Pizza:
        pass

    def order_pizza(self, type_):
        pizza = self.create_pizza(type_)
        print("--- Making a " + pizza.name + "---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYStylePizzaStore(PizzaStore):
    def create_pizza(self, type_):
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()
        if type_ == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.name = "New York Style Cheese Pizza"
        elif type_ == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.name = "New York Style Pepperoni Pizza"
        return pizza
    

class ChicagoStylePizzaStore(PizzaStore):
    def create_pizza(self, type_):
        pizza = None
        ingredient_factory = ChicagoPizzaIngredientFactory()
        if type_ == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.name = "Chicago Style Cheese Pizza"
        elif type_ == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.name = "Chicago Style Pepperoni Pizza"
        return pizza


def test_pizza():
    nystore = NYStylePizzaStore()
    chicagostore = ChicagoStylePizzaStore()

    pizza = nystore.order_pizza("cheese")
    print("Ethan ordered a " + pizza.name + "\n")

    pizza = chicagostore.order_pizza("cheese")
    print("Joel ordered a " + pizza.name + "\n")
