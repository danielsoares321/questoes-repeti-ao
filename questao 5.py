# Definindo os candidatos e os tipos de voto
candidatos = {
    1: "José",
    2: "João",
    3: "Maria",
    4: "Ana"
}

# Inicializando contadores de votos
votos_candidatos = {1: 0, 2: 0, 3: 0, 4: 0}
votos_nulo = 0
votos_branco = 0
total_votos = 0

print("Código dos candidatos:")
for codigo, nome in candidatos.items():
    print(f"{codigo} - {nome}")
print("5 - Voto Nulo")
print("6 - Voto em Branco")
print("0 - Encerrar votação")

# Loop para registrar os votos
while True:
    voto = int(input("Digite o código do voto: "))
    
    # Encerrar votação com o código 0
    if voto == 0:
        break
    
    # Contabilizar votos válidos e especiais
    if voto in votos_candidatos:
        votos_candidatos[voto] += 1
    elif voto == 5:
        votos_nulo += 1
    elif voto == 6:
        votos_branco += 1
    else:
        print("Código de voto inválido! Tente novamente.")
        continue
    
    total_votos += 1

# Cálculo das porcentagens
percent_nulo = (votos_nulo / total_votos) * 100 if total_votos > 0 else 0
percent_branco = (votos_branco / total_votos) * 100 if total_votos > 0 else 0

# Exibindo resultados
print("\nResultados da eleição:")
for codigo, nome in candidatos.items():
    print(f"{nome}: {votos_candidatos[codigo]} votos")
print(f"Votos Nulos: {votos_nulo}")
print(f"Votos em Branco: {votos_branco}")
print(f"Percentual de votos Nulos: {percent_nulo:.2f}%")
print(f"Percentual de votos em Branco: {percent_branco:.2f}%")
