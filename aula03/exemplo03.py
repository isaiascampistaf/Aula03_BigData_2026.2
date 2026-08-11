# Uma loja oferece 10% de desconto sobre o valor total da compra
#Solicite o preço do produto e quantidade comprada
# Calcule o valor total, aplique o desconto e informe o valor final.

#Entrada
preco= float(input("preço do produto: "))
quantidade= int(input("Quantidade compraa: ")) 

#processamento
total = preco * quantidade 
desconto = total * 0.1  #desconto de 10%
valor_pagar= total - desconto 

#Saida

print(30*'=')
print(f"Valor total: R$ {total: .2f}")
print(f"Valor a pagar: R$ {valor_pagar: .2f}")
print(f"Desconto de R$: {desconto: .2f}")

