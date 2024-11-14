while True:
    print("************************************************")
    print("PROGRAMA PARA CÁLCULO DE GRANDEZAS ELÉTRICAS")
    print("************************************************")
    print("1. Tensão (em Volt)")
    print("2. Resistência (em Ohm)")
    print("3. Corrente (em Ampére)")
    print("0. SAIR DO PROGRAMA")
    print("************************************************")

    h = input("Qual grandeza deseja calcular(digite a opção)?")

    a = "1"
    b = "2"
    c = "3"
    d = "0"

    if h == a:
        print("voce escolheu calcular tensão")
        resistência = float(input("informe o valor da resistência"))
        corrente = float(input("informe o valor da corrente"))
        tensão = resistência*corrente
        print(f"a tensão é {tensão} volt")

    elif h == b:
        print("voce escolheu calcular resistência")
        tensão = float(input("informe o valor da corrente"))
        corrente = float(input("informe o valor da corrente"))
        resistência = tensão/corrente
        print(f"a resistência é {resistência} Ohm ")

    elif h == c:
        print("voce escolheu calcular corrente")
        tensão = float(input("informe o valor da corrente"))
        resistência = float(input("informe o valor da resistência"))
        corrente = tensão/resistência
        print(f"a corrente é {corrente} ampéres")
        
    elif h == d:
        print("sair do programa")
        break
