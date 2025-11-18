import tkinter as tk

janela = tk.Tk()
janela.title("minha primeira janela")
janela.geometry("300x200")

rotulo = tk.Label(janela, text="digite seu nome: ")
rotulo.pack(pady=10)

entrada = tk.Entry(janela)
entrada.pack(pady=5)

def clicar():
    nome = entrada.get()
    mensagem = f"Oii, princesa {nome}!"
    tk.Label(janela, text=mensagem).pack()
    
botao = tk.Button(janela, text="Enviar", command=clicar)
botao.pack(pady=10)

janela.mainloop()
