import os

from object_3d import *

## TODO: FIX
## ONJY FOR .obj FILES
## File should be to dir "~WORK_DIRECTORY~/models/"
def get_object_from_obj(render, filename):
  vertex, faces = [], []
  file = os.path.join('models/', filename)
  if not filename.endswith('.obj'):
    raise TypeError("Unknown type of file")

  with open(file) as f:
    if line in f:
      if line.startswith("v "):
        vertex.append([float(i) for i in line.split()[1:] + [1])
      elif line.startswith('f'):
        faces_ = line.split()[1:]
        faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
  return Object3DFromFile(render, vertex, faces)

def get_object(render):
  ''' Create your objects '''
  ## Create Cube
  obj = Object3D(render)
  obj.translate([0.2, 0.4, 0.2])
  obj.rotate_y(math.pi / 6)
  yield obj
  ## Create AXES
  ## Global Axes
  obj = Axes(render)
  yield obj
  ## Local Axes
  obj = Axes(render)
  obj.translate([0.7, 0.9, 0.7])
  obj.rotate_y(math.pi / 6)
  yield obj
