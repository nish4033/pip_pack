"""
Calculator application for understanding basics of Unit testing in Python.
"""
import math


class BasicCalc(object):
    """
    The basic calculator service provides functions like add, subtract, multiply and divide for 2
    given numbers
    """

    def add(self, a, b):
        """
        Function to return sum of two given numbers.
        :param a:
        :param b:
        :return: Sum of a and b
        """
        if isinstance(a, (int,float)) and isinstance(b, (int,float)):
            return a + b

    def difference(self, a, b):
        """
        Function to return difference of two given numbers.
        :param a:
        :param b:
        :return: Difference between a and b
        """
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a - b
        else:
            return "Wrong input"

    def multiply(self, a, b):
        """
        Function to return multiplication of two given numbers.
        :param a:
        :param b:
        :return: multiply a and b
        """
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a * b
        else:
            return "Wrong input"

    def divide(self, a, b, c=None):
        """
        Function to return division of two given numbers.
        :param a:
        :param b:
        :return: division of a by b
        """
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if b != 0:
                return a / b
            else:
                return "Wrong Input"
        else:
            return "Wrong Input"


class AdvCalc(BasicCalc):

    def __init__(self):
        super(AdvCalc, self).__init__()

    def mod(self, a, b):
        """
        Function to return the modulus between two numbers
        :param a:
        :param b:
        :return: a modulus b
        """
        a = abs(a)
        b = abs(b)
        if b != 0:
            div = math.floor(self.divide(a, b))
            prod = self.multiply(div, b)
            mod = self.difference(a, prod)
            return mod
        else:
            return "wrong input"




