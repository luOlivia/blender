import bpy
import os
import glob

#parse shapes
shape_directory = "/Users/olivialu/Desktop/CUAir/blender/shapes/thicc/"
files = glob.glob(shape_directory + "*.obj")
default_shapes = {}
for f in files:
    head, tail = os.path.split(f)
    shape_name = tail.replace('.obj', '')
    default_shapes[shape_name] = f

#parse letters
letters_directory = "/Users/olivialu/Desktop/CUAir/blender/letters/"
files = glob.glob(letters_directory + "*.obj")
default_letters = {}
for f in files:
    head, tail = os.path.split(f)
    letter_name = tail.replace('.obj', '')
    default_letters[letter_name] = f

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

light_dir = {
    "left": (-1, 0, 1),
    "right": (1, 0, 1),
    "top": (0, 1, 1),
    "bottom": (0, -1, 1),
    "above": (0, 0, 1),
}


def create(path, shape, loc, color):
    '''loads [shape] from a .obj, adds [color] material, and places it at [loc]'''
    #loads specified shape from obj file
    bpy.ops.import_scene.obj(filepath=path)

    #sets shape ref + name
    bpy.context.selected_objects[0].name = shape
    ob = bpy.data.objects[shape]
    ob.location = loc

    #adds color material + sets specified color
    mat = bpy.data.materials.new(name=color)
    ob.data.materials.append(mat)
    # ob.active_material.diffuse_color = default_colors[color]
    ob.active_material.node_tree.nodes[1].inputs[
        'Base Color'].default_value = default_colors[color]


def add_lamp(dir, shape_name):
    '''creates a lamp at loc relative to curr object location'''
    ob = bpy.data.objects[shape_name]
    curr_loc = tuple(map(sum, zip(ob.location, light_dir[dir])))
    bpy.ops.object.light_add(type='POINT', location=curr_loc)


s = 'semicircle'
l = 'A'
create(default_shapes[s], s, (0, 0, 0), 'green')
create(default_letters[l], l, (0, 0, 0.07), 'red')
add_lamp('left', s)

#toggles view to camera
area = next(area for area in bpy.context.screen.areas
            if area.type == 'VIEW_3D')
area.spaces[0].region_3d.view_perspective = 'CAMERA'

#renders + saves image of camera
bpy.context.scene.render.filepath = '/Users/olivialu/Desktop/CUAir/blender/image.jpg'
bpy.ops.render.render(write_still=1)
