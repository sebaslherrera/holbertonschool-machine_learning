#!/usr/bin/env python3

"""Project 0x03. Probability"""


class Normal:
    """Class that represents an Normal distribution"""

    e = 2.7182818285
    pi = 3.1415926536

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

    def z_score(self, x):
        """Calculates the z-score of a given x-value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score"""
        return z * self.stddev + self.mean

    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value"""

        return (self.e ** (-0.5 * (self.z_score(x) ** 2))) \
            / (self.stddev * ((2 * self.pi) ** 0.5))

    def erf(self, z):
        """Error function encountered in integrating the normal distribution"""
        return (2 / (self.pi**0.5)) * \
            (z - (z**3) / 3 + (z**5) / 10 - (z**7) / 42 + (z**9) / 216)

    def cdf(self, x):
        """Calculates the value of the CDF for a given x-value"""

        return 0.5 * (1 + self.erf((self.z_score(x) / (2 ** 0.5))))
