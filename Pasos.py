class Pasos:
    def __init__(self,orden,instruccion):
        self._orden = orden
        self._instruccion = instruccion

    @property
    def orden(self):
        return self._orden
    
    @orden.setter
    def orden(self,orden):
        self._orden = orden
    
    def getDic(self):
        diccionario = {"orden":self._orden, "instruccion": self._instruccion}
        return diccionario
    
    @property
    def instruccion(self):
        return self._instruccion
    
    @instruccion.setter
    def instruccion(self,instruccion):
        self._instruccion = instruccion
    
    def __str__(self):
        return f'Paso {self._orden}: {self._instruccion}'
    
if __name__ == "__main__":
    paso1 = Pasos(1,"Colocar Agua en una olla")
    print(paso1)
    print(paso1.getDic())