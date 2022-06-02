from tkinter import *
import Funcoes

janela = Tk()
janela.title("Lojito del Tadeo")

janela["bg"] = "Gray"

btAdministrador = Button(janela, width=20, height=2, text="Admin")  
btAdministrador.place(x=230 , y=160)

btCliente = Button(janela, width=20, height=2, text="Cliente")
btCliente.place(x=230 , y=205)

#Largura x Altura + Margem.Esqu + Margem.Topo
janela.geometry("600x400")
janela.mainloop()