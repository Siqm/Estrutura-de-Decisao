# Faça um Programa para um caixa eletrônico. O programa deverá perguntar
# ao usuário a valor do saque e depois informar quantas notas de cada valor
# serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100
# reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa
# não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece
# duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas
# de 100,uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


def pede_saque(mnm, mxm):
    cond = False

    while not cond:
        print('O valor mínimo para saque é de R$10 e o valor máximo é de R$600')
        saque = int(input('Saque desejado: '))
        cond = mnm <= saque <= mxm
    return saque


def main():
    notas = [100, 50, 10, 5, 1]
    minimo = 10
    maximo = 600
    saque = pede_saque(minimo, maximo)
    troco = {}

    for i in notas:
        if saque >= i:
            resto = saque // i
            saque -= i*resto
            troco[i] = resto

    print('Seu troco será dividido da sequinte forma: ')
    for i in troco:
        if troco[i] > 1:
            print(f'{troco[i]} notas de R${i}')
        else:
            print(f'{troco[i]} nota de R${i}')


if __name__ == '__main__':
    main()

