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


def Pede_devolve_sal_ir():
    sal = float(input('Insira seu salário: '))
    if sal <= 900:
        ir = 'Isento'
    elif sal <= 1500:
        ir = 0.05
    elif sal <= 2500:
        ir = 0.1
    else:
        ir = 0.2
    return sal, ir


def main():
    salario, ir = Pede_devolve_sal_ir()
    sindicato = 0.03
    fgts = 0.11
    inss = 0.1
