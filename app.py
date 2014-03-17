from pygpu import *
from numpy import *

# main application program

# code to create a cube mesh
cube_vertices = []
cube_vertices.append(matrix('-1  1  1  1'))
cube_vertices.append(matrix(' 1  1  1  1'))
cube_vertices.append(matrix('-1 -1  1  1'))
cube_vertices.append(matrix('-1 -1 -1  1'))
cube_vertices.append(matrix('-1  1 -1  1'))
cube_vertices.append(matrix(' 1  1 -1  1'))
cube_vertices.append(matrix(' 1 -1  1  1'))
cube_vertices.append(matrix(' 1 -1 -1  1'))

cube_position = matrix('0 0 0')
cube_rotation  = matrix('0 0 0')

cube_mesh = Mesh(cube_vertices, "Cube", cube_position, cube_rotation)

print cube_mesh.vertices


test_display = Device(640, 480)
test_display.set_screen_color(0, 0, 255, 0)
test_display.update_display()
test_display.set_screen_color(255, 0, 0, 0)
test_display.update_display()