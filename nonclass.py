import bpy
import math

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

def object_from_data(data, name, scene, select=True): 
    """ Create a mesh object and link it to a scene """
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(data['verts'], data['edges'], data['faces'])
    obj = bpy.data.objects.new(name, mesh)
    print(obj)
    
    bpy.context.collection.objects.link(obj)

    scene.objects.active = obj
    obj.select = True
    mesh.validate(verbose=True)
    return obj

def set_color(color):
    bpy.context.active_object.name = 'SIR'
    ob = bpy.data.objects['SIR']

    #create new material
    color_material = bpy.data.materials['color']
    ob.data.materials.append(color_material)
    ob.data.materials['color'].diffuse_color = default_colors[color]


def create_circle(loc):
    bpy.ops.mesh.primitive_circle_add(location=loc, fill_type='NGON')

# def create_semicircle(loc):
#     # create_circle(loc)
#     # ob = bpy.context.active_object
#     verts = []
#     segments = 24
#     for i in range(segments):
#         angle = (math.pi*2) * i / segments
#         verts.append((math.cos(angle), math.sin(angle), 0))

#     data = {
#         'verts': verts,
#         'edges': [],
#         'faces': []
#     }
#     data['edges'] = [(i, i+1) for i in range(segments)]
#     data['edges'].append((segments - 1, 0))

#     scene = bpy.context.scene
#     return object_from_data(data, 'SIR', scene)


def create_square(loc):
    bpy.ops.mesh.primitive_plane_add(location=loc)


default_shapes = {
    "circle": create_circle,
    # "semicircle": create_semicircle,
    "square": create_square,
    # "circle": bpy.ops.mesh.primitive_circle_add,
    # "square": bpy.ops.mesh.primitive_plane_add
}


def create(shape, loc, color):
    bpy.data.materials.new(name='color')
    default_shapes[shape](loc)
    set_color(color)


create('circle', (0, 0, 0), 'green')