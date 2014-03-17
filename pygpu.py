import numpy
import pygame

# Class to describe a Camera object
class Camera(object):

	def __init__(self, position, target):
		self.position = position  # camera position in the 3d world
		self.target = target 	  # where the camera is looking (location)

	# set functions
	def set_position(self, position):
		self.position = position

	def set_target(self, target):
		self.target = target

	# get functions
	def get_position(self):
		return self.position

	def get_target(self):
		return self.target

# Class to describe a Mesh object
class Mesh(object):

	def __init__(self, vertices, name, position, rotation):
		self.name = name   		  # mesh name
		self.vertices = vertices  # collection of (x,y,z) vertices to define mesh
		self.position = position  # its position in the 3d world
		self.rotation = rotation  # rotation state of the mesh
	
	# set functions	
	def set_vertices(self, vertices):
		self.vertices = vertices

	def set_name(self, name):
		self.name = name

	def set_position(self, position):
		self.position = position

	def set_rotation(self, rotation):
		self.rotation = rotation

	# get functions
	def get_vertices(self):
		return self.vertices

	def get_name(self):
		return self.name

	def get_position(self):
		return self.position

	def get_rotation(self):
		return self.rotation


# Class to define the rendering device
class Device(object):

	# constructor initializes frame buffer
	def __init__(self, pixel_width, pixel_height):
		self.pixel_width = pixel_width
		self.pixel_height = pixel_height

		pygame.init()  # init pygame
		self.display = pygame.display.set_mode((self.pixel_width, self.pixel_height), 0, 32)  # create display


	# set screen to one solid color
	def set_screen_color(self, color):
		for x in range(self.pixel_width):
			for y in range(self.pixel_height):
				self.display.set_at((x,y), color)

	# set pixel
	def put_pixel(self, x, y, color):
		self.display.set_at((x,y), color)

	# update output
	def update_display(self):
		pygame.display.update()



