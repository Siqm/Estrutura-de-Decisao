# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um
# triângulo. Indique, caso os lados formem um triângulo,
# se o mesmo é: equilátero, isósceles ou escaleno.

# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;


def pede_lados():
    l1 = float(input('Insira o tamanho do primeiro lado:'))
    l2 = float(input('Insira o tamanho do segundo lado:'))
    l3 = float(input('Insira o tamanho do terceiro lado:'))
    return l1, l2, l3


def main ():
    lado1, lado2, lado3 = pede_lados()

    triangulo = lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2
    equilatero = lado1 == lado2 == lado3
    isosceles = lado1 == lado2 or lado1 == lado3 or lado2 == lado3

    if triangulo:
        print('Os 3 lados formam um triangulo!')
        if equilatero:
            print('O triangulo é equilatero')
        elif isosceles:
            print('O triangulo é isosceles')
        else:
            print('O triangulo é escaleno')
    else:
        print('Os 3 lados não formam um triangulo')


if __name__ == '__main__':
    main()