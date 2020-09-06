'''
Abstract Factory Pattern -   allows you to produce the families of related objects without specifying their
                             concrete classes. Using the abstract factory method, we have the easiest ways to produce
                             a similar type of many objects. It provides a way to encapsulate a group of individual factories.

                             difference between abstract factory and factory method is that abstract factory is a factory of a factory.
                             we give CourseFactory new factories (course classes) as parameter.
'''

import random

class CourseFactory:
    def __init__(self, courses_factory):
        """course factory is out abstract factory"""
        self.course_factory = courses_factory

        """creates and shows courses using the abstract factory"""
    def show_course(self):
        course = self.course_factory()
        print('We have a course named {}'.format(course))
        print('its price is {}'.format(course.price()))



class EnglishCourse:
    def price(self):
        return 1000

    def __str__(self):
        return "English"


class MathsCourse:
    def price(self):
        return 800

    def __str__(self):
        return "Maths"


class PhysicsCourse:
    def price(self):
        return 1500

    def __str__(self):
        return 'Physics'


def random_course():
    """A random class for choosing the course"""
    return random.choice([EnglishCourse, MathsCourse, PhysicsCourse])()


# main method
if __name__ == "__main__":
    for i in range(5):
        course = CourseFactory(random_course)
        course.show_course()