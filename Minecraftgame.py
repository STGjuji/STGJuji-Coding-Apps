from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Voxel(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
		parent = scene,
		position = position,
		model = 'cube',
		origin_y = 0.5,
		texture = 'white_cube',
		color = color.white,
		hghlight_color = color.lime)


		def input(self,key):
			if self.hovered:
				if key == 'left mouse down':
					voxel = Voxel(position = self.position + mouse.normal)

app = Ursina()

for z in range(10):
	for x in range(10):
		voxel = Voxel((x,0,z))

player = FirstPersonController()

app.run()