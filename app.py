from pygpu import *
import numpy as np

######### code to create a cube mesh ##########
cube_vertices = []
cube_vertices.append(np.matrix('-1;  1;  1;  1'))
cube_vertices.append(np.matrix(' 1;  1;  1;  1'))
cube_vertices.append(np.matrix('-1; -1;  1;  1'))
cube_vertices.append(np.matrix('-1; -1; -1;  1'))
cube_vertices.append(np.matrix('-1;  1; -1;  1'))
cube_vertices.append(np.matrix(' 1;  1; -1;  1'))
cube_vertices.append(np.matrix(' 1; -1;  1;  1'))
cube_vertices.append(np.matrix(' 1; -1; -1;  1'))


cube_position = (0, 0, 0)
cube_rotation  = (0.0, 0.0, 0.0)

cube_mesh = Mesh(cube_vertices, "Cube", cube_position, cube_rotation)

# list of meshes. single mesh for now
meshes = [cube_mesh]


####### code to create a new camera ######
camera_position = (0, 0, 10)  # 10 units along the z axis
camera_target = (0.0, 0.0, 1.0)
my_camera = Camera(camera_position, camera_target)


####### code to create a new device #######
my_device = Device(300, 300)  # screen 100 x 100

###### main rendering loop #####
my_device.set_screen_color((255, 0, 0, 255))  # clear screen



while True:

	my_device.set_screen_color((255, 0, 0, 255))  # clear screen
	# rotate cube slightly during each frame rendered
	for mesh in meshes:
		mesh.rotation = (mesh.rotation[0] + 0.1, mesh.rotation[1] + 0.1, mesh.rotation[2]) # move mesh position slightly
		my_device.render(my_camera, meshes)  # render meshes
		my_device.update_display()  # update display

	
	

