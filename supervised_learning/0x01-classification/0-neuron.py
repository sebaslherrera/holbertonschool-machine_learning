#!/usr/bin/env python3

"""0. Neuron
"""

import numpy as np


class Neuron:
    """Class that defines a single neuron
    """

    def __init__(self, nx):
        """Initialize a neuron

        Args:
            nx (int): number of input features to the neuron
        """
        self.nx = nx
        self.W = np.random.normal(size=(1, self.__nx))
        self.b = 0
        self.A = 0

    @property
    def nx(self):
        """Getter of nx

        Returns:
            int: Number of input features to the neuron
        """
        return self.__nx

    @nx.setter
    def nx(self, value):
        """Setter of nx

        Args:
            value (int): Number of input features to the neuron

        Raises:
            TypeError: nx must be an integer
            ValueError: nx must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("nx must be an integer")
        if value < 1:
            raise ValueError("nx must be a positive integer")
        self.__nx = value

    @property
    def W(self):
        """Getter of W

        Returns:
            int: Weights vector for the neuron
        """
        return self.__W

    @W.setter
    def W(self, value):
        """Setter of W

        Args:
            value (int): Weights vector for the neuron
        """
        self.__W = value

    @property
    def b(self):
        """Getter of b

        Returns:
            int: The bias for the neuron
        """
        return self.__b

    @b.setter
    def b(self, value):
        """Setter of b

        Args:
            value (int): The bias for the neuron
        """
        self.__b = value

    @property
    def A(self):
        """Getter of A

        Returns:
            int: The activated output of the neuron (prediction)
        """
        return self.__A

    @A.setter
    def A(self, value):
        """Setter of A

        Args:
            value (int): The activated output of the neuron (prediction)
        """
        self.__A = value
