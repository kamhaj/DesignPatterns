SOLID principles of Object Oriented Design

##S - Single Responsibility

class should only have ONE responsibility.
(either cooking or washing up, but not both).

##O - Open-Closed

class should be open for extension (usually by inheritance) but closed for modification (someone is using our class and we suddenly change it - not a good call).


##L - Liskov Substitution

subclasses should be able to stand in for their parents in a program without breaking anything.


##I - Interface Segregation

many specific interfaces (smaller ones) are better than one 'do-it-all' interface.
(in Python we use abstract base classes and multiple inheritance to achieve this effect)

##D - Dependency Inversion

we should program towards abstractions, not implementations. Implementations can vary, abstractions should not.


