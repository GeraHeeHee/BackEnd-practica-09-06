"Gerardo Ramirez Martin del campo"
"06IDPRMA"
"2403230423"
from p5 import *
from classes.classes import *
from models.models import *

ancho_ventana = 600
alto_ventana = 600
ventana = None

def setup():
    global ventana
    size(ancho_ventana, alto_ventana)
    ventana = Ventana()

def draw():
    background(240) 
    ventana.dibujar()
    
run()