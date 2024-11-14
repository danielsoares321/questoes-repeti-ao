print("1. Média ponderada, com pesos 2 e 3, respectivamente")
print("2. Quadrado da soma dos 2 números")
print("3. Cubo do menor número")
print("4. Sair")

e = input("Escolha uma opção: ")

a = "1"
b = "2"
c = "3"
d = "4"

if e == a:
    print("voce solicitou calcular a madia ponderada")
    nu1 = int(input("informe o valaor 1: "))
    nu2 = int(input("informe o valaor 2: "))
    media_p = (nu1 * 2 + nu2 * 3) / 5
    print(f"media ponderada é {media_p}")

elif e == b:
    print("voce solicitou calcular o quadrado da soma")
    nu1 = int(input("informe o valaor 1: "))
    nu2 = int(input("informe o valaor 2: "))
    quada_s = (nu1 + nu2) ** 2
    print(f"quadrado da soma {quada_s}")

elif e == c:
    print("voce solicitou calcularo cubo do menor número")
    nu1 = float(input("informe o menor numero"))
    cubo = nu1 ** 2
    print(f"o cubo do menor numero {cubo}")

elif e == d:
    print("voce solicitou sair ")
