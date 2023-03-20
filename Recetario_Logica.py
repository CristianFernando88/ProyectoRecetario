from Recetario_Servicios import RecetasCrud as rc
from Receta import Receta
from Pasos import Pasos
from Ingrediente import Ingrediente
class RecetarioLogica:
    def __init__(self,ruta_archivo):
        self.ruta = ruta_archivo
        self.archivo = rc(ruta_archivo)
        
    
    def getRecetas(self):
        lista_diccionario = self.archivo.get_recetas()
        print(lista_diccionario)
        lista = []
        for dic in lista_diccionario:
            #print(dic)
            receta = Receta(dic["nombre"],dic["preparacion"],dic["coccion"])
            #print(dic["ingredientes"])
            print()
            #aux_i = []
            '''for ing in dic["ingredientes"]:
                ingrediente = Ingrediente(ing["nombre"],ing["unidad"],ing["cantidad"])
                aux_i.append(ingrediente)
                #print(ingrediente)
                #receta.agregar_ingrediente(ingrediente)
            print(len(aux_i))
            receta.ingredientes = aux_i
            for p in dic["pasos"]:
                paso = Pasos(p["orden"],p["instruccion"])
                receta.agregar_paso(paso)'''
            receta.creacion = dic["creacion"]
            receta.etiqueta = dic["etiqueta"]
            receta.favorito = dic["favorito"]
            lista.append(receta)
        return lista
        
    def agregarReceta(self,receta):
        '''agrega una receta al archivo'''
        if self.archivo.buscar_receta_nombre(receta.nombre) == -1:
            self.archivo.agregar_receta(receta.getDic())
            return True
        return False
    
    def getReceta(self,nombre):
        recetas = self.getRecetas()
        pos = self.archivo.buscar_receta_nombre(nombre)
        if pos != -1:
            return recetas[pos]
        else:
            return None

if __name__ == "__main__":
    rl = RecetarioLogica("Recetario.json")
    receta = rl.getReceta("Arroz con leche")
    print(rl.getRecetas())
    #print(receta)
    #print(receta.getDic())