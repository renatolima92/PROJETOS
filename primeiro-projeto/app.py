# Programa de Cálculo de média de notas
# Renato de Lima Leoncio

nome = (input("Digite o nome do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"\nAluno: {nome}")
print(f"Média: {media:.2f}")
if media >= 6:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")
    