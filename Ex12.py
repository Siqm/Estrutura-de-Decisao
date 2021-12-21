# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
# descontos são do Imposto de Renda, que depende do salário bruto (conforme
# tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
# Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido
# corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao
# usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na
# tela as informações, dispostas conforme o exemplo abaixo.


def Pede_devolve_sal_ir(sal):
    if sal <= 900:
        ir = 0
    elif sal <= 1500:
        ir = 0.05
    elif sal <= 2500:
        ir = 0.1
    else:
        ir = 0.2
    return ir


def main():
    hora = float(input('Insira o valor da hora trabalhada: '))
    qtdhora = float(input('Insira a quantidade de horas trabalhadas: '))

    salario = qtdhora * hora
    ir = Pede_devolve_sal_ir(salario)
    # sindicato = 0.03 exercício da esse valor mas não pede a operação
    fgts = 0.11
    inss = 0.1

    cIr = ir * salario
    cInss = inss * salario
    cFgts = salario * fgts
    liquido = salario - cIr - cInss

    print(f'Salário bruto: ({hora} * {qtdhora})\t\t : R${salario}')
    if ir == 0:
        print(f'IR Isento\t\t\t\t\t\t : R$-----')
    else:
        print(f'(-) IR ({ir * 100}%)\t\t\t\t\t\t : R${cIr} ')
    print(f' (-) INSS ({inss * 100}%)\t\t\t\t\t : R${cInss}')
    print(f'FGTS ({fgts * 100}%) \t\t\t\t\t\t : R${cFgts}')
    print(f'Total de descontos \t\t\t\t\t : R${cIr+cInss}')
    print(f'Salário liquído \t\t\t\t\t : R${liquido}')


if __name__ == '__main__':
    main()
