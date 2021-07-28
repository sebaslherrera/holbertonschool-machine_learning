#!/usr/bin/env python3

"""Project 0x03. Probability"""


class Exponential:
    """Class that represents an Exponential distribution"""

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """Constructor of Exponential
        If data is given lambtha is calculated
        """
        self.data = data

        if self.data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = lambtha
        else:
            # Calculates lambtha of data
            self.lambtha = 1 / (sum(data) / len(data))

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

    def pdf(self, k):
        """Calculates the value of the PDF given time period"""

        if k < 0:
            return 0
        return (self.lambtha) * (self.e ** (-self.lambtha*k))

    def cdf(self, k):
        """Calculates the value of the CDF for a given
        number of successes"""

        k = int(k)

        if k < 0:
            return 0
        ans = 0
        for i in range(0, k + 1):
            ans += self.pdf(i)
        return ans
