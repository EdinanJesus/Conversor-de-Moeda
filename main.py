from tkinter import Tk, ttk
from tkinter import *

from PIL import Image, ImageTk, ImageOps, ImageDraw
import requests
import json
import string

#Collorl

cor0 = "#FFFFFF"  # white / branca
cor1 = "#333333"  # black / preta
cor2 = "#38576b"  # dark blue / azul escuro

#configuracao janela

janela = Tk()
janela.geometry('300x320')
janela.title("Conversor")
janela.configure(bg=cor0)
janela.resizable(width=FALSE, height=FALSE)

style= ttk.Style(janela)
style.theme_use("clam")

#divisao da janela

Frame_cima = Frame(janela, width=300, height=60, padx=0, pady=0, bg=cor2, relief="flat")
Frame_cima.grid(row=0, column=0, columnspan=2)

Frame_baixo = Frame(janela, width=300, height=260, padx=0, pady=5, bg=cor0, relief="flat")
Frame_baixo.grid(row=1, column=0, sticky=NSEW)

#funcao converter

def  converter():
   moeda_de = combo_de.get()
   moeda_para = combo_para.get()
   valor_entrada = valor.get()
   response =requests.get('https://api.exchangerate-api.com/v4/latest/{}'.format(moeda_de))
   dados = json.loads(response.text)
   cambio = (dados['rates'][moeda_para])

   #para multiplicar o valor
   resultado = float(valor_entrada)*float(cambio)

   if moeda_para == 'USD':
    simbolo= '$'
   elif moeda_para == 'EUR':
    simbolo= '€'
   elif moeda_para == 'INR':
    simbolo= '₹'
   elif moeda_para == 'AOA':
    simbolo= 'Kz'
   else:
    simbolo= 'R$'

   moeda_equivalente = simbolo + "{:,.2f}".format(resultado)
    
   app_resultado['text'] = moeda_equivalente

def new_func():
    moeda_de = 'USD'
    return moeda_de
#configurando frame cima

icon = Image.open("./icon.png")
icon = icon.resize((40,40))
icon = ImageTk.PhotoImage(icon)

app_nome = Label(Frame_cima, image=icon, compound=LEFT, text="Conversor de Moedas", height=5, pady=30, padx=13, relief=RAISED, anchor=CENTER, font=("Arial 16 bold"), bg=cor2, fg=cor0)
app_nome.place(x=0, y=0)

#configurando frame baixo

app_resultado = Label(Frame_baixo, text="", width=16, height=2, relief='solid', anchor=CENTER, font=("Ivy 15 bold"), bg=cor0 , fg=cor1)
app_resultado.place(x=50, y=10)

moeda = ["AOA","BRL","EUR","INR","USD"]

app_de = Label(Frame_baixo, text="De", width=8, height=1, relief= "flat", anchor=NW, font=("Ivy 10 bold"), bg=cor0 , fg=cor1)
app_de.place(x=48, y=90)
combo_de = ttk.Combobox(Frame_baixo, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo_de.place(x=50, y=115)
combo_de['values'] = (moeda)

app_para = Label(Frame_baixo, text="Para", width=8, height=1, relief= "flat", anchor=NW, font=("Ivy 10 bold"), bg=cor0 , fg=cor1)
app_para.place(x=158, y=90)
combo_para = ttk.Combobox(Frame_baixo, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo_para.place(x=160, y=115)
combo_para['values'] = (moeda)

valor = Entry(Frame_baixo, width=22, justify=CENTER, font=("Ivy 12 bold"), relief=SOLID)
valor.place(x=50, y=155)

botao = Button(Frame_baixo,command= converter, text="CONVERTER", width=19, padx=5, height=1, bg=cor2, fg=cor0, font=("Ivy 12 bold"), relief='raised',overrelief=RIDGE)
botao.place(x=50, y=210  )


janela.mainloop()
