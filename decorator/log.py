import logging
logging.basicConfig(level=logging.INFO)


def logging_decorator(func):
    def wrapper_logging(*args, **kwargs):
        logging.info("start execute %s() ..." % func.__name__)
        func(*args, **kwargs)
        logging.info("%s() done" % func.__name__)
    return wrapper_logging


@logging_decorator
def show_info(*args, **kwargs):
    print("this is a test function, parameters: ", args, kwargs)


@logging_decorator
def show_sum(a, b):
    print("the sum of %d, %d is: %d" % (a, b, a+b))


# decorated_show_info = logging_decorator(show_info)
# decorated_show_info('arg1', 'arg2', kwarg1=1, kwarg2=2)

# decorated_show_sum = logging_decorator(show_sum)
# decorated_show_sum(2, 3)


show_info('arg1', 'arg2', kwarg1=1, kwarg2=2)
show_sum(2, 3)


class ClassDecorator:
    def __init__(self, func):
        self.__num_of_call = 0
        self.__func = func

    def __call__(self, *args, **kwargs):
        self.__num_of_call += 1
        obj = self.__func(*args, **kwargs)
        print("create %s of %d instance: %s" % (self.__func.__name__, self.__num_of_call, id(obj)))
        return obj


@ClassDecorator
class MyClass:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


tony = MyClass("Tony")
karry = MyClass("Karry")
print(id(tony))
print(id(karry))
