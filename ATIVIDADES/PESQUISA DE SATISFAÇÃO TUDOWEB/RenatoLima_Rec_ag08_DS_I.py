# Pesquisa de Satisfação - TudoWeb

excelente = 0
bom = 0
ruim = 0

print("===================================")
print("  PESQUISA DE SATISFAÇÃO - TUDOWEB")
print("===================================")

for i in range(1, 51):
    print(f"\nEntrevistado {i} de 50")

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    print("\nComo você avalia nosso atendimento?")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opção: "))

    if opiniao == 1:
        excelente += 1
        print("Obrigado! Sua avaliação foi EXCELENTE.")

    elif opiniao == 2:
        bom += 1
        print("Obrigado! Sua avaliação foi BOA.")

    elif opiniao == 3:
        ruim += 1
        print("Obrigado! Sua avaliação foi RUIM.")

    else:
        print("Opção inválida! Resposta não contabilizada.")

# Resultado final
print("\n===================================")
print("       RESULTADO DA PESQUISA")
print("===================================")

print(f"Respostas EXCELENTE: {excelente}")
print(f"Respostas BOM: {bom}")
print(f"Respostas RUIM: {ruim}")

print("\nPesquisa finalizada!")