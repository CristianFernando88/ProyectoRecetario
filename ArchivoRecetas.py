import json
from Receta import Receta
from Pasos import Pasos
from Ingrediente import Ingrediente
class RecetasCrud:
    def __init__(self,ruta):
        self.ruta = ruta
        self.recetas = []
        self.existe_archivo()

    def agregar_receta(self,receta):
        '''Agrega una persona el archivo'''
        
        self.recetas.append(receta)
        with open(self.ruta,"w") as archivo:
            json.dump(self.recetas,archivo)
        
    def existe_archivo(self):
        lista = []
        try:
            with open(self.ruta,"r") as archivo:
                lista = json.load(archivo)
            self.recetas = lista
        except:
            with open(self.ruta,"w") as archivo:
                json.dump(lista,archivo)
            self.recetas = lista
        
if __name__ == "__main__":
    crud = RecetasCrud("Recetario.json")
    '''receta1 = Receta("arroz con leche","10 min","60 min")

    ingrediente1 = Ingrediente("leche","Lt",1)
    ingrediente2 = Ingrediente("Arroz","gs",250)
    
    receta1.agregar_ingrediente(ingrediente1)
    receta1.agregar_ingrediente(ingrediente2)
    
    paso1 = Pasos(1,"Lavar el Arroz")
    paso2 = Pasos(2,"Poner la Leche a fuego lento 10 min")
    receta1.agregar_paso(paso1)
    receta1.agregar_paso(paso2)'''


    #crud.agregar_receta(receta1.getDic())
    print(len(crud.recetas))
    #print(crud.recetas)
    for receta in crud.recetas:
        print(receta["nombre"])
