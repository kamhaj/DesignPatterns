##Some of Software Design Patterns implemented in Python 3

Design pattern - is a model solution to a common design problem. It describes the problem and a general approach to solving it.

We need design patterns to ensure our work is consistent, reliable and understandable.

We divide design patterns into:
a) Creational (object creation)
b) Structural (objects relationships)
c) Behavioral (objects interaction and resposibility)

[other types of patterns. e.g. Concurrency Patterns (for multithreaded systems) are not covered here]



CREATIONAL PATTERNS (provide various object creation mechanisms, which increase flexibility and reuse of existing code):
	
	1. Singleton Pattern 
	(lets you ensure that a class has only one instance, while providing a global access point to this instance)

	2. Builder Pattern 
	(lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code)

	3. Factory Pattern / Factory Method
	(provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created)

	4. Abstract Factory Pattern 
	(lets you produce families of related objects without specifying their concrete classes)
	
more: 
Prototype Pattern
	
	



STRUCTURAL PATTERNS (explain how to assemble objects and classes into larger structures while keeping these structures flexible and efficient):

	1. --

more: 
Adapter Pattern
Bridge Pattern
Composite Pattern
Decorator Pattern
Facade Pattern
Flyweight Pattern
Proxy Pattern






BEHAVIORAL PATTERNS (are concerned with algorithms and the assignment of responsibilities between objects):
	
	1. Command Pattern
	(turns a request into a stand-alone object that contains all information about the request. This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations)

	2. Observer Pattern
	(lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing)

	3. Strategy Pattern / Policy Pattern
	(lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable/swappable)

	4. Null Pattern
	
more:
Chain of Responsibility Pattern
Iterator Pattern
Mediator Pattern
Memento Pattern
State Pattern
Template Method Pattern
Visitor Pattern




Red flags for possible pattern use

sequence of many if/elif statements --> Strategy Pattern
