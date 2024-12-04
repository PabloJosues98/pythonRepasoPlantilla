class vehiculo:
    def __init__(self, color, numero_asientos, tipo_vehiculo='Ninguno'):   #el self hace referencia a si mismo y permite modificarlos desde cualquier parte de la case
        self.__color = color                #declarar variable privada
        self.numero_asientos = numero_asientos
        self.__tipo_vehiculo = tipo_vehiculo
        
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
    
    def mostrarDatos(self):
        print("tipo vehiculo ",self.__tipo_vehiculo," color ",self.__color," numero_asientos ",self.numero_asientos)