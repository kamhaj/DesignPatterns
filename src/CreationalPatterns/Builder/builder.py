'''
Builder Pattern - separates object construction from its representation

                    Affords finer control over the construction process. Unlike creational patterns that construct
                    products in one shot, the Builder pattern constructs the product step by step under the control
                    of the "director".

Real World Example: Children's meals typically consist of a main item, a side item, a drink, and a toy
                    (e.g., a hamburger, fries, Coke, and toy dinosaur - these are our steps). Note that
                    there can be variation in the content of the children's meal, but the construction
                    process is the same. Cashier is the Director Class here.

Intent:  1. Separate the construction of a complex object from its representation so that the same construction
            process can create different representations.
         2. Parse a complex representation, create one of several targets.


Advantages of using Builder Method:
    1. Reusability: While making the various representations of the products, we can use the same construction
        code for other representations as well.
    2. Single Responsibility Principle: We can separate out both the business logic as well as the complex
        constructioncode from each other.
    3. Construction of the object: Here we construct our object step by step, defer construction steps or run
        steps recursively.

Disadvantages of using Builder method:
    1. Code complexity increases: The complexity of our code increases, because the builder pattern requires
        creating multiple new classes.
    2. Mutability: It requires the builder class to be mutable
    3. Initialization: Data members of the class are not guaranteed to be initialized.


Check List:
1. Decide if a common input and many possible representations (or outputs) is the problem at hand.
2. Encapsulate the parsing of the common input in a Reader class.
3. Design a standard protocol for creating all possible output representations. Capture the steps of this protocol in a Builder interface.
4. Define a Builder derived class for each target representation.
5. The client creates a Reader object and a Builder object, and registers the latter with the former.
6. The client asks the Reader to "construct".
7. The client asks the Builder to return the result.

// Sometimes creational patterns are complementary: Builder can use one of the other patterns to implement which components get built.
// Abstract Factory, Builder, and Prototype can use Singleton in their implementations.Builder often builds a Composite.
'''

import abc


class Director:
    """ Construct an object using the Builder interface."""
    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_part_a()
        self._builder._build_part_b()
        self._builder._build_part_c()


class Builder(metaclass=abc.ABCMeta):  #just an INTERFACE
    """Specify an abstract interface for creating parts of a Product object."""
    def __init__(self):
        self.product = Product()

    @abc.abstractmethod
    def _build_part_a(self):
        pass

    @abc.abstractmethod
    def _build_part_b(self):
        pass

    @abc.abstractmethod
    def _build_part_c(self):
        pass


class ConcreteBuilder(Builder):             #like a certain set meal in a restaurant (burger A + toy C + drink A)
    """
    Construct and assemble parts of the product by implementing the
    Builder interface.
    Define and keep track of the representation it creates.
    Provide an interface for retrieving the product.
    """
    def _build_part_a(self):
        #how to make this concrete part? implemented in here
        pass

    def _build_part_b(self):
        #how to make this concrete part? implemented in here
        pass

    def _build_part_c(self):
        #how to make this concrete part? implemented in here
        pass


class Product:
    """Represent the complex object under construction."""
    pass


def main():
    concrete_builder = ConcreteBuilder()
    director = Director()
    director.construct(concrete_builder)
    product = concrete_builder.product    #returned to a client


if __name__ == "__main__":
    main()