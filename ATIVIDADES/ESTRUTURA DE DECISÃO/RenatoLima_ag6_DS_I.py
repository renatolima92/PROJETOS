# CAMPANHA DE DESCONSTOS PROGRESSIVOS!!!
#Entrada: valor total da compra
valor_total_compra = float(input("Digite o valor total da compra: R$ "))
#PROCESSAMENTO: o sistema calculara o desconto.
if valor_total_compra < 200:
    percentual_de_desconto = 0.05 # 5% de desconto
elif valor_total_compra <= 300:
    percentual_de_desconto = 0.10 # 10% de desconto
else:
    percentual_de_desconto = 0.15 # 15% de desconto
#Valor do desconto em Reais
valor_desconto = valor_total_compra * percentual_de_desconto
valor_final = valor_total_compra - valor_desconto
#SAÍDA: Valor final da compra com desconto
print("\n🛍️  RESUMO DA COMPRA")
print(f"💰 Valor da compra: R$ {valor_total_compra:.2f}")
print(f"🏷️  Desconto aplicado: R$ {valor_desconto:.2f}")
print(f"💳 Total a pagar: R$ {valor_final:.2f}")