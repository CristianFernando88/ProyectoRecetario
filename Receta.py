import datetime as dt
from Ingrediente import Ingrediente
from Pasos import Pasos
class Receta:
    def __init__(self,nombre="",tiempoPreparacion="",tiempoCocion="",lista_ingredientes = [],lista_pasos= [],imagen=None,etiqueta="",favorito = False):
        self.nombre = nombre
        self.imagen = imagen
        self.tiempoPreparacion = tiempoPreparacion
        self.tiempoCocion = tiempoCocion
        self.ingredientes = lista_ingredientes
        self.lista_pasos = lista_pasos
        self.creacion = dt.datetime.now()
        self.etiqueta = etiqueta
        self.favorito = favorito

    def agregar_ingrediente(self,ingrediente):
        #ingrediente = Ingrediente(nombre,unidad,cantidad)
        self.ingredientes.append(ingrediente)

    def agregar_paso(self,paso):
        #paso = Pasos(orden,instruccion)
        self.lista_pasos.append(paso)
    
    def eliminar_paso(self,paso):
        tam = len(self.lista_pasos)
        for  i in range(0,tam):
            if self.lista_pasos[i].orden == paso.orden:
                pos = paso.orden
                del self.lista_pasos[i]
                for j in range(i,tam-1):
                    self.lista_pasos[j].orden = pos
                    pos+=1
                break

    def diccionario_pasos(self):
        lista = []
        for p in self.lista_pasos:
            lista.append(p.getDic())
        return lista
        
    def diccionario_ingredientes(self):
        lista = []
        for ing in self.ingredientes:
            lista.append(ing.getDic())     
        return lista
    
    def getDic(self):
        diccionario = {
            "nombre": self.nombre,
            "preparacion" : self.tiempoPreparacion,
            "coccion" : self.tiempoCocion,
            "ingredientes": self.diccionario_ingredientes(),
            "pasos": self.diccionario_pasos(),
            "creacion": str(self.creacion),
            "etiqueta": self.etiqueta,
            "favorito": self.favorito    
        }
        return diccionario

    def __str__(self):
        return f"nombre: {self.nombre}, preparacion: {self.tiempoPreparacion}, coccion: {self.tiempoCocion}"

if __name__ == "__main__":
    receta1 = Receta("arroz con leche","10 min","60 min")
    paso1 = "Hacer corona de harina"
    paso2 = "Colocar la salmuera"
    paso3 = "mezclar"
    paso4 = "Amasar"

    receta1.agregar_paso(paso1)
    receta1.agregar_paso(paso2)
    receta1.agregar_paso(paso3)
    receta1.agregar_paso(paso4)

    print(receta1.getDic())

    receta1.eliminar_paso(receta1.lista_pasos[2])

    print(receta1.getDic())

    #print(receta1)
    #print(receta1.getDic())
    #print(receta1.creacion)