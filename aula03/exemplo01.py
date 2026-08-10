# GitHUB
print("GitHub- Aula 03")

# Um veiculo percorre 10km com cada litro de combustivel
# Considere duas distancias percorridas e calcule a quantidade
# de combustivel necessária para realizar o percurso total
# Apresente a distancia total e o combustivel necessário.

# Exemplo 01 - Veiculo 10km/1
#Entrada
CONSUMO= 10   #Quando em CAPS, é constante, valor fixo. 
distancia1 = float(input("Informe a distancia: "))
distancia2 = float(input("Informe a 2º distancia: "))

#Processamento (algoritimo é composto por entrada, processamento, saida) pode ocorrer de nao ter processamento
distancia_total= distancia1 + distancia2 
combustivel= distancia_total / CONSUMO 

#Saida
print(f"Distancia percorrida: {distancia_total}")
print(f"Consumo de {combustivel} litros")
