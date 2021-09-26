class PizzaStore:
    def create_pizza(self, type_):
        pass

    def order_pizza(self, type_):
        pizza = self.create_pizza(type_)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYStylePizzaStore(PizzaStore):
    def create_pizza(self, type_):
        pizza = None
        if type_ == "cheese":
            pizza = NYStyleCheesePizza()
        # elif type_ == "pepperoni":
        #     pizza = NYStylePepperoniPizza()
        # elif type_ == "clam":
        #     pizza = NYStyleClamPizza()
        # elif type_ == "veggie":
        #     pizza = NYStyleVeggiePizza()
        return pizza
    

class ChicagoStylePizzaStore(PizzaStore):
    def create_pizza(self, type_):
        pizza = None
        if type_ == "cheese":
            pizza = ChicagoStyleCheesePizza()
        # elif type_ == "pepperoni":
        #     pizza = ChicagoStylePepperoniPizza()
        # elif type_ == "clam":
        #     pizza = ChicagoStyleClamPizza()
        # elif type_ == "veggie":
        #     pizza = ChicagoStyleVeggiePizza()
        return pizza


class Pizza:
    name = ""
    dough = ""
    sauce = ""
    toppings = []

    def prepare(self):
        print("Preparing " + self.name + "\n")
        print("Tossing dough...\n")
        print("Adding sauce...\n")
        print("Adding toppings: \n")
        for topping in self.toppings:
            print("   " + topping + "\n")

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def get_name(self):
        return self.name


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"

        self.toppings.append("Grated Reggiano Cheese")


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "Chicago Style Deep Dih Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"

        self.toppings.append("Shredded Mozzarella Cheese")

    def cut(self):
        print("Cutting the pizza into square slices")


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
    def to_string(self):
        pass


class ThickCrustDough(Dough):
    def to_string(self):
        return "ThickCrust style extra thick crust dough"


class ThinCrustDough(Dough):
    def to_string(self):
        return "ThinCrust style extra thin crust dough"


class Sauce:
    def to_string(self):
        pass


class MarinaraSauce(Sauce):
    def to_string(self):
        return "Marinara Sauce"


class PlumTomatoSauce(Sauce):
    def to_string(self):
        return "Plum Tomato Sauce"


class Veggies:
    def to_string(self):
        pass


class Garlic(Veggies):
    def to_string(self):
        return "Garlic"


class Onion(Veggies):
    def to_string(self):
        return "Onion"


class BlackOlives(Veggies):
    def to_string(self):
        return "Black Olives"


class Eggplant(Veggies):
    def to_string(self):
        return "Eggplant"


def test_pizza():
    nystore = NYStylePizzaStore()
    chicagostore = ChicagoStylePizzaStore()

    pizza = nystore.order_pizza("cheese")
    print("Ethan ordered a " + pizza.get_name() + "\n")

    pizza = chicagostore.order_pizza("cheese")
    print("Joel ordered a " + pizza.get_name() + "\n")
