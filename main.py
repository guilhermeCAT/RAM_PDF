import packages
import os

def menu():
    while True:
        os.system('cls')
        print('===========================')
        print(9*' ',"RAM PDF")
        print('===========================')
        print("1. Converter Arquivo")
        print("2. Traduzir Arquivo")
        print("3. Sair")
        try:    
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            os.system('cls')
            print('Opção indisponível, somente de 1 a 3. Tente novamente.')
            continue

        if escolha == 1:
            os.system('cls')
            packages.conversor()
        elif escolha == 2:
            os.system('cls')
            packages.Entrada_do_usuario()
        elif escolha == 3:
            print("Saindo do programa.")
            break
        else:
            os.system('cls')
            print("Opção inválida. Tente novamente.")


menu()