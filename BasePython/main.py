from vehiculo import vehiculo  #importaciones from "nombre de archivo sin extension.py" importar "nombre de clase"
from terrestre import terrestre
from aereo import aereo

if __name__ == '__main__':
    print('prueba')
    vehiculo1 = vehiculo('rojo', 4)         #creacion de objeto vehiculo
    #vehiculo1.__cambiarEstado()             #No se afecta ya que el metodo es privada
    vehiculo1.mostrarEstado()                   #si se afecta ya que la variable es publica
    vehiculo1.mostrarDatos()
    vehiculo1.mostrarEstado()
    vehiculo1.__color='azul'        #No se afecta ya que la variables es privada
    vehiculo1.numero_asientos=5     #si se afecta ya que la variable es publica
    vehiculo1.mostrarDatos()    
    vehiculo1.set_color('verde')
    vehiculo1.set_numero_asientos(6)
    vehiculo1.mostrarDatos()

    vehiculo2 = terrestre('Toyota', 'Corolla', 'naranja', 5, 4)    #creacion de objeto terrestre
    vehiculo2.mostrarDatos()
    vehiculo2.__marca='Honda'        #No se afecta ya que la variables es privada
    vehiculo2.set_modelo('Protege')  #si se afecta ya que la variable es publica
    vehiculo2.mostrarDatos()
    vehiculo2.set_marca('Honda')
    vehiculo2.set_modelo('Civic')
    vehiculo2.set_color('negro')
    vehiculo2.set_numero_asientos(4)
    vehiculo2.set_numero_llantas(5)
    vehiculo2.mostrarDatos() 

    print('*****    Creacion del objeto aereo')
    vehiculo3 = aereo('Naranja',8,2,4,'Jorge')
    print('-----     Mostrando los datos para inicializacion')
    vehiculo3.mostrarDatos()
    vehiculo3.set_color('Verde')
    vehiculo3.set_numero_asientos(5)
    vehiculo3.set_numero_motores(4)
    vehiculo3.set_numero_alas(2)
    vehiculo3.set_nombre_duenio('Carlos')
    print('-----     Mostrando los datos despues de modificar las variables privadas por medio de metodos publicos')
    vehiculo3.mostrarDatos()

    nombre="Jorge"
    print("valor de nombre: "+nombre)
    print(type(nombre))
    nombre=3
    print("valor de nombre: ",nombre)
    print(type(nombre))
    suma=2+nombre
    print(suma)

    