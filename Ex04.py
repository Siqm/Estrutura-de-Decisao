# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def main():
    letra = input('Insira uma letra: ').lower().strip()
    vogal = letra in ['a', 'e', 'i', 'o', 'u']
    if vogal:
        print(f'A letra \'{letra.upper()}\' é uma vogal')
    else:
        print(f'A letra \'{letra.upper()}\' é uma consoante')


if __name__ == '__main__':
    main()
