import tkinter as tk 
from tkinter import messagebox,simpledialog
from sistema import Sistema

class Apptk:
    def __init__(self,root):
        self .root = root
        self.root.title("Sistema de Cadasro")
        self.root.geometry("300x260")
        
        
        self.sistema = Sistema()
        
        tutulo = tk.Label(root, text="Sistema de Cadastro", font=("Arial",16))
        titulo.pack(pady=10)
        
        tk.Button(root, text="Cadastrar Usuário",width=25, command=self.janela_cadastrar).pack(pady=5)
        tk.Button(root, text="Listar Usuário",width=25, command=self.janela_listar).pack(pady=5)
        tk.Button(root, text="Buscar Usuário",width=25, command=self.janela_buscar).pack(pady=5)
        tk.Button(root, text="Sair",width=25, command=root.quit).pack(pady=5)
        
    def janela_cadastrar(self):
        win = tk.Toplevel()
        win.title("Cadastrar Usuário")
        win.geometry("300x200")
        
        tk.Label(win, text="Nome: ").pack()
        entry_nome = tk.Entry(win)
        entry_nome.pack()
        
        tk.Label(win, text="Idade: ").pack()
        entry_idade = tk.Entry(win)
        entry_idade.pack()
        
        tk.Label(win, text="E-mail: ").pack()
        entry_email = tk.Entry(win)
        entry_email.pack()
        
    def janela_listar(self):
         win = tk.Toplevel()
         win.title("Listar Usuário")
         win.geometry("350x300")
         
         usuarios = self.sistema.listar()
         
         if not usuarios:
             tk.Label(win, text="Nenhum usuário cadastrado.").pack(pady=20)
             return
         
         text_area = tk.Text(win, width=40, height=15)
         text_area.pack(pady=10)
         
         for u in usuarios:
             text_area.insert(tk.END, f"Nome: {u.nome}|Idade: {u.idade}\nEmail: {u.email}\n-----------------\n")
    
    def janela_buscar(self):
        email = simpledialog.askstring("Buscar Usuário", "Digite o e-mail:")   
        
        if not email:
            return
        
        usuario = self.sistema.buscar(email)     
        
        if usuario:
            messagebox.showinfo(
                "usuário Encontrado",
                f"Nome: {usuario.nome}\nIdade: {usuario.idade}\nEmail: {usuario.email}"
            )
        else:
            messagebox.showinfo("Não encontrado", "Nenhum usuário com esse e-mail/")
        