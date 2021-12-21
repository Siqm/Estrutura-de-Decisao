# Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


def pede_numero():
    num = []
    for i in range (0, 3):
        num.append(float(input(f'Insira o preço do {i+1}° produto: ')))
    return num


def encontra_produto(produtos, barato):
    for i in range(0, 3):
        if produtos[i] == barato:
            break
    return i


def main():
    produtos = pede_numero()
    barato = min(produtos)
    print(f'O produto mais barato é o {encontra_produto(produtos, barato)+1}°, com o valor de R${barato}')


if __name__ == '__main__':
    main()
