import bpy

bpy.ops.mesh.primitive_cube_add()
so = bpy.context.active_object
so.location[0] = 4

mod_subsurf = so.modifiers.new("my modifier", 'SUBSURF')
mod_subsurf.levels = 3

bpy.ops.object.shade_smooth()

#long
#mesh = so.data
#for face in mesh.polygons:
#    face.use_smooth = True

mod_displace = so.modifiers.new("my displacement", 'DISPLACE')

#change texture
new_tex = bpy.data.textures.new("my texture", 'DISTORTED_NOISE')

#change texture setting
new_tex.noise_scale = 2.0