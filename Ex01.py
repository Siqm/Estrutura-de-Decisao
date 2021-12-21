# Faça um Programa que peça dois números e imprima o maior deles.

def main():
    num1 = float(input('Insira o primeiro número: '))
    num2 = float(input('Insira o segundo número: '))

    if num1 > num2:
        print(f'O maior número é o {num1}')
    else:
        print(f'O maior número é o {num2}')


if __name__ == '__main__':
    main()
