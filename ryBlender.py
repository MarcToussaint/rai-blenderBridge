import sys
sys.path.append('/home/mtoussai/git/build-rai/')

import bpy
import matplotlib.image as mpimg

from ryOrthey import *

class RyBlenderBridge():
    camera = []
    light = []
    camFocus = []
    camPos = []

    def __init__(self):
        #delete default configuration
        #cube = bpy.context.scene.objects['Cube']
        #bpy.context.collection.objects.unlink(cube)

        #completely delete all existing objects:
        for obj in bpy.context.scene.objects:
            bpy.context.collection.objects.unlink(obj)

        #create camera object
        cam = bpy.data.cameras.new("Camera")
        self.camera = bpy.data.objects.new("Camera", cam)
        bpy.context.collection.objects.link(self.camera)
        bpy.context.scene.camera = self.camera
        bpy.context.view_layer.objects.active = self.camera

        #reposition camera
        self.camFocus = Vector([0,0,1])
        self.camPos = Vector([5,10,5])
        self.repositionCamera()

        #create light object
        light = addLightSourcePoint([5,5,5])

    def setConfiguration(self, C):
        for f in C.frames():
            addMeshForFrame(f)

    def repositionCamera(self):
        self.camera.location = self.camPos
        look = self.camPos - self.camFocus
        rot_quat = look.to_track_quat('Z', 'Y')
        self.camera.rotation_mode = 'XYZ'
        self.camera.rotation_euler = rot_quat.to_euler()

    def setCameraPos(self, pos):
        self.camPos = Vector(pos)
        self.repositionCamera()
        
    def render(self, renderer='BLENDER_WORKBENCH'): #'CYCLES' 'EEVEE'
        bpy.context.scene.render.filepath = 'image'
        bpy.context.scene.render.resolution_x = 600 #perhaps set resolution in code
        bpy.context.scene.render.resolution_y = 400
        bpy.context.scene.render.engine = renderer
        bpy.ops.render.render(write_still=True)
        
        img = mpimg.imread('image.png')
        return img

def addMesh(name, pos, quat, pts, tris):
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(mesh.name, mesh)
    obj.location = pos
    obj.rotation_mode = 'QUATERNION'
    obj.rotation_quaternion = quat
    bpy.context.collection.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    
    mesh.from_pydata(pts, [], tris)

def addMeshForFrame(f):
    name = f.getName()
    pos = f.getPosition()
    quat = f.getQuaternion()
    pts = f.getMeshPoints()
    tris = f.getMeshTriangles()
    
    if tris.size>1:
        addMesh(name, pos, quat, pts.tolist(), tris.tolist())

    
