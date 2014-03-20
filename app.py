from pygpu import *
import numpy as np
import pygame


######### code to create a cube mesh ##########
cube_vertices = []
cube_vertices.append(np.matrix('-1;  1;  1;  1'))  # vertex 0
cube_vertices.append(np.matrix(' 1;  1;  1;  1'))  # vertex 1
cube_vertices.append(np.matrix('-1; -1;  1;  1'))  # vertex 2
cube_vertices.append(np.matrix(' 1; -1;  1;  1'))  # vertex 3
cube_vertices.append(np.matrix('-1;  1; -1;  1'))  # vertex 4
cube_vertices.append(np.matrix(' 1;  1; -1;  1'))  # vertex 5
cube_vertices.append(np.matrix(' 1; -1; -1;  1'))  # vertex 6
cube_vertices.append(np.matrix('-1; -1; -1;  1'))  # vertex 7

cube_faces = []
cube_faces.append(Face(0, 1, 2))  # face 0
cube_faces.append(Face(1, 2, 3))  # face 1
cube_faces.append(Face(1, 3, 6))  # face 2
cube_faces.append(Face(1, 5, 6))  # face 3
cube_faces.append(Face(0, 1, 4))  # face 4
cube_faces.append(Face(1, 4, 5))  # face 5

cube_faces.append(Face(2, 3, 7))  # face 6
cube_faces.append(Face(3, 6, 7))  # face 7
cube_faces.append(Face(0, 2, 7))  # face 8
cube_faces.append(Face(0, 4, 7))  # face 9
cube_faces.append(Face(4, 5, 6))  # face 10
cube_faces.append(Face(4, 6, 7))  # face 11


cube_position = (0, 0, 0)
cube_rotation  = (0.0, 0.0, 0.0)

cube_mesh = Mesh(cube_vertices, cube_faces, "Cube", cube_position, cube_rotation)

# list of meshes. single mesh for now
meshes = [cube_mesh]


######### code to create a cube mesh with triangles ##############


####### code to create a new camera ######
camera_position = (0, 0, 10)  # 10 units along the z axis
camera_target = (0.0, 0.0, 1.0)
my_camera = Camera(camera_position, camera_target)


####### code to create a new device #######
my_device = Device(300, 300)  # screen 100 x 100

###### main rendering loop #####
my_device.set_screen_color((255, 0, 0, 255))  # clear screen

done = False

while not done:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			break

	if done:
		break

	my_device.set_screen_color((255, 0, 0, 255))  # clear screen
	# rotate cube slightly during each frame rendered
	for mesh in meshes:
		mesh.rotation = (mesh.rotation[0] + 0.1, mesh.rotation[1] + 0.1, mesh.rotation[2]) # move mesh position slightly
		my_device.render(my_camera, meshes)  # render meshes
		my_device.update_display()  # update display

	
	

