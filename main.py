def valores_usuario():
    a = int(input("Digite seu primeiro valor: "))
    b = int(input("Digite seu segundo valor: "))
    return a, b


def equacoes():
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    return input("Opção: ")


def operacao_matematica(a, b, opcao):
    try:
        if opcao == "1":
            print(f"O resultado é: {a + b}")
        elif opcao == "2":
            print(f"O resultado é: {a - b}")
        elif opcao == "3":
            print(f"O resultado é: {a * b}")
        elif opcao == "4":
            if b != 0:
                print(f"O resultado é: {a / b}")
            else:
                print("Não é possível realizar divisão por 0.")
        else:
            print("Opção inválida.")
    except Exception as e:
        print(f"Erro encontrado: {e}")


a, b = valores_usuario()
opcao = equacoes()
operacao_matematica(a, b, opcao)
