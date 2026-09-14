idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você ainda é menor de idade.")

temperatura = float(input("Digite a temperatura: "))
if temperatura > 30:
    print("Está muito quente hoje!") 
valor_compra = float(input("Digite o valor da compra: R$ "))
if valor_compra >= 100:
    print("Você ganhou um desconto de 10%!")
else:
    print("Sem desconto. Aproveite as próximas promoções!") 
nota = float(input("Digite sua nota final: "))
if nota >= 9:
    print("Excelente desempenho!")
elif nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")