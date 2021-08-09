#!/usr/bin/env python3

"""2. Neuron Forward Propagation
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
        self.__W = np.random.normal(size=(1, self.__nx))
        self.__b = 0
        self.__A = 0

    def forward_prop(self, X):
        """Forward propagation of the neuron

        Args:
            X (np.array): numpy array with shape (nx, m)

        Returns:
            np.array: The activated function of the neuron
        """

        self.__A = Neuron.sigmoid(np.dot(self.W, X) + self.b)
        return self.A

    @staticmethod
    def sigmoid(z):
        """Miscellaneous Sigmoid function

        Args:
            z (int or list): int or lists of numbers

        Returns:
            int or list: Sigmoid function result
        """
        return 1/(1+np.exp(-z))

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

    @property
    def b(self):
        """Getter of b

        Returns:
            int: The bias for the neuron
        """
        return self.__b

    @property
    def A(self):
        """Getter of A

        Returns:
            int: The activated output of the neuron (prediction)
        """
        return self.__A
