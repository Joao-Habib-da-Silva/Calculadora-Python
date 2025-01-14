import tkinter as tk


def calcular():
    try:
        resultado = eval(entrada.get())  
        entrada.delete(0, tk.END)  
        entrada.insert(0, str(resultado))  
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro") 


janela = tk.Tk()
janela.title("Calculadora Simples")

entrada = tk.Entry(janela, width=20, font=("Arial", 14), justify="right")
entrada.grid(row=0, column=0, columnspan=4)

botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

def botao_clicado(texto):
    if texto == "=":
        calcular()  
    elif texto == "C":
        entrada.delete(0, tk.END)  
    else:
        entrada.insert(tk.END, texto)  

for texto, linha, coluna in botoes:
    botao = tk.Button(janela, text=texto, width=5, height=2, command=lambda t=texto: botao_clicado(t))
    botao.grid(row=linha, column=coluna)


janela.mainloop()
