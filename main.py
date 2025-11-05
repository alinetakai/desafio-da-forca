# Ponto de entrada do jogo

from palavras import escolher_palavra
from logica import mostrar_palavra, verificar_letra, verificar_vitoria
from utils import limpar_tela, exibir_titulo

def main():
    palavra = escolher_palavra()
    letras_certas = set()
    letras_erradas = set()
    tentativas = 6

    while tentativas > 0:
        limpar_tela()
        exibir_titulo()
        print(mostrar_palavra(palavra, letras_certas))
        print(f"\n❌ Letras erradas: {', '.join(letras_erradas)}")
        print(f"Tentativas restantes: {tentativas}")

        letra = input("\nDigite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            input("Digite apenas uma letra válida. Pressione ENTER para continuar.")
            continue

        if letra in letras_certas or letra in letras_erradas:
            input("Você já tentou essa letra. Pressione ENTER para continuar.")
            continue

        if verificar_letra(letra, palavra, letras_certas, letras_erradas):
            print("✅ Boa! Letra correta!")
        else:
            print("❌ Letra errada!")
            tentativas -= 1

        if verificar_vitoria(palavra, letras_certas):
            limpar_tela()
            exibir_titulo()
            print(f"🎉 Parabéns! Você acertou a palavra: {palavra}")
            break

    else:
        print(f"😢 Fim de jogo! A palavra era: {palavra}")

if __name__ == "__main__":
    main()
