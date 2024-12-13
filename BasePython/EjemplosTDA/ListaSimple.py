from NodoUsuario import NodoUsuario
class ListaSimple:
    def __init__(self):
        self.__primero = None
        self.__ultimo = None        #tanto ultimo como cantidad son opcionales
        self.__cantidad = 0         #se pueden usar para optimizar tanto insercion, eliminacion como obtener la cantidad de elementos

    def insertar(self, nombre, edad, genero):
        nuevoNodo = NodoUsuario(nombre,edad,genero)     #se crea el nodo
        if self.__primero == None:                  #Si la lista esta vacia se asigna el nodo a primero y ultimo
            self.__primero = nuevoNodo
            self.__ultimo = nuevoNodo
        else:                                       #Si la lista no esta vacia se asigna el nodo a ultimo y se enlaza con el anterior
            #self.__ultimo.siguiente = nuevoNodo
            self.__ultimo.setSiguiente(nuevoNodo)    #enlazar con el ultimo nodo
            self.__ultimo = nuevoNodo               #el puntero ultimo apunta al nuevo nodo
            '''nodoActual = self.__primero
            while nodoActual != None:
                if nodoActual.getSiguiente() == None:
                    self.__ultimo.setSiguiente(nuevoNodo)
                    self.__ultimo = nuevoNodo
                nodoActual = nodoActual.getSiguiente()'''
        self.__cantidad += 1

    '''def cantidadNodos(self):
        nodoActual = self.__primero
        cantidad = 0
        while nodoActual != None:
            cantidad += 1
            nodoActual = nodoActual.getSiguiente()
        return cantidad'''

    def mostrar(self):
        nodoActual = self.__primero             #se crea un nodo actual que apunta al primero
        while nodoActual != None:               #valida que el nodo actual no sea nulo, es decir que no se haya llegado al final de la lista
            nodoActual.mostrarDatos()    #muestra los datos del nodo actual
            nodoActual = nodoActual.getSiguiente()  #el nodo actual toma el valor del siguiente nodo

    def buscar(self, nombre):
        nodoActual = self.__primero
        while nodoActual != None:
            if nodoActual.getNombre() == nombre:
                #nodoActual.mostrarDatos()
                return True
            nodoActual = nodoActual.getSiguiente()
        #print('No se encontro el nombre')
        return False

    def eliminar(self, nombre):
        nodoActual = self.__primero
        anterior = None                     #se crea un nodo anterior que se inicializa en nulo
        while nodoActual != None:
            if nodoActual.getNombre() == nombre:        #validamos si el nodo actual es el que buscamos
                if nodoActual == self.__primero:        #Validamos si el nodo actual es el primero
                    self.__primero = nodoActual.getSiguiente()  #el primero toma el valor del siguiente nodo
                                                                #esto elimina la referencia al objeto que esta al inicio
                                                                #y lo deja sin referencias, por lo que el recolector de basura lo elimina
                                                                #y el aputador señala al siguiente nodo 
                else:
                    anterior.setSiguiente(nodoActual.getSiguiente())    #el aputador de anterior deja de apuntar a nodo actual
                    #anterior.siguiente = nodoActual.siguiente      #y apunta al siguiente del nodo actual, dejando sin referencias al nodo actual
                                                                    #por lo que el recolector de basura lo elimina
                #print('Se elimino el nodo')
                self.__cantidad -= 1
                return True
            anterior = nodoActual                   #Este permite almacenar el nodoa actual en anterior, dado que en la siuiente iteracion sera el anterior
            nodoActual = nodoActual.getSiguiente()  #el nodo actual toma el valor del siguiente nodo, dado que en la siguiente itacion sera el nodo actual
            #nodoActual = nodoActual.siguiente
        #print('No se encontro ni elimino el nodo')
        return False
    
    def getCantidad(self):
        return self.__cantidad
    
    def mostrarUltimo(self):
        self.__ultimo.mostrarDatos()