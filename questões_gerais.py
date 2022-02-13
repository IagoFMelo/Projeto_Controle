# @Propriedade de Iago Melo


# coding: utf-8

from matplotlib.pyplot import get_fignums
from Classe_Controle import *
import sys

s = tf("s")

sn = ["Y", "y"]

g1 = None
g2 = None

while True:
    print("A digitação da função se dará da forma -> Ex: Numerador - (sˆ2+2s) :. 0 1 2 0\nCoeficientes iniciam com sˆ3\n")

    x1, y1, w1, z1 = input(
        "Digite os coeficientes do numerador da Função transferência G1: ").split()

    x11, y11, w11, z11 = input(
        "Digite os coeficientes do denominador da Função transferência G1: ").split()

    ti_1 = input(
        "A função transferência tem termo independente? [Y]/[y] ou [N]/[n]: ")

    if ti_1 in sn:

        ti = input("Digite o valor do termo independete: ")
        g1 = tf([int(x1), int(y1), int(w1), int(z1)], [
                int(x11), int(y11), int(w11), int(z11)]) + int(ti)
    else:

        g1 = tf([int(x1), int(y1), int(w1), int(z1)], [
                int(x11), int(y11), int(w11), int(z11)])

    print(g1)

    us = input(
        "Será utilizada uma segunda função transferência? [Y]/[y] ou [N]/[n]: ")

    if us in sn:
        x2, y2, w2, z2 = input(
            "Digite os coeficientes do numerador da Função transferência G2: ").split()

        x22, y22, w22, z22 = input(
            "Digite os coeficientes do denominador da Função transferência G2: ").split()

        ti_2 = input(
            "A função transferência tem termo independente? [Y]/[y] ou [N]/[n]:")

        if ti_2 in sn:

            ti1 = input("Digite o valor do termo independete: ")
            g2 = tf([int(x2), int(y2), int(w2), int(z2)], [
                    int(x22), int(y22), int(w22), int(z22)]) + int(ti1)
        else:

            g2 = tf([int(x2), int(y2), int(w2), int(z2)], [
                    int(x22), int(y22), int(w22), int(z22)])

    print(g2)

    controle1 = Transfer_function(g1, g2, )
    controle1.feedback_tf()
    controle1.resposta_degrau()
    tit = input("Digite qual o título do seu gráfico: ")
    plt.title(tit)
    plt.legend(fontsize=12)
    plt.xlabel("Tempo[t]")
    plt.ylabel("y(t)")
    plt.grid()
    plt.show()

    answer = input("Rodar novamente? [Y]/[y] ou [N]/[n]: ")
    if answer in sn:
        print("Continua...")
    else:
        sys.exit()
