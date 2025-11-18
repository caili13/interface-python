import tkinter as tk

expressao = ""

def clicar(valor):
    global expressao
    expressao += str(valor)
    texto_var.set(expressao)

def calcular():
    global expressao
    try:
        resultado = str(eval(expressao))
        texto_var.set(resultado)
        expressao = resultado
    except:
        texto_var.set("Erro")
        expressao = ""

def limpar():
    global expressao
    expressao = ""
    texto_var.set("")

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.resizable(False, False)

texto_var = tk.StringVar()
visor = tk.Entry(
    janela,
    textvariable=texto_var,
    font=("Arial", 20),
    bg="#5d1eee",
    fg="white",
    justify="right"
)
visor.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

frame_botoes = tk.Frame(janela)
frame_botoes.pack()

botoes = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for linha in range(4):
    for coluna in range(4):
        texto = botoes[linha][coluna]
        if texto == "=":
            botao = tk.Button(
                frame_botoes,
                text=texto,
                width=5,
                height=2,
                bg="#3c8f3f",
                fg="white",
                font=("Arial", 16),
                command=calcular
            )
        else:
            botao = tk.Button(
                frame_botoes,
                text=texto,
                width=5,
                height=2,
                font=("Arial", 16),
                command=lambda x=texto: clicar(x)
            )
        botao.grid(row=linha, column=coluna, padx=5, pady=5)

botao_limpar = tk.Button(
    janela,
    text="C",
    width=20,
    height=2,
    bg="red",
    fg="white",
    font=("Arial", 14),
    command=limpar
)
botao_limpar.pack(pady=10)

janela.mainloop()
