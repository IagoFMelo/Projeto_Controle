# coding: utf-8

from inspect import trace
from re import X
from control import *
import matplotlib.pyplot as plt


class Transfer_function:

    def __init__(self, tf1=None, tf2=None):  # Inicialização
        self.tf1 = tf1
        self.tf2 = tf2

    def resposta_degrau(self):

        trace = input(
            "Digite a cor do tracejado de g1 red[r], blue[b], green[g]: ")
        trace1 = input(
            "Digite a cor do tracejado de g2 red[r], blue[b], green[g]: ")

        t, y = step_response(self.tf1)
        plt.plot(t, y, "-{0}".format(trace), label=self.tf1)
        if self.tf2 is not None:
            t1, y1 = step_response(self.tf2)
            plt.plot(t1, y1, "--{0}".format(trace1), label=self.tf2)


if __name__ == "__main__":
    s = tf("s")
    g1 = tf([1, 0], [2, 1, 2])
    print(g1)
