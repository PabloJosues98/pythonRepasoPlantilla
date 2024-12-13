class NodoUsuario:
    def __init__(self,nombre,edad,genero):   #constructor con variables locales
        self.__nombre = nombre
        self.__edad = edad
        self.__genero = genero      #manejara solo H o M

        self.__siguiente = None       #este es el puntero a siguiente, se inicializa como nulo, o vacio
        #Los punteros nos permiten apuntar a otro objeto de la misma clase, en este caso a otro nodo
        #En realidad guardan la direccion de memoria del objeto al que apuntan

    def setNombre(self,nombre):
        self.__nombre=nombre

    def setEdad(self,edad):
        self.__edad=edad
    
    def setGenero(self,genero):
        self.__genero=genero

    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente

    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def getGenero(self):
        return self.__genero
    
    def getSiguiente(self):
        return self.__siguiente

    def mostrarDatos(self):
        print('---------DATOS USUARIO-------------')
        print('Nombre: ',self.__nombre)
        print('Edad: ',self.__edad)
        print('Genero: ',self.__genero)
        print('-----------------------------------')