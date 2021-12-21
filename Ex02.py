# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def main():
    num1 = float(input('Insira um número: '))

    if num1 > 0:
        print(f'O  número é positivo')
    else:
        print(f'O  número é negativo')


if __name__ == '__main__':
    main()
