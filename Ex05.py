# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:

# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

def main():
    n1 = float(input('Insira a nota 1: '))
    n2 = float(input('Insira a nota 2: '))
    condicao = 0 <= n1 <= 10 and 0 <= n2 <= 10
    if condicao:
        media = (n2+n1) / 2

        if media == 10:
            print('Sua média foi 10 e você foi Aprovado com Distinção!')
        elif media >= 7:
            print(f'Sua média é de {media} e você foi APROVADO!')
        else:
            print(f'Sua média foi {media} e você foi REPROVADO!')
    else:
        print('O valor da nota deve ser entre 0 e 10!')
        main()


if __name__ == '__main__':
    main()