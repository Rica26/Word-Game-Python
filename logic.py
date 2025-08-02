class JogoForca:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_usadas = set()
        self.tentativas = 10
        self.letras_adivinhadas = ["_"] * len(palavra)

    def palpite_valido(self, palpite):
        if len(palpite) == 1:
            return palpite.isalpha()
        return palpite.isalpha() and len(palpite) == len(self.palavra)

    def fazer_palpite(self, palpite):
        if not self.palpite_valido(palpite):
            return "Palpite inválido.", False

        if len(palpite) > 1:
            letras_erradas = [l for l in self.letras_usadas if l not in self.palavra]
            if any(l in palpite for l in letras_erradas):
                return "Palpite inválido: contém letras já tentadas que não estão na palavra.", False

            if palpite == self.palavra:
                self.letras_adivinhadas = list(self.palavra)
                return None, None
            else:
                self.tentativas = -1
                return None, None

        else:
            if palpite in self.letras_usadas:
                return "Você já usou essa letra. Tente outra.", False
            self.letras_usadas.add(palpite)
            if palpite in self.palavra:
                for i, letra in enumerate(self.palavra):
                    if letra == palpite:
                        self.letras_adivinhadas[i] = palpite
                return "Bom palpite!", True
            else:
                self.tentativas -= 1
                return "Palpite incorreto.", False

    def venceu(self):
        return "_" not in self.letras_adivinhadas

    def perdeu(self):
        return self.tentativas <= 0
