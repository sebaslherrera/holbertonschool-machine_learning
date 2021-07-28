#!/usr/bin/env python3

"""Project 0x03. Probability"""


class Poisson:
    """Class that represents a poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """Constructor of Poisson
        If data is given lambtha is calculated
        """
        self.data = data

        if self.data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = lambtha
        else:
            # Calculates lambtha of data
            self.lambtha = sum(data) / len(data)

    @property
    def data(self):
        """Getter of data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter of data"""
        if value is not None and not isinstance(value, list):
            raise TypeError("data must be a list")
        if value is not None and len(value) < 2:
            raise ValueError("data must contain multiple values")
        self.__data = value

    @property
    def lambtha(self):
        """Getter of lambtha"""
        return self.__lambtha

    @lambtha.setter
    def lambtha(self, value):
        """Setter of lambtha"""
        self.__lambtha = float(value)
