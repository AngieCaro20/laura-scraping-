import requests
import tkinter as tk
from tkinter import tk

#para crear la ventana esa
ventana = tk.Tk()
ventana.title("Love of my life")  
ventana.iconbitmap("rocky_paw_patrol_canine_patrol_icon_263826.ico")  
ventana.geometry("900x600")  
ventana.resizable(False, True)


frame1 = tk.Frame(ventana)
frame1.configure(width=600, height=280, bg="cyan3", bd=20)
frame1.pack(pady=20)  


def obtener_celulares():
    url = "https://api.mercadolibre.com/sites/MLA/search?q=samsung"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos["results"]


def mostrar_resultados():
    resultados = obtener_celulares()
    for resultado in resultados:
        print(resultado['title'])  


boton = tk.Button(frame1, text="OPRIMEME", command=mostrar_resultados)
boton.pack(pady=10)  
ventana.mainloop()