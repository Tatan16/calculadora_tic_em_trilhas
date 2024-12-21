def calculadora():
    while True:
        print("\nCalculadora Simples")
        print()
        print("1. Soma")
        print("2. Substração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("s. Sair")
        
        operacao = input("\nSelecioane uma opção ou 's' para sair: ")
        
        if  operacao == 's' or operacao == 'S':
            print("Obrigado por ultilizar a Calculadora Simples!")
            break
        
        if operacao not in ["1", "2", "3", "4",]:
            print("Opção invalida! Tente novamente.")
            continue
        
        numero_1 = float(input("Primeiro número: "))
        numero_2 = float(input("Segundo número: "))
        
        if operacao == "1":
            resultado = numero_1 + numero_2
            print(f"O resultado da operação soma é {resultado}")
            
        elif operacao == "2":
            resultado = numero_1 - numero_2
            print(f"O resultado da operação substração é {resultado}")
            
        elif operacao == "3":
            resultado = numero_1 * numero_2
            print(f"O resultado da operação multiplicação é {resultado}")
            
        else:
            if numero_2 == 0:
                print("Divisões por zero não são possivel.\n Tente novamente.")
                continue
            else:
                resultado = numero_1 * numero_2
                print(f"O resultado da operação divisão é {resultado}")
                
calculadora()
            
        