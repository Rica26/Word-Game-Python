import tkinter as tk

class ForcaGUI:
    def __init__(self, jogo):
        self.jogo = jogo
        self.janela = tk.Tk()
        self.janela.title("Jogo da Forca")
        self.janela.geometry("500x400")
        self.janela.configure(bg="#f0f8ff")

        self.label_palavra = tk.Label(self.janela, text=" ".join(self.jogo.letras_adivinhadas), font=("Helvetica", 24), bg="#f0f8ff")
        self.label_palavra.pack(pady=10)

        self.entry_palpite = tk.Entry(self.janela, font=("Helvetica", 16))
        self.entry_palpite.pack()

        self.botao_palpite = tk.Button(self.janela, text="Dar Palpite", command=self.processar_palpite, font=("Helvetica", 16), bg="#add8e6")
        self.botao_palpite.pack(pady=5)

        self.label_usadas = tk.Label(self.janela, text="Letras usadas: ", bg="#f0f8ff")
        self.label_usadas.pack()

        self.label_mensagem = tk.Label(self.janela, text="", fg="blue", bg="#f0f8ff")
        self.label_mensagem.pack(pady=5)

        self.canvas = tk.Canvas(self.janela, width=200, height=200, bg="white")
        self.canvas.pack(pady=10)

    def processar_palpite(self):
        palpite = self.entry_palpite.get().lower()
        self.entry_palpite.delete(0, tk.END)
        mensagem, valido = self.jogo.fazer_palpite(palpite)
        self.label_mensagem.config(text=mensagem, fg="green" if valido else "red")

        self.label_palavra.config(text=" ".join(self.jogo.letras_adivinhadas))
        self.label_usadas.config(text="Letras usadas: " + ", ".join(sorted(self.jogo.letras_usadas)))

        self.desenhar_forca()

        if self.jogo.venceu():
            self.label_mensagem.config(text="Parabéns! Adivinhaste!", fg="green")
            self.entry_palpite.config(state='disabled')
            self.botao_palpite.config(state='disabled')
        elif self.jogo.perdeu():
            self.label_mensagem.config(text=f"Fim de jogo! A palavra era: {self.jogo.palavra}", fg="red")
            self.entry_palpite.config(state='disabled')
            self.botao_palpite.config(state='disabled')

    def desenhar_forca(self):
        self.canvas.delete("all")
        tentativas = self.jogo.tentativas
        if tentativas <= 9:
            self.canvas.create_line(20, 180, 120, 180)  # Base
        if tentativas <= 8:
            self.canvas.create_line(70, 180, 70, 20)    # Poste
        if tentativas <= 7:
            self.canvas.create_line(70, 20, 120, 20)    # Viga superior
        if tentativas <= 6:
            self.canvas.create_line(120, 20, 120, 40)   # Cordão
        if tentativas <= 5:
            self.canvas.create_oval(110, 40, 130, 60)   # Cabeça
        if tentativas <= 4:
            self.canvas.create_line(120, 60, 120, 100)  # Corpo
        if tentativas <= 3:
            self.canvas.create_line(120, 70, 100, 90)   # Braço esquerdo
        if tentativas <= 2:
            self.canvas.create_line(120, 70, 140, 90)   # Braço direito
        if tentativas <= 1:
            self.canvas.create_line(120, 100, 100, 130) # Perna esquerda
        if tentativas <= 0:
            self.canvas.create_line(120, 100, 140, 130) # Perna direita

    def rodar(self):
        self.janela.mainloop()
