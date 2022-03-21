#creacion de clase Auto con sus metodos

from typing import Type


class Auto:
    cantidadCreados = 0 #atributo de clase
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        #atributos de instancia
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos #es un array de la clase Asiento
        self.marca = marca
        self.motor = motor # objeto de la clase Motor
        self.registro = registro
    #creacion de metodos
    def cantidadAsientos(self):
        total = 0
        for i in self.asientos:
            verificar = type(i) == Asiento
            if verificar == True:
                total += 1
        return total

    def verificarIntegridad(self):
        for i in self.asientos:
            if i != None:
                if self.registro == i.registro and self.registro == self.motor.registro:
                    return "Auto original"
                else:
                    return "Las piezas no son originales"
#creacion de clase Asiento con sus metodos

class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self,color):
        colores = ["rojo","verde","amarillo","negro","blanco"]
        if color not in colores:
            pass
        else:
            self.color = color
#creacion de clase Motor con sus metodos

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self,registro):
        self.registro = registro

    def asignarTipo(self,tipo):
        tipos = ["electrico","gasolina"]
        if tipo not in tipos:
            pass
        else:
            self.tipo = tipo

if __name__ == "__main__":
    a = Auto("model 3", 33000, list(),"tesla", Motor(4, "electrico", 142), 341)
    a.asientos = [Asiento("blanco", 5000, 435),None, None, Asiento("blanco", 5000, 435), None]
    
    print(a.cantidadAsientos)