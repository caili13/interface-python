import tkinter as tk

def enviar():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    resultado.config(text=f"nome: {nome}, idade: {idade}")
    
janela = tk.Tk()
janela.title("cadastro Simples")
janela.geometry("300x200")
    
tk.Label(janela,text="nome:").grid(row=0, column=0,padx=10, pady=5)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1)
    
tk.Label(janela,text="idade:").grid(row=1, column=0,padx=10, pady=5)
entrada_idade = tk.Entry(janela)
entrada_idade.grid(row=1, column=1)
    
tk.Button(janela, text="Enviar", command=enviar).grid(row=2, column=1, pady=5)
resultado = tk.Label(text="")
resultado.grid(row=3, column=0,columnspan=2)
    
janela.mainloop()