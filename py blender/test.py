# You need to create a Python program which constructs the similar bones hierarchy with the same animation and saves the file. 
# Basically you need to create 2 objects with armatures. 
# Each armature contains 2 bones. Each bone of the first armature rotates 90 degrees (from 0 to 10 frame). 
# Second armature’s bones don’t have any rotation on them. Instead each bone of this armature has ‘COPY_ROTATION’ constraint which copies rotations of bones of the first armature.
# Note: You can use bpy.ops however that’s not the best practice. 
import bpy
from math import radians
from mathutils import Matrix

def createBones(name, loc):
#    bpy.ops.object.mode_set(mode='OBJECT',  toggle=True)
    
    # parnet bone
    bpy.ops.object.armature_add(location=loc)
    arm = bpy.context.active_object
    arm.name = name
    return arm

# =======================================
# =======================================

def keyFrame(arm, firstFrame, lastFrame):
    # keyframing parnet bone
    arm.keyframe_insert(data_path="rotation_euler", frame=firstFrame)
    arm.rotation_euler[0] = radians(90)
    arm.keyframe_insert(data_path="rotation_euler", frame=lastFrame)

# =======================================
# =======================================

def join(n1, n2):
    obs = [ bpy.data.objects[n2], bpy.data.objects[n1] ]
    
    ctx = bpy.context.copy()
    # one of the objects to join
    ctx['active_object'] = obs[0]
    ctx['selected_editable_objects'] = obs
    bpy.ops.object.join(ctx) 


# =======================================
# =======================================
# =======================================
# =======================================


if __name__ == "__main__" :
    # locP = (0, 0, 0)
    armP = createBones('Armature parent', (0, 0, 0))
    armC = createBones('Armature kid',    (0, 0, 1))

    # making parent    
    bpy.ops.object.parent_set(type='BONE')

    armC.parent = armP

#    if joining animation doesn't work ok
#    join(armC.name, armP.name)

    # keyFraming 
    keyFrame(armP, 1, 10)
    keyFrame(armC, 1, 10)
    
    temp = bpy.data.objects['Armature parent']
    temp.select_set(True)
    context = bpy.context
    
    # obj = bpy.context.object
    # constraint = obj.constraints.new('COPY_ROTATION')

# =======================================
# =======================================
#    C = bpy.context
#    src_obj = bpy.data.objects['Armature parent']
#    new_obj = src_obj.copy()
#    new_obj.data = src_obj.data.copy()
#    C.collection.objects.link(new_obj)
# =======================================
# =======================================
 

# =======================================
# =======================================
    # creating 2nd armature
    arm2P = createBones('2nd armature parent', (1, 0, 0))
    arm2C = createBones('2nd armature kid',    (0, 0, 1))

#    bpy.context.active_object.constraints['Copy Rotation'].target = obj['2nd armature parent']
    
    # making parent     
    bpy.ops.object.parent_set(type='BONE')
    arm2C.parent = arm2P


    temp = bpy.data.objects['2nd armature parent']
    temp.select_set(True)
#    temp.constraint_add(type='COPY_ROTATION')

    print(f"\t\n {temp.name}, {temp} \n")
    
    con = temp.constraints.new(type='COPY_ROTATION')
    con.target = bpy.data.objects['Armature parent']
    print(f"\t\n {temp.name}, {temp} \n")




    temp = bpy.data.objects['2nd armature parent kic']
    temp.select_set(True)
    con = temp.constraints.new(type='COPY_ROTATION')
    con.target = bpy.data.objects['Armature parent']
    print(f"\t\n {temp.name}, {temp} \n")




# =======================================
# =======================================
    # context = bpy.context
    # scene = context.scene
    # arm2 = scene.object.get('Armature parent')

#    temp = bpy.data.objects['Armature parent']
#    temp.select_set(True)
#    
#    print(f"\ttemp: {temp}\n")
#    temp.rotation_euler[1] = radians(90)

#    copy_bone.matrix = temp.matrix.copy()
#    #move bone down
#    copy_bone.translate((0, 0, 1))

#    arm2 = createBones('2nd Armature', (1, 0, 0))
#    arm2 = bpy.context.active_object 
#    print(f"arm2,{arm2}")
#    #    arm2 = temp.copy()
#    arm2 = temp.data.copy()
#    #    arm2.select_set(True)
#    print(f"arm2, after copy {arm2}")
