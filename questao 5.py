cand_1 = 0
cand_2 = 0
cand_3 = 0
cand_4 = 0
votos_nulo = 0
votos_branco = 0
total_votos = 0

print("Código dos candidatos:")
print("1 - José")
print("2 - João")
print("3 - Maria")
print("4 - Ana")
print("5 - Voto Nulo")
print("6 - Voto em Branco")
print("0 - Encerrar votação")

while True:
    voto = int(input("Digite o código do voto: "))
    
    if voto == 0:
        break

    elif voto == 1:
        cand_1 += 1
    elif voto == 2:
        cand_2 += 1
    elif voto == 3:
        cand_3 += 1
    elif voto == 4:
        cand_4 += 1
    elif voto == 5:
        votos_nulo += 1
    elif voto == 6:
        votos_branco += 1
    
    total_votos += 1

percent_nulo = (votos_nulo / total_votos) * 100
percent_branco = (votos_branco / total_votos) * 100 

print("Resultados da eleição:")
print(f"Candidato 1: {cand_1} votos")
print(f"Candidato 2: {cand_2} votos")
print(f"Candidato 3: {cand_3} votos")
print(f"Candidato 4: {cand_4} votos")
print(f"Votos Nulos: {votos_nulo}")
print(f"Votos em Branco: {votos_branco}")
print(f"Percentual de votos Nulos: {percent_nulo}")
print(f"Percentual de votos em Branco: {percent_branco}")
