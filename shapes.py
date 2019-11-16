
# the Shape class creates a new blender object
class Shape:

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

    def __init__(self, shape, loc, color):
        #create mutable color material
        # bpy.data.materials.new(name='color')
        self.shape = shape
        self.loc = loc
        self.color = default_colors[self.color]

    def set_color(self):
        bpy.context.active_object.name = 'SIR'
        ob = bpy.data.objects['SIR']

        #create new material
        color_material = bpy.data.materials['color']
        ob.data.materials.append(color_material)
        ob.data.materials['color'].diffuse_color = self.color

    def create_circle(self):
        bpy.ops.mesh.primitive_circle_add(location=self.loc, fill_type='NGON')

    def create_square(self):
        bpy.ops.mesh.primitive_plane_add(location=self.loc)

    default_shapes = {
        "circle": create_circle,
        "square": create_square,
        # "circle": bpy.ops.mesh.primitive_circle_add,
        # "square": bpy.ops.mesh.primitive_plane_add
    }

    def create(self):
        default_shapes[self.shape](self.loc)
        set_color(self)
    

saheed = Shape('circle', (0, 0, 0), 'green')

