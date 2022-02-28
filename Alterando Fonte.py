from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Escrevendo em diversas fontes e cores")
menu_inicial.geometry("800x600")

label_1 = Label(menu_inicial, text="Eu amo programar.", bg="yellow",fg="blue", font="Arial 14")
label_1.pack()

label_2 = Label(menu_inicial, text="Python é a melhor linguagem existente.",
                bg="light green",fg="black", font="Times 14 italic")
label_2.pack()

label_3 = Label(menu_inicial, text="Programar é tudo de bom", bg="white",fg="dark blue", font="Verdana 15")
label_3.pack()

label_4 = Label(menu_inicial, text="Programando se aprende a se tornar um grande programador.",
                bg="light gray",fg="dark green", font="Script 25")
label_4.pack()

menu_inicial.mainloop()