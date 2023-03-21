import tkinter as tk
from tkinter import ttk,messagebox
from Vista_AgregarModificar import Vista_Agregar
from Recetario_Logica import RecetarioLogica as rl
from Vista_Receta import VistaReceta as vr
import math
import datetime as dt


class Recetario(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.width=900
        self.parent.height=450
        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (self.parent.width, self.parent.height, (self.screenwidth - self.parent.width) / 2, (self.screenheight - self.parent.height) / 2)
        self.parent.geometry(self.alignstr)
        self.parent.title("RECETARIO")
        self.parent.iconbitmap('icono.ico')
        self.recetario = rl("Recetario.json")
        self.crear_widgets()
        self.llenar_tabla_recetas()

    def crear_widgets(self):
        self.entry_buscar = tk.Entry(self.parent,width=30)
        self.entry_buscar.grid(row=0,column=0,pady=20,sticky=tk.EW,padx=10)

        self.btn_buscar = tk.Button(self.parent,text="Buscar Receta")
        self.btn_buscar.grid(row=0,column=1,sticky=tk.W)
        
        
        self.frame_recetas = ttk.LabelFrame(self.parent,text="Recetas")
        self.frame_recetas.grid(row=1,column=0,columnspan=4)

        self.tabla_recetas = ttk.Treeview(self.frame_recetas, columns=tuple(['nombre', 'preparacion', 'coccion','etiqueta']))
        self.tabla_recetas.grid(row=1, column=0, columnspan=4,padx=10, pady=5)
        
        # asignamos tamño a las columnas
        self.tabla_recetas.column("#0", width=40, minwidth=10)
        self.tabla_recetas.column("nombre", width=200, minwidth=10)
        self.tabla_recetas.column("preparacion", width=100, minwidth=10)
        self.tabla_recetas.column("coccion", width=100, minwidth=10)
        self.tabla_recetas.column("etiqueta", width=100, minwidth=10)
        

        # colocamos nombres a la cabecera
        self.tabla_recetas.heading("#0", text="N°", anchor="center")
        self.tabla_recetas.heading("nombre", text="Nombre", anchor="center")
        self.tabla_recetas.heading("preparacion", text="Preparación", anchor="center")
        self.tabla_recetas.heading("coccion", text="Cocción", anchor="center")
        self.tabla_recetas.heading("etiqueta", text="Etiqueta", anchor="center")
        
        #botones crud
        self.btn_refrescar = tk.Button(self.frame_recetas,text="Refrescar tabla", command=self.llenar_tabla_recetas)
        self.btn_refrescar.grid(row=0,column=3)
        
        self.btn_mostrar = tk.Button(self.frame_recetas,text="Mostrar Receta",command=self.mostrar_receta)
        self.btn_mostrar.grid(row=2,column=0)

        self.btn_agregar = tk.Button(self.frame_recetas,text="Agregar Receta",command=self.agregar)
        self.btn_agregar.grid(row=2,column=1)

        self.btn_modificar = tk.Button(self.frame_recetas,text="Modificar Receta",command=self.modificar)
        self.btn_modificar.grid(row=2,column=2)

        self.btn_modificar = tk.Button(self.frame_recetas,text="Eliminar Receta",command=self.eliminar_receta)
        self.btn_modificar.grid(row=2,column=3)
    
    def llenar_tabla_recetas(self):
        self.tabla_recetas.delete(*self.tabla_recetas.get_children())
        num=0
        if self.recetario.getRecetas() != []:
            #self.label_estado['text']=""
            for receta in self.recetario.getRecetas():
                num += 1
                self.tabla_recetas.insert("", tk.END, text=str(num),values=(receta.nombre,receta.tiempoPreparacion,receta.tiempoCocion,receta.etiqueta))

    
    def agregar(self):
        '''Abre una ventana top leve para agregar una receta'''
        self.ventana_agregar = Vista_Agregar(self.parent)
    
    def modificar(self):
        try:
            nombre = self.tabla_recetas.item(self.tabla_recetas.selection())['values'][0]
            #etiqueta = self.tabla_recetas.item(self.tabla_recetas.selection())['values'][3]
            buscado = self.recetario.getReceta(nombre)
            v_modificar = Vista_Agregar(self.parent,buscado)
        except Exception:
            messagebox.showwarning("Receta","Debe seleccionar una fila de la tabla")
         
    def mostrar_receta(self):
        try:
            nombre = self.tabla_recetas.item(self.tabla_recetas.selection())['values'][0]
            #etiqueta = self.tabla_recetas.item(self.tabla_recetas.selection())['values'][3]
            buscado = self.recetario.getReceta(nombre)
            v_mostrar = vr(self.parent,buscado)
            
        except Exception:
            messagebox.showwarning("Receta","Debe seleccionar una fila de la tabla")

    def eliminar_receta(self):
        try:
            nombre = self.tabla_recetas.item(self.tabla_recetas.selection())['values'][0]
            pos = self.recetario.buscarRecetaNombre(nombre)
            res = messagebox.askyesno(title="Confirmar",message="¿Estas seguro que deseas eliminar este elemento del recetario?")
            if res:
                self.recetario.eliminarReceta(pos)
                self.llenar_tabla_recetas()

        except Exception:
            messagebox.showwarning("Receta","Debe seleccionar una fila de la tabla")



root = tk.Tk()
recetario = Recetario(root)
root.mainloop()
