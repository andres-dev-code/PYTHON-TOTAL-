from os import *
from pathlib import Path

usuario = input("Cual es tu nombre?")

local_de_recetas = Path(Path.home(),'Recetas')
print(local_de_recetas)