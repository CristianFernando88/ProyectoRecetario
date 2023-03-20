import tkinter as tk
from tkinter import font,ttk,messagebox
from Receta import Receta
class VistaReceta:
    def __init__(self,parent,receta):
        self.parent = parent
        self.receta = receta
        self.ventana = tk.Toplevel(self.parent)
        self.ventana.title("Receta")
        
        self.nombre = self.receta.nombre.upper()
        #self.imagen = imagen
        self.tiempoPreparacion = self.receta.tiempoPreparacion
        self.tiempoCocion = self.receta.tiempoCocion
        self.ingredientes = self.receta.ingredientes
        self.lista_pasos = self.receta.lista_pasos
        self.creacion = self.receta.creacion
        self.etiqueta = self.receta.etiqueta
        self.favorito = self.receta.favorito
        self.crear_widget()
        self.agregar_contenido()
        
    def crear_widget(self):
        self.lbl_nombre = tk.Label(self.ventana,text=self.nombre,font = font.Font(family="Times",size=18),fg="DarkOrange4")
        self.lbl_nombre.grid(row=0,column=0,padx=5,pady=5)
        self.cuadro_texto = tk.Text(self.ventana,width=40,height=20)
        self.cuadro_texto.grid(row=1,column=0,padx=5,pady=5)
    
    def agregar_contenido(self):
        self.cuadro_texto.insert('end',"PREPARACION:\n")
        self.cuadro_texto.insert('end',self.tiempoPreparacion+"\n")
        self.cuadro_texto.insert('end',"COCCION:\n")
        self.cuadro_texto.insert('end',self.tiempoCocion+"\n")
        self.cuadro_texto.insert('end',"INGREDIENTES:\n")
        for ing in self.ingredientes:
            self.cuadro_texto.insert('end',f'{ing}\n')
        self.cuadro_texto.insert('end',"PASOS:\n")
        for p in self.lista_pasos:
            self.cuadro_texto.insert('end',f'{p}\n')
            
        self.cuadro_texto.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    receta1 = Receta("arroz con leche","10 min","60 min")
    v = VistaReceta(root,receta1)
    root.mainloop()