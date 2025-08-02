# import requests
# import tkinter as tk

# response = requests.get("https://random-word-api.herokuapp.com/word")

# palavra_secreta = response.json()[0].lower()
# letras_usadas = set()
# tentativas = 10
# letras_adivinhadas = ["_"] * len(palavra_secreta)



# print(" ".join(letras_adivinhadas))

# def palpite_valido(palpite):
#     if len(palpite) == 1:
#         return palpite.isalpha()
#     return palpite.isalpha() and len(palpite) == len(palavra_secreta)


# def fazer_palpite(palpite):
#     global tentativas, letras_adivinhadas
#     entry_palpite.delete(0, tk.END)
#     if not palpite_valido(palpite):
#         label_mensagem.config(text="Palpite inválido.")
#         return
#     if len(palpite) > 1:
#         letras_erradas = [l for l in letras_usadas if l not in palavra_secreta]
#         if any(l in palpite for l in letras_erradas):
#             label_mensagem.config(text="Palpite inválido: contém letras já tentadas que não estão na palavra.", fg="orange")
#             return
#         if palpite == palavra_secreta:
#             letras_adivinhadas = list(palavra_secreta)
#         else:
#             tentativas = -1
#     else:
#         if palpite in letras_usadas:
#             label_mensagem.config(text="Você já usou essa letra. Tente outra.", fg="blue")
#             return
#         letras_usadas.add(palpite)
#         if palpite in palavra_secreta:
#             label_mensagem.config(text="Bom palpite!", fg="green")
#             for i, letra in enumerate(palavra_secreta):
#                 if letra == palpite:
#                     letras_adivinhadas[i] = palpite
#         else:
#             label_mensagem.config(text="Palpite incorreto.", fg="red")
#             tentativas -= 1
#     label_palavra.config(text=" ".join(letras_adivinhadas))
#     label_usadas.config(text="Letras usadas: " + ", ".join(sorted(letras_usadas)))

#     desenhar_forca()
#     if "_" not in letras_adivinhadas:
#         label_mensagem.config(text="Parabéns! Adivinhaste a palavra!", fg="green")
#         entry_palpite.config(state='disabled')
#         botao_palpite.config(state='disabled')
#     elif tentativas <= 0:
#         label_mensagem.config(text=f"Fim de jogo! A palavra era: {palavra_secreta}", fg="red")
#         entry_palpite.config(state='disabled')
#         botao_palpite.config(state='disabled')
    


# def desenhar_forca():
#     if tentativas == 9:
#         canvas.create_line(20, 180, 120, 180) 
#     elif tentativas == 8:
#         canvas.create_line(70, 180, 70, 20)    
#     elif tentativas == 7:
#         canvas.create_line(70, 20, 120, 20)    
#     elif tentativas == 6:
#         canvas.create_line(120, 20, 120, 40)   
#     elif tentativas == 5:
#         canvas.create_oval(110, 40, 130, 60)   
#     elif tentativas == 4:
#         canvas.create_line(120, 60, 120, 100)  
#     elif tentativas == 3:
#         canvas.create_line(120, 70, 100, 90)   
#     elif tentativas == 2:
#         canvas.create_line(120, 70, 140, 90)   
#     elif tentativas == 1:
#         canvas.create_line(120, 100, 100, 130) 
#     elif tentativas == 0:
#         canvas.create_line(120, 100, 140, 130)
#     elif tentativas == -1:
#         canvas.create_line(20, 180, 120, 180) 
#         canvas.create_line(70, 180, 70, 20)    
#         canvas.create_line(70, 20, 120, 20)    
#         canvas.create_line(120, 20, 120, 40)   
#         canvas.create_oval(110, 40, 130, 60)   
#         canvas.create_line(120, 60, 120, 100)  
#         canvas.create_line(120, 70, 100, 90)   
#         canvas.create_line(120, 70, 140, 90)   
#         canvas.create_line(120, 100, 100, 130) 
#         canvas.create_line(120, 100, 140, 130)

# janela = tk.Tk()
# janela.title("Jogo da Forca")
# janela.geometry("500x400")
# janela.configure(bg="#f0f8ff")
# label_palavra = tk.Label(janela, text=" ".join(letras_adivinhadas), font=("Helvetica", 24), bg="#f0f8ff")
# label_palavra.pack(pady=10)
# entry_palpite = tk.Entry(janela, font=("Helvetica", 16))
# entry_palpite.pack()
# botao_palpite = tk.Button(janela, text="Dar Palpite", command= lambda: fazer_palpite(entry_palpite.get().lower()), font=("Helvetica", 16), bg="#add8e6")
# botao_palpite.pack(pady=5)
# label_usadas = tk.Label(janela, text="Letras usadas: ", bg="#f0f8ff")
# label_usadas.pack()

# label_mensagem = tk.Label(janela, text="", fg="blue", bg="#f0f8ff")
# label_mensagem.pack(pady=5)

# canvas = tk.Canvas(janela, width=200, height=200, bg="white")
# canvas.pack(pady=10)

# janela.mainloop()

from api import buscar_palavra
from logic import JogoForca
from GUI import ForcaGUI

def main():
    palavra = buscar_palavra()
    jogo = JogoForca(palavra)
    gui = ForcaGUI(jogo)
    gui.rodar()

if __name__ == "__main__":
    main()