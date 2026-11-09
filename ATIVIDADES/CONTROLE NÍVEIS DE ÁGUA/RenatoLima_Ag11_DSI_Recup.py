from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

# Lista com os níveis do reservatório
niveis_agua = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)"
]

# Função para definir a cor conforme o nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Simulação dos níveis registrados
leituras = [1, 2, 3, 4, 5]

# Exibe as mensagens com suas respectivas cores
print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

for nivel in leituras:
    cor = definir_cor(nivel)
    mensagem = niveis_agua[nivel - 1]

    print(cor + mensagem + Style.RESET_ALL)
