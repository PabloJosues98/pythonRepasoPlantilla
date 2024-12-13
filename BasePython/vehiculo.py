class vehiculo:
    def __init__(self, color, numero_asientos, tipo_vehiculo='Ninguno',activo=False):   #el self hace referencia a si mismo y permite modificarlos desde cualquier parte de la case
        self.__color = color                #declarar variable privada
        self.numero_asientos = numero_asientos      #variable publica
        self.__tipo_vehiculo = tipo_vehiculo
        self.__activo = activo              #variable booleana

    def set_color(self,color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_numero_asientos(self, numero_asientos):
        self.numero_asientos = numero_asientos

    def get_numero_asientos(self):
        return self.numero_asientos
    
    def get_tipo_vehiculo(self):
        return self.__tipo_vehiculo
    
    def __cambiarEstado(self):                  #metodo privado
        self.__activo = not self.__activo

    def mostrarEstado(self):
        self.__cambiarEstado()
        print('Estado del vehiculo: ',self.__activo)
    
    def mostrarDatos(self):
        print("tipo vehiculo ",self.__tipo_vehiculo," color ",self.__color," numero_asientos ",self.numero_asientos)