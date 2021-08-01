from simple_3dviz import Scene
from simple_3dviz import Mesh, Spherecloud
from simple_3dviz.utils import save_frame
import numpy as np
import cv2
from PIL import Image, ImageOps
import matplotlib.image as mpimg




if __name__ == "__main__":
    scene = Scene(background=(0.0, 0.0, 0.0, 1.0), size=(512, 512))

    # Load a mesh from a file
    m = Mesh.from_file("cad_models/joystick.stl", color=(0.1,1,0))
    scene.add(m)    
    scene.camera_position = (0, -100, -500)
    scene.camera_target=(0, 0, 200)
    scene.render()
    
    save_frame("scenes.png", scene.frame)
    img = scene.frame
    img = Image.fromarray(img,'RGBA')
    # print(np.shape(img))
    # img = img.convert('RGB')
    # gray_image = ImageOps.grayscale(img)
    rgb_img = np.array(img)
    rgb_img = rgb_img[:, :, ::-1].copy()  
    print(np.shape(rgb_img))
    gray = cv2.cvtColor(rgb_img,cv2.COLOR_BGR2GRAY)
    img.show(rgb_img)
    # gray_image.show()
  