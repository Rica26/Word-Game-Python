import requests

response = requests.get("https://random-word-api.herokuapp.com/word")
palavra_secreta = response.json()[0].lower()
letras_usadas = set()
tentativas = 9
letras_adivinhadas = ["_"] * len(palavra_secreta)



print(" ".join(letras_adivinhadas))

def palpite_valido(palpite):
    return len(palpite) == 1 and palpite.isalpha()

def fazer_palpite(palpite):
    global tentativas
    if not palpite_valido(palpite):
        print("Palpite inválido. Tente novamente.")
        return
    if palpite in letras_usadas:
        print("Você já usou essa letra. Tente outra.")
        return
    if palpite in palavra_secreta:
        print("Bom palpite!")
        for i, letra in enumerate(palavra_secreta):
            if letra == palpite:
                letras_adivinhadas[i] = palpite
    else:
        print("Palpite incorreto.")
        tentativas -= 1
    print(" ".join(letras_adivinhadas))
    print(f"Tentativas restantes: {tentativas}")
    if "_" not in letras_adivinhadas:
        print("Parabéns! Você adivinhou a palavra!")
        return True
    if tentativas == 0:
        print("Fim de jogo! A palavra era:", palavra_secreta)
        return True
    letras_usadas.add(palpite)
    return False

while tentativas > 0 and "_" in letras_adivinhadas:
    print("Letras usadas:", sorted(letras_usadas))
    palpite = input("Digite um palpite (uma letra): ").lower()
    if fazer_palpite(palpite):
        break