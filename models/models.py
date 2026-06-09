from p5 import *
from classes.classes import *

class Ventana (Figura):
    
    def __init__(self):
        self.cuadrado_base = Cuadrado(
            borde_color="#000000", borde_grosor=2,
            width=50, height=60,
            x=0, y=0,
            relleno="#CCA12A"
        )
        self.vidrio1 = Cuadrado(
            borde_color="#000000", borde_grosor=2,
            width=15, height=15,
            x=5, y=5,
            relleno="#77B9D3"
        )
        self.vidrio2 = Cuadrado(
            borde_color="#000000", borde_grosor=2,
            width=15, height=15,
            x=30, y=5,
            relleno="#77B9D3"
        )
        self.vidrio3 = Cuadrado(
            borde_color="#000000", borde_grosor=2,
            width=15, height=15,
            x=5, y=30,
            relleno="#77B9D3"
        )
        self.vidrio4 = Cuadrado(
            borde_color="#000000", borde_grosor=2,
            width=15, height=15,
            x=30, y=30,
            relleno="#77B9D3"
        )
        self.base = Cuadrado(
            borde_color="#000000", borde_grosor=2,
            width=50, height=10,
            x=0, y=50,
            relleno="#D15C3F"
        )
    def dibujar(self):
        self.cuadrado_base.dibujar()
        self.vidrio1.dibujar()
        self.vidrio2.dibujar()
        self.vidrio3.dibujar()
        self.vidrio4.dibujar()
        self.base.dibujar()