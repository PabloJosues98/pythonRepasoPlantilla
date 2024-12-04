from vehiculo import vehiculo
class terrestre(vehiculo):
    def __init__(self, modelo, color, numero_asientos, numero_llantas,marca):
        super().__init__(color, numero_asientos, 'Terrestre')
        self.__marca = marca
        self.__modelo = modelo
        self.__numero_llantas = numero_llantas

    def set_marca(self, marca):
        self.__marca = marca
    
    def get_marca(self):
        return self.__marca
    
    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_modelo(self):
        return self.__modelo
    
    def set_numero_llantas(self, numero_llantas):
        self.__numero_llantas = numero_llantas

    def get_numero_llantas(self):
        return self.__numero_llantas

    def mostrarDatos(self):
        super().mostrarDatos()
        print("marca ",self.__marca," modelo ",self.__modelo, " numero de llantas ",self.__numero_llantas)
        
