#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import math
import json

import bpy
import bpy_extras
import mathutils

class objexport(object):
	def __init__(self, obj):
		self.obj = obj
		
	def print(self):
		'''
		for polygon in self.obj.data.polygons:  
			verts_in_face = polygon.vertices[:]
			print()  
			print("face index", polygon.index)  
			print("normal", polygon.normal)  
			for vert in verts_in_face:  
				print("vert", vert, " vert co", self.obj.data.vertices[vert].co) 
		'''
		
		filepath = bpy.data.filepath
		directory = os.path.dirname(filepath)
		outfilename = os.path.join(directory, "test.json")
		outfile = open(outfilename, "wt")
		
		for face in self.obj.data.polygons:
			
			#outfile.write('FACE\n')
			
			outfile.write('[')
			
			for vert, loop in zip(face.vertices, face.loop_indices):
				
				#print('{:3d} {:3d} '.format(loop, vert), end="")
				#outfile.write('{: 8d} '.format(loop))
				
				#outfile.write('{: 8d},'.format(vert))
				
				
				outfile.write('[')
				
				for item in self.obj.data.vertices[vert].co: 
					outfile.write('{: 8.3f},'.format(item))
				
				outfile.write('\t')
				
				for item in self.obj.data.vertices[vert].normal: 
					outfile.write('{: 8.3f},'.format(item))
				
				outfile.write('\t')
				
				arrUV = (0.0, 0.0)
				if self.obj.data.uv_layers.active is not None :
					arrUV = self.obj.data.uv_layers.active.data[loop].uv   
				
				for item in arrUV:
					outfile.write('{: 8.3f},'.format(item))
					
				outfile.write('],')
				
				outfile.write('\n')
				
				
			outfile.write('],')
			
			outfile.write('\n')
				
		outfile.close()
				

for obj in bpy.data.objects:
	if obj.type == 'MESH':
		bpy.context.scene.objects.active = obj
		objItem = objexport(obj)
		objItem.print()
