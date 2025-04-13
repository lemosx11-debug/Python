import math

def calculadora():
    while True:
        print("\n=== Calculadora ===")
        print("Selecione a operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Potência")
        print("6 - Raiz quadrada")
        print("7 - Porcentagem")
        print("0 - Sair")

        escolha = input("Digite a opção (0-7): ")

        if escolha == '0':
            print("Encerrando a calculadora. Até mais!")
            break

        if escolha in ["1", "2", "3", "4", "5", "7"]:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == "1":
                print(f"{num1} + {num2} = {num1 + num2}")
            elif escolha == "2":
                print(f"{num1} - {num2} = {num1 - num2}")
            elif escolha == "3":
                print(f"{num1} * {num2} = {num1 * num2}")
            elif escolha == "4":
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Erro: divisão por zero.")
            elif escolha == "5":
                print(f"{num1} ^ {num2} = {math.pow(num1, num2)}")
            elif escolha == "7":
                print(f"{num1}% de {num2} = {(num1 / 100) * num2}")
        elif escolha == "6":
            num = float(input("Digite o número para raiz quadrada: "))
            if num >= 0:
                print(f"Raiz quadrada de {num} = {math.sqrt(num)}")
            else:
                print("Erro: não existe raiz quadrada real de número negativo.")
        else:
            print("Opção inválida.")

calculadora()