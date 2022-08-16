from CALCULADORA.motor import Calculadora


class Menu:
    while True:
        print(
              "escolha uma das opçoes abaixo \n"
              "[1] Soma\n"
              "[2] multiplicacao\n"
              "[3] subtracao\n"
              "[4] divisao\n"
              "[5] sair\n")
        opcao = int(input("digite uma opcao: "))
        if opcao ==1:
            soma = Calculadora(
                numero01 = float(input("Digite o primeiro numero: ")),
                numero02 = float(input("Digite o primeiro numero: "))
            )
            print("=====================================")
            soma.adcao()
            print("=====================================")
        elif opcao ==2:
            multi = Calculadora(
                numero01=float(input("Digite o primeiro numero: ")),
                numero02=float(input("Digite o primeiro numero: "))
            )
            print("=====================================")
            multi.multiplicar()
            print("=====================================")
        elif opcao == 3:
            subt = Calculadora(
                numero01=float(input("Digite o primeiro numero: ")),
                numero02=float(input("Digite o primeiro numero: "))
            )
            print("=====================================")
            subt.subtracao()
            print("=====================================")
        elif opcao ==4:
            divis = Calculadora(
                numero01=float(input("Digite o primeiro numero: ")),
                numero02=float(input("Digite o primeiro numero: "))
            )
            print("=====================================")
            divis.divisao()
            print("=====================================")
        else:
            exit()

