''' 
Factory Pattern -   allows an interface or a class to create an object, but let subclasses decide which class or object
                    to instantiate. Using the Factory method, we have the best ways to create an object. Here, objects
                    are created without exposing the logic to the client and for creating the new type of the object,
                    the client uses the same common interface.
                    Suppose you want to create multiple instances of similar kind and want to 
                    achieve loose coupling then you can go for Factory pattern.  Consider an
                    example of using multiple database servers like SQL Server and Oracle.
'''

import matplotlib.pyplot as plt
import matplotlib
import numpy as np


class Circle:
    def __init__(self):
        print("I am a Circle!")

    def draw(self):
        return plt.Circle((0, 0), 0.2, color='r')



class Triangle:
    def __init__(self):
        print("I am a Triangle!")

    def draw(self):
        points = [[.2, .1], [.8, .1], [.8, .4]]
        return plt.Polygon(points, color='g')



class Rectangle:
    def __init__(self):
        print("I am a Rectangle!")

    def draw(self):
        return matplotlib.patches.Rectangle((0.5, 0.5), 0.3, 0.2, color='b')


    """Factory Method"""
def Factory(shape ="Circle"):
    shapes_dict = {
        "Circle": Circle,
        "Triangle": Triangle,
        "Rectangle": Rectangle,
    }
    return shapes_dict[shape.lower().capitalize()]()



def provideChart(listOfShapes):
    # Define limits of coordinate system
    x1 = -1.5
    x2 = 1.5
    y1 = -1.5
    y2 = 1.5

    fig, ax = plt.subplots()
    for shape in listOfShapes:
        ax.add_artist(shape.draw())

    plt.axis("equal")
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.xlim(left=x1)
    plt.xlim(right=x2)
    plt.ylim(bottom=y1)
    plt.ylim(top=y2)
    plt.axhline(linewidth=2, color='k')
    plt.axvline(linewidth=2, color='k')

    #plt.grid(True)
    plt.grid(color='k', linestyle='-.', linewidth=0.5)
    plt.show()


if __name__ == "__main__":
    # main method to call others
    listOfShapes = [Factory("Circle"), Factory("TRIANGLE"), Factory("rectangle")]
    provideChart(listOfShapes)