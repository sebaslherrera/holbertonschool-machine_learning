#!/usr/bin/env python3

"""Project 0x03. Probability"""


class Normal:
    """Class that represents an Normal distribution"""

    e = 2.7182818285

    def __init__(self, data=None, mean=0., stddev=1.):
        """Constructor of Normal
            Parameters:
            data (list): List of numbers
            mean (float): mean of data
            stddev (float): Standard deviation of Normal distribution
        """
        self.data = data

        if self.data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = mean
            self.stddev = stddev
        else:
            # Calculates the mean and standard deviation of data
            self.mean = sum(data) / len(data)
            tmpstdev = 0
            for el in data:
                tmpstdev += (el - self.mean) ** 2
            self.stddev = (tmpstdev/len(data)) ** (1/2)

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
    def mean(self):
        """Getter of mean"""
        return self.__mean

    @mean.setter
    def mean(self, value):
        """Setter of mean"""
        self.__mean = float(value)

    @property
    def stddev(self):
        """Getter of stddev"""
        return self.__stddev

    @stddev.setter
    def stddev(self, value):
        """Setter of stddev"""
        self.__stddev = float(value)

    def pdf(self, k):
        """Calculates the value of the PDF given time period"""

        if k < 0:
            return 0
        return (self.lambtha) * (self.e ** (-self.lambtha*k))

    def cdf(self, k):
        """Calculates the value of the CDF for a given time period"""

        if k < 0:
            return 0
        return 1 - (self.e ** (-self.lambtha*k))
