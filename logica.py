# Contém as funções de lógica

def mostrar_palavra(palavra, letras_certas):
    return " ".join([letra if letra in letras_certas else "_" for letra in palavra])

def verificar_letra(letra, palavra, letras_certas, letras_erradas):
    if letra in palavra:
        letras_certas.add(letra)
        return True
    else:
        letras_erradas.add(letra)
        return False

def verificar_vitoria(palavra, letras_certas):
    return all(letra in letras_certas for letra in palavra)
