#Uma pessoa deseja comprar ingressos para um evento e possui um valor disponivel para gastar
# Solicite o preço de cada ingresso e o valor disponivel.
# Calcule quantos ingressos podem ser comprados e qual será o troco.

preco_unitario = float(input("Valor do Ingresso: "))

valor_disponivel = float(input("Informe o valor disponivel: "))

quantidade = int(valor_disponivel // preco_unitario)
troco = valor_disponivel % preco_unitario 

print(f"Quantidade de ingressos: {quantidade}")
print(f"Troco: {troco}")