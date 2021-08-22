import bpy
from math import radians


x_init, y_init, z_init = 10, 10, 20
mass = 500
spacing = 10  
angle_X, angle_Y, angle_Z = 0, 0, 0
blockSize = 2

for x in range(0, x_init, 2):
    for y in range(0, y_init, 2):  
        for z in range(0, z_init,  2):
            # print(f"{x} {y} {z} || {mass}")                  
            bpy.ops.mesh.primitive_cube_add(size=blockSize, location=(x, y, z))
            bpy.context.active_object.rotation_euler[0] += radians(angle_X)
            bpy.context.active_object.rotation_euler[1] += radians(angle_Y)
            bpy.context.active_object.rotation_euler[2] += radians(angle_Z)
            
            # add colision
            bpy.ops.object.modifier_add(type='COLLISION')  
            
            bpy.ops.rigidbody.object_add()
            bpy.context.object.rigid_body.mass = mass
            bpy.context.object.rigid_body.collision_shape = 'BOX'
            bpy.context.object.rigid_body.linear_damping = 0.206667
            bpy.context.object.rigid_body.linear_damping = 0.405079
            bpy.context.object.rigid_body.angular_damping = 0.703175  
            

            
#        angle_X += 15
#        angle_Y += 15
#    blockSize -= .4
#    angle_Z += 15 
#    mass += 25 
        