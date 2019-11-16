from enum import Enum
import bpy  #only works when run inside Blender's Python console

# class Shape(Enum):
# 	CIRCLE = 0
# 	SEMICIRCLE = 1
# 	QUARTER_CIRCLE = 2
# 	TRIANGLE = 3
# 	SQUARE = 4
# 	RECTANGLE = 5
# 	TRAPEZOID = 6
# 	PENTAGON = 7
# 	HEXAGON = 8
# 	HEPTAGON = 9
# 	OCTAGON = 10
# 	STAR = 11
# 	CROSS = 12
# 	CUBE = bpy.ops.mesh.primitive_cube_add(location=(0,0,0))

# class Color(Enum):
# 	WHITE = 0
# 	BLACK = 1
# 	GRAY = 2
# 	RED = 3
# 	BLUE = 4
# 	GREEN = 5
# 	YELLOW = 6
# 	PURPLE = 7
# 	BROWN = 8
# 	ORANGE = 9

default_colors = {
    "white": (255, 255, 255, 1),
    "black": (0, 0, 0, 1),
    "gray": (135, 135, 135, 1),
    "red": (255, 0, 0, 1),
    "blue": (0, 55, 255, 1),
    "green": (0, 55, 255, 1),
    "yellow": (0, 55, 255, 1),
    "purple": (0, 55, 255, 1),
    "brown": (54, 28, 24, 1),
    "orange": (255, 145, 0, 1)
}

default_shapes = {
    "circle": bpy.ops.mesh.primitive_circle_add,
    "square": bpy.ops.mesh.primitive_plane_add
}

def set_color(fun, loc, color):

    #name object to SIR
    bpy.context.active_object.name = 'SIR'
    ob = bpy.data.objects['SIR']

    #create new material
    color_material = bpy.data.materials['color']
    ob.data.materials.append(color_material)
    ob.data.materials['color'].diffuse_color = color


def create(shape, loc, color):
    #create mutable color material
    bpy.data.materials.new(name='color')

    #create shape
    fun = default_shapes[shape]
    if shape == 'circle': #need to be filled in first
        fun(location=loc, fill_type='NGON')
    else:
        fun(location=loc)
    set_color(fun, loc, default_colors[color])


create('circle', (0, 0, 0), 'green')
#take obj in scene named target and change color








