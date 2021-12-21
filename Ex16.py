# Faça um programa que calcule as raízes de uma equação do segundo grau,
# na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c
# e fazer as consistências, informando ao usuário nas seguintes situações:

# Se o usuário informar o valor de A igual a zero, a equação não é do segundo
# grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;


def main():
    a = float(input('Insira o valor de A: '))
    b = float(input('Insira o valor de B: '))
    c = float(input('Insira o valor de C: '))
    delta = b**2 - 4 * a*c

    if delta < 0:
        print('A equação não possui raízes reais')
        exit()
    elif a == 0:
        print('\'A\' não pode ser igual a zero')
        exit()
    else:
        x1 = (-b + delta ** 0.5) / 2 * a
        x2 = 0
        if delta > 0:
            x2 = (-b - delta ** 0.5) / 2 * a
        else:
            print(f'Delta possui apenas uma raiz, igual a: {x1}')
        print(f'Delta possui duas raízes')
        print(f'primeira raiz: {x1}')
        print(f'segunda raiz: {x2}')


if __name__ == '__main__':
    main()
