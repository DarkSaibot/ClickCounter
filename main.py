import tkinter as tk

root = tk.Tk()
root.geometry('600x600')
root.title("Contador De Clicks")
root.configure(background='#0d0142')

numero = 0

def acrescentar_click():
    global numero
    numero = numero + 1
    contador_clicks.configure(text=numero)
    

def decrementa_click():
    global numero
    numero = numero - 1
    contador_clicks.configure(text=numero)
    

    

margem = tk.Canvas(root, height=200, background= '#0d0142', bd=0, highlightthickness= 0, relief= 'flat')
margem.pack()

botao_adicionar = tk.Button(root, bg='#FFFFFF', text='+', font=("Gotham", 15, 'bold'), padx= 10, command= acrescentar_click)
botao_adicionar.pack() 

contador_clicks = tk.Label(root, text=numero,fg='#FFFFFF',bg = "#0d0142", font=("Gotham", 15, 'bold'))
contador_clicks.pack()

botao_retirar = tk.Button(root, bg='#FFFFFF', text='-', font=("Gotham", 15, 'bold'), padx= 13, command= decrementa_click)
botao_retirar.pack() 








root.mainloop()

