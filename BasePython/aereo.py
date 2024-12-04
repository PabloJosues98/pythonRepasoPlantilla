from vehiculo import vehiculo
class aereo(vehiculo):
    def __init__(self, color, numero_asientos, numero_motores, numero_alas, nombre_duenio):
        super().__init__(color, numero_asientos,'Aereo')
        self.__numero_motores = numero_motores
        self.__numero_alas = numero_alas
        self.__nombre_duenio = nombre_duenio

    def set_numero_motores(self, numero_motores):
        self.__numero_motores = numero_motores

    def set_numero_alas(self, numero_alas):
        self.__numero_alas = numero_alas

    def set_nombre_duenio(self, nombre_duenio):
        self.__nombre_duenio = nombre_duenio

    def get_numero_motores(self):
        return self.__numero_motores

    def get_numero_alas(self):
        return self.__numero_alas

    def get_nombre_duenio(self):
        return self.__nombre_duenio

    def mostrarDatos(self):
        super().mostrarDatos()
        print("numero de motores ",self.__numero_motores," numero de alas ",self.__numero_alas, " nombre del dueño ",self.__nombre_duenio)