class Ingrediente:
    def __init__(self,nombre,unidadMedida,cantidad):
        self.nombre = nombre
        self.unidad_medida = unidadMedida
        self.cantidad = cantidad

    def getDic(self):
        diccionario = {"nombre":self.nombre,"unidad":self.unidad_medida,"cantidad":self.cantidad}
        return diccionario
    def __str__(self):
        return f"{self.nombre}, {self.cantidad} {self.unidad_medida}"
    

if __name__ == "__main__":
    mi_ingrediente = Ingrediente("Sal","gramos",5)
    print(mi_ingrediente.getDic())
    print(mi_ingrediente)
        