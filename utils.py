# Funções auxiliares

import os
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def exibir_titulo():
    print("🎯 JOGO DA FORCA 🎯")
    print("-" * 25)
