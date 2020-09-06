'''
Singletone Pattern - separates object construction from its representation

                    Affords finer control over the construction process. Unlike creational patterns that construct
                    products in one shot, the Builder pattern constructs the product step by step under the control
                    of the "director".

Real Life Example:  Single databse connection.
Real World Example: There should only be one current president of Poland (one instance of class PresidentOfPoland)

Ensure a class has only one instance, and provide a global point of access to it.
Encapsulated "just-in-time initialization" or "initialization on first use".

Singleton should be considered only if all three of the following criteria are satisfied:
    1. Ownership of the single instance cannot be reasonably assigned
    2. Lazy initialization is desirable
    3. Global access is not otherwise provided for

The Singleton pattern can be extended to support access to an application-specific number of instances.

Deleting a Singleton class/instance is a non-trivial design problem. if a client *deletes* the instance without
the Singleton class knowing about it, from then on the Singleton class will hand out "dangling references,"
which point to objects that no longer exist.
'''

class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        #if instance already exist
        return cls._instance



class MyClass(metaclass=Singleton):         # Singletone.__init__ invoked
    """Example class. Singletone is easy to use here, no need to create private/protected constructors, nor any static method."""
    pass


class MyClass2():
    """Example class that DOES NOT inherit from Singletone class."""
    pass


def main():
    singletone1 = MyClass()             #__call__ invoked, not __init__
    singletone2 = MyClass()             #__call__ invoked
    not_singletone1 = MyClass2()
    not_singletone2 = MyClass2()


    if (singletone1 is singletone2):

        print("MyClass1: Both objects include the same instance.")
    else:
        print("MyClass1: Singleton pattern implemented poorly.")


    if (not_singletone1 is not_singletone2):
        print("MyClass2: Both objects include the same instance.")
    else:
        print("MyClass2: Singleton pattern implemented poorly.")


if __name__ == "__main__":
    main()