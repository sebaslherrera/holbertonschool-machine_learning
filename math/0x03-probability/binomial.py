#!/usr/bin/env python3

"""Project 0x03. Probability"""


class Binomial:
    """Class that represents an Binomial distribution"""

    e = 2.7182818285
    pi = 3.1415926536

    def __init__(self, data=None, n=1, p=0.5):
        """Constructor of Binomial

        Parameters:
        data (list): list of the data to be used to estimate the distribution
        n (int): number of Bernoulli trials
        p (float): probability of a “success”
        """
        self.data = data

        if self.data is None:
            self.n = n
            self.p = p
        else:
            # Calculate n and p from data
            lenData = len(data)
            mean = sum(data) / lenData
            variance = sum(pow((e - mean), 2) for e in data) / lenData
            p = 1 - variance/mean
            self.n = round(mean/p)
            self.p = mean/self.n

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
    def n(self):
        """Getter of n"""
        return self.__n

    @n.setter
    def n(self, value):
        """Setter of n"""

        if value <= 0:
            raise ValueError("n must be a positive value")
        self.__n = int(value)

    @property
    def p(self):
        """Getter of p"""
        return self.__p

    @p.setter
    def p(self, value):
        """Setter of p"""

        if value <= 0 or value >= 1:
            raise ValueError("p must be greater than 0 and less than 1")
        self.__p = float(value)

    def z_score(self, x):
        """Calculates the z-score of a given x-value"""
        return (x - self.n) / self.p

    def x_value(self, z):
        """Calculates the x-value of a given z-score"""
        return z * self.p + self.n

    @staticmethod
    def factorial(x):
        """Return factorial of x"""
        ans = 1
        for i in range(x, 1, -1):
            ans *= i
        return ans

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of successes."""

        if k < 0 or k > self.n:
            return 0

        k = int(k)

        c = (Binomial.factorial(self.n)) / \
            (Binomial.factorial(k) * self.factorial((self.n - k)))

        return c * pow(self.p, k) * pow((1 - self.p), (self.n - k))

    def cdf(self, k):
        """Calculates the value of the CDF for a given number of successes."""

        if k < 0 or k > self.n:
            return 0

        k = int(k)
        ans = 0
        for i in range(0, k + 1):
            ans += self.pmf(i)
        return ans
