import subprocess
import tkinter as tk
from tkinter import messagebox

# Função para abrir a calculadora e exibir a mensagem
def abrir_calculadora_e_exibir_mensagem():
    # Caminho para a calculadora do Windows
    calc_path = "calc.exe"

    # Abrindo a calculadora
    try:
        subprocess.Popen([calc_path], shell=True)
    except Exception as e:
        print("Erro ao abrir a calculadora:", e)
    
    # Exibindo a mensagem
    messagebox.showinfo("Aviso", "Seu computador foi hackeado!")

# Criando a janela principal
root = tk.Tk()
root.withdraw()  # Oculta a janela principal

# Chamando a função para abrir a calculadora e exibir a mensagem
abrir_calculadora_e_exibir_mensagem()

# Mantém a janela de mensagem aberta
root.mainloop()
