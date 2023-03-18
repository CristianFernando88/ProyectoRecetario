import tkinter as tk
from tkinter import ttk,messagebox
from Receta import Receta
from Ingrediente import Ingrediente
from Pasos import Pasos
from ArchivoRecetas import RecetasCrud
class Vista_Agregar:
    def __init__(self,parent,receta = None):
        self.parent = parent
         #variables
        self.nombre = tk.StringVar()
        self.preparacion = tk.StringVar()
        self.coccion = tk.StringVar()
        self.etiqueta = tk.StringVar()
        self.fecha = None

        if receta == None:
            self.receta = Receta()
        else:
            self.receta = receta
        self.crear_widgets()  

    def crear_widgets(self):
        ventana = tk.Toplevel(self.parent)
        ventana.title("Agregar Receta")   

        
        lbl_nombre = tk.Label(ventana,text="Nombre Receta")
        lbl_nombre.grid(row=0,column=0,padx=10,pady=5)
        input_nombre = tk.Entry(ventana,width=20,textvariable=self.nombre)
        input_nombre.grid(row=0,column=1,padx=5,pady=5)

        lbl_preparacion = tk.Label(ventana,text="Tiempo Preparacion (min): ")
        lbl_preparacion.grid(row=1,column=0,padx=10,pady=5)
        input_preparacion = tk.Entry(ventana,width=20,textvariable=self.preparacion)
        input_preparacion.grid(row=1,column=1,padx=5,pady=5)

        lbl_cocccion = tk.Label(ventana,text="Tiempo Coccion (min): ")
        lbl_cocccion.grid(row=2,column=0,padx=10,pady=5)
        input_coccion = tk.Entry(ventana,width=20,textvariable=self.coccion)
        input_coccion.grid(row=2,column=1,padx=5,pady=5)

        lbl_clave = tk.Label(ventana,text="Etiqueta: ",textvariable=self.etiqueta)
        lbl_clave.grid(row=3,column=0,padx=10,pady=5)
        input_clave = tk.Entry(ventana,width=20)
        input_clave.grid(row=3,column=1,padx=5,pady=5)

        lbl_creacion = tk.Label(ventana,text="Fecha Creacion: ")
        lbl_creacion.grid(row=4,column=0,padx=10,pady=5)
        input_creacion = tk.Entry(ventana,width=20,state=tk.DISABLED)
        input_creacion.grid(row=4,column=1,padx=5,pady=5)

        ''''image = Image.open(file="default.png")
        image = image.resize((100,100), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        lbl_img = tk.Label(ventana,image=img)
        lbl_img.grid(row=0,column=4)'''

        #cuadro ingredientes
        #variables ingredientes
        self.nom_ing = tk.StringVar()
        self.unidad = tk.StringVar()
        self.cant = tk.StringVar()
        self.estado_cajas_ingrediente = False

        frame_ingredientes = tk.LabelFrame(ventana,text="Ingredientes")
        frame_ingredientes.grid(row=5,column=0,columnspan=2,padx=5)
        
        lbl_non_ingr = tk.Label(frame_ingredientes,text="Nombre:")
        lbl_non_ingr.grid(row=0,column=0,padx=5,pady=5)
        self.entry_nom_ingr = tk.Entry(frame_ingredientes,textvariable=self.nom_ing,state=tk.DISABLED)
        self.entry_nom_ingr.grid(row=0,column=1,padx=5,pady=5)

        lbl_medida = tk.Label(frame_ingredientes,text="Unida de Medida:")
        lbl_medida.grid(row=1,column=0,padx=5,pady=5)
        self.entry_medida = tk.Entry(frame_ingredientes,textvariable=self.unidad,state=tk.DISABLED)
        self.entry_medida.grid(row=1,column=1,pady=5)

        lbl_cantidad = tk.Label(frame_ingredientes,text="Cantidad:")
        lbl_cantidad.grid(row=2,column=0,padx=5,pady=5)
        self.entry_cantidad = tk.Entry(frame_ingredientes,textvariable=self.cant,state=tk.DISABLED)
        self.entry_cantidad.grid(row=2,column=1,pady=5)
        
        self.list_ingredientes = tk.Listbox(frame_ingredientes,width=50)
        self.list_ingredientes.grid(row=4,column=0,columnspan=4,padx=5,pady=5,rowspan=4)
        btn_nuevo = tk.Button(frame_ingredientes,text="Nuevo",command=self.config_cajas_ingredientes)
        btn_nuevo.grid(row=0,column=3,sticky=tk.EW,padx=5)
        btn_guardar = tk.Button(frame_ingredientes,text="Guardar",command=self.guardar_ingrediente)
        btn_guardar.grid(row=1,column=3,sticky=tk.EW,padx=5)
        btn_quitar = tk.Button(frame_ingredientes,text="Quitar",command=self.eliminar_ingrediente)
        btn_quitar.grid(row=2,column=3,sticky=tk.EW,padx=5)

        
        
        #cuadro preparacion
        #variables preparacion
        self.orden = tk.StringVar()
        self.paso = tk.StringVar()
        

        frame_preparacion = tk.LabelFrame(ventana,text="Preparacion")
        frame_preparacion.grid(row=5,column=2,columnspan=2,padx=5,sticky=tk.N)

        lbl_orden = tk.Label(frame_preparacion,text="Orden")
        lbl_orden.grid(row=0,column=0,padx=5,pady=5)
        entry_orden = tk.Entry(frame_preparacion,textvariable=self.orden)
        entry_orden.grid(row=0,column=1,padx=5,pady=5,columnspan=2)

        lbl_paso = tk.Label(frame_preparacion,text="Instruccion")
        lbl_paso.grid(row=1,column=0,padx=5,pady=5)
        entry_paso = tk.Entry(frame_preparacion,width=40,textvariable=self.paso)
        entry_paso.grid(row=1,column=1,padx=5,pady=5,columnspan=2)

        btn_nuevo_paso = tk.Button(frame_preparacion,text="Nuevo")
        btn_nuevo_paso.grid(row=2,column=0,padx=5,sticky=tk.EW)
        btn_guardar_paso = tk.Button(frame_preparacion,text="Guardar",command=self.agregar_pasos)
        btn_guardar_paso.grid(row=2,column=1,padx=5,sticky=tk.EW)
        btn_eliminar_paso = tk.Button(frame_preparacion,text="Quitar",command=self.eliminar_paso)
        btn_eliminar_paso.grid(row=2,column=2,padx=5,sticky=tk.EW)


        self.list_pasos = tk.Listbox(frame_preparacion,width=50)
        self.list_pasos.grid(row=3,column=0,columnspan=3,padx=5,pady=5)

        btn_guardarAll = tk.Button(ventana,text="Guardar",command=self.guardar_general)
        btn_guardarAll.grid(row=6,column=1,sticky=tk.EW)
    
    #boton guardar todo
    def validar_cajas_gral(self):
        if self.nombre.get() != "" and self.preparacion.get()!="" and self.coccion.get()!="":
            return True
        else:
            return False
        
    def guardar_general(self):
        if self.validar_cajas_gral():
            self.receta.nombre = self.nombre.get()
            self.receta.tiempoPreparacion = self.preparacion.get()
            self.receta.tiempoCocion = self.coccion.get()
            self.receta.etiqueta = self.etiqueta.get()
            print(self.receta.getDic())
            archivo_receta = RecetasCrud("Recetario.json")
            archivo_receta.agregar_receta(self.receta.getDic())
        else:
            messagebox.showwarning("Agregar Producto","Las cajas principales estan vacias")

    #funciones para caja de ingredientes
    def guardar_ingrediente(self):
        ingrediente = Ingrediente(self.nom_ing.get(),self.unidad.get(),self.cant.get())
        self.limpar_ingrediente()
        self.config_cajas_ingredientes()
        self.list_ingredientes.insert(tk.END,ingrediente)
        self.receta.agregar_ingrediente(ingrediente)
    
    def eliminar_ingrediente(self):
        indice = self.list_ingredientes.curselection()[0]
        #print(indice)
        self.list_ingredientes.delete(indice)

    def limpar_ingrediente(self):
        self.nom_ing.set("")
        self.unidad.set("")
        self.cant.set("")

    def config_cajas_ingredientes(self):
        #print(self.entry_nom_ingr.configure["state"])
        if self.estado_cajas_ingrediente:
            self.entry_nom_ingr.configure(state=tk.DISABLED)
            self.entry_medida.configure(state=tk.DISABLED)
            self.entry_cantidad.configure(state=tk.DISABLED)
            self.estado_cajas_ingrediente = False
        else: 
            self.entry_nom_ingr.configure(state=tk.NORMAL)
            self.entry_medida.configure(state=tk.NORMAL)
            self.entry_cantidad.configure(state=tk.NORMAL)
            self.estado_cajas_ingrediente = True

    #funciones para cajas de pasos

    def agregar_pasos(self):
        paso = Pasos(self.orden.get(),self.paso.get())

        self.list_pasos.insert(tk.END,paso)
        self.receta.agregar_paso(paso)

        self.orden.set("")
        self.paso.set("")

        '''pos = len(self.lista_auxilar_p)+1
        self.lista_auxilar_p.append((pos,self.paso.get()))
        self.list_pasos.insert(tk.END,self.paso.get())
        print(self.lista_auxilar_p)
        print(self.lista_auxilar_p[pos-1][0])'''

    def eliminar_paso(self):
        pass
        '''indice = self.list_pasos.curselection()[0]
        #print(indice)
        #self.list_pasos.delete(indice)
        self.list_pasos.delete(0, tk.END)
        del self.lista_auxilar_p[indice]
        for i in range(indice,len(self.lista_auxilar_p)):
            self.lista_auxilar_p[i][0] = i+1
        for i in range(0,len(self.lista_auxilar_p)):
            self.list_pasos.insert(i,"Paso "+str(self.lista_auxilar_p[i][0])+": "+self.lista_auxilar_p[i][1])
        print(self.lista_auxilar_p)'''

if __name__ == "__main__":
    root = tk.Tk()
    ventana = Vista_Agregar(root)
    root.mainloop()
    