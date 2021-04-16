from mathutils import *
import bpy

def addLightSourceSun(location):
    light_data = bpy.data.lights.new(name="light_2.80", type='SUN')
    light_data.energy = 5
    light_data.angle = 5/180.0
    light_data.specular_factor = 0.8
    light_object = bpy.data.objects.new(name="light_2.80",
      object_data=light_data)
    bpy.context.collection.objects.link(light_object)
    light_object.location = location

def addLightSourcePoint(location):
    light_data = bpy.data.lights.new(name="light_2.80", type='POINT')
    light_data.energy = 6000
    light_data.specular_factor = 0.4
    light_data.use_contact_shadow = True
    light_object = bpy.data.objects.new(name="light_2.80",
      object_data=light_data)
    bpy.context.collection.objects.link(light_object)
    light_object.location = location
    return light_object

def addLightSourceArea(location, size=13, energy=400):
    name = "light_source_area_"+str(location)
    light_2 = bpy.data.lights.new(name=name, type='AREA')
    light_2.energy = energy
    light_2.size = size
    light_2_object = bpy.data.objects.new(name=name, object_data=light_2)
    bpy.context.collection.objects.link(light_2_object)
    light_2_object.location = location

def addCamera(loc, foc):
    cam = bpy.data.cameras.new("Camera")
    cam_ob = bpy.data.objects.new("Camera", cam)
    bpy.context.collection.objects.link(cam_ob)
    cam_ob.location = loc
    bpy.context.scene.camera = cam_ob
    bpy.context.view_layer.objects.active = cam_ob
    look = loc - foc
    distance = look.length
    
    rot_quat = look.to_track_quat('Z', 'Y')
    
    cam_ob.rotation_mode = 'XYZ'
    cam_ob.rotation_euler = rot_quat.to_euler()
    return cam_ob
