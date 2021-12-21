# As Organizações Tabajara resolveram dar um aumento
# de salário aos seus colaboradores e lhe contraram
# para desenvolver o programa que calculará os reajustes.

# Faça um programa que recebe o salário de um colaborador e o
# reajuste segundo o seguinte critério, baseado no salário atual:

# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

def calcula_aumento():
    sal = float(input('Insira o seu salário: '))

    if sal <= 280:
        aumento = 0.2
    elif 280 < sal <= 700:
        aumento = 0.15
    elif 700 < sal <= 1500:
        aumento = 0.1
    else:
        aumento = 0.05
    return sal, aumento


def main():
    salario, aumento = calcula_aumento()
    valor = salario * aumento
    reajuste = salario + valor
    print(f'O salário antes do reajuste é de R${salario}')
    print(f'O percentual de aumento foi de {aumento*100}%')
    print(f'O valor de aumento é de R${valor}')
    print(f'O salário depois do aumento é de R${reajuste}')


if __name__ == '__main__':
    main()