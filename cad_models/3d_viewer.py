import numpy as np
import matplotlib.pyplot as plt
from simple_3dviz import Mesh
from simple_3dviz.window import show
from simple_3dviz.utils import render
from simple_3dviz import Scene
from simple_3dviz.behaviours.io import SaveFrames

x,y,z = [0,0,0]
if __name__ == "__main__":
   
    m = Mesh.from_file("cad_models/joystick.stl", color=(0.1, 0.8, 0.1))
    m.offset = (x,y,z)
    show(m, size=(640,640), background = (1,1,1), camera_position=(0, -100, -500), camera_target=(0, 0, 200), light=None)

