import os 
from sqlite3 import Row
import tkinter
from turtle import down
import pyautogui as pg
import time
from tkinter import *
from cProfile import label


nunca=pg.locateOnScreen(r'C:\Users\lvpgpereira\Desktop\Projetos Python\edge\nunca.png')
site=pg.locateOnScreen(r"C:\Users\lvpgpereira\Desktop\Projetos Python\edge\sites.png")
padrao=pg.locateOnScreen(r"C:\Users\lvpgpereira\Desktop\Projetos Python\edge\padrao.png")
permitir=pg.locateOnScreen(r'C:\Users\lvpgpereira\Desktop\Projetos Python\edge\permitir.png')
reiniciar=pg.locateOnScreen(r'C:\Users\lvpgpereira\Desktop\Projetos Python\edge\reiniciar.png')


def configurar():

    site1 = site.get()
    test = str(site1)

    print(site1)

    pg.alert('Favor não mexer, a configuração vai iniciar!  Clicar em OK')

    #Abrindo as configurações do Edge
    pg.press('win')
    time.sleep(1)
    pg.write('Microsoft Edge')
    time.sleep(2)
    pg.press('enter')
    time.sleep(3)
    pg.write('edge://settings/defaultBrowser')
    pg.press('enter')
    time.sleep(3)
  pg.click()
    pg.press('enter')
    ##########################################
    

    #Consfiguração: Permitir que IE abra sites no Edge
  
    time.sleep(1)
    pg.press('tab')
    time.sleep(1)
    pg.press('tab')
    time.sleep(1)
    pg.press('enter')
    pg.press('down')
    pg.press('enter')

    #######################################

    pg.press('tab')
    pg.press('enter')
    ########################################




    #Permitir que os sites sejam recarregados como IE
    
    #Adicionando sites na execção
    pg.press('tab')
    time.sleep(1)
    pg.press('tab')
    time.sleep(1)
    pg.press('tab')
    time.sleep(1)
    pg.press('tab')
    time.sleep(1)
    pg.press('tab')
    time.sleep(1)
    pg.press('tab')
    time.sleep(1)
    pg.press('tab')
    time.sleep(5)
    pg.write(test)
    time.sleep(5)       
    pg.press('tab')
    time.sleep(1)
    pg.press('enter')
    time.sleep(1)

    pg.alert('Configuração realizada!')


configurar



janela = Tk()

janela.title("Automação Service Desk")
janela.geometry("600x400")
janela.configure(background="#dde")
texto = Label(janela, text="Vamos começar a configuração", background="#dde")
texto.place(x=115, y=70)

texto4 = Label(janela, text="Inserir o Site que deseja configurar", background="#dde")
texto4.place(x=115, y=90)

texto2 = Label(janela, text="Exemplo como o site deve ser colocado:", background="#dde")
texto2.configure(font=("Arial", 10, "bold"))
texto2.place(x=130, y=170)

texto3 = Label(janela, text="https://google.com", background="#dde")
texto3.configure(font=("Arial", 10, "bold"))
texto3.place(x=130, y=190)

site=Entry(janela)
site.grid(column=2, row=0, padx=25,pady=15 )
site.place(x=130, y=110)
 
botao = Button(janela, text="Iniciar configuração", command=configurar)
botao.place(x=133, y=140)

janela.mainloop()