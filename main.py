import six
import types


class Source:
    @staticmethod
    def hello_world_v1():
        print("Hello World v1!")

    @staticmethod
    def hello_world_v2():
        print("Hello World v2!")


class Meta(type):
    def __new__(cls, name, bases, dct):
        for member in Source.__dict__:
            if isinstance(Source.__dict__[member], staticmethod):
                dct[member] = Source.__dict__[member]

        return super(Meta, cls).__new__(cls, name, bases, dct)


class Destination(six.with_metaclass(Meta)):
    pass


dst = Destination()
dst.hello_world_v1()
dst.hello_world_v2()
