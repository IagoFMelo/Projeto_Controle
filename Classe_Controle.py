# @Propriedade de Iago Melo

# coding: utf-8

from inspect import trace
from re import X
from control import *
import matplotlib.pyplot as plt

sn = ["Y", "y"]


class Transfer_function:

    def __init__(self, tf1=None, tf2=None, tff=None):  # Inicialização
        self.tf1 = tf1
        self.tf2 = tf2
        self.tff = tff

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

    # Usar declarador nesta função
    def feedback_tf(self):

        fb = input("o sistema tem realimentação? [Y]/[y] ou [N]/[n]: ")
        if fb in sn:
            fb1, fb2, fb3, fb4 = input(
                "Digite os coeficientes do numerador da Função de Realimentação: ").split()
            fb11, fb22, fb33, fb44 = input(
                "Digite os coeficientes do denominador da Função de Realimentação: ").split()
            gff = tf([int(fb1), int(fb2), int(fb3), int(fb4)], [
                     int(fb11), int(fb22), int(fb33), int(fb44)])
            g1y, g2y = input(
                "A Função Transferência que está sendo realimentada é G1? É G2? (Colocar espaçado) [Y]/[y] ou [N]/[n]: ").split()

            if g1y in sn:
                fb_tf = feedback(self.tf1, gff)
                print(fb_tf)
            elif g2y in sn:
                fb_tf = feedback(self.tf2, gff)
                print(fb_tf)
