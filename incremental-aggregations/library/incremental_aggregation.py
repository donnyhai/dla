# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 15:06:59 2021

@author: donnykong

This class describes the general setup for a simulation of an incremental aggregation. 
"""
import random
import geometry as geom

class Incremental_Aggregation:
	def __init__(self):
		self.particles = [0]  # particles will be presented as complex numbers
		self.boundary_set = self.get_neighbours(0)
		self.cluster_radius = 0 #radius of the current cluster = maximum of all distances from 0 to the cluster points
	
	
	def run_process(self, iterations):
		for k in range(iterations):
			new_particle = self.get_next_particle()
			
			self.particles.append(new_particle)
			self.actualize_cluster_radius()
			self.actualize_boundary_set()
			
			print(k)
		
	
	def get_next_particle(self):
		"""
		to give an example just choose randomly of the current boundary set
		"""
		return random.choice(self.boundary_set) 
	
	
	def actualize_cluster_radius(self):
		self.cluster_radius = max(self.cluster_radius, self.get_distance(self.particles[-1], 0))
		
		
	def actualize_boundary_set(self):
		""" 
		suppose that position is part of the current boundary set and a particle
		comes to sit there now. therefore delete position of the current boundary set and add its empty neighbours to it
		"""
		position = self.particles[-1]
		self.boundary_set.remove(position)
		for neighbour in self.get_neighbours(position):
			if neighbour not in self.boundary_set and neighbour not in self.particles:
				self.boundary_set.append(neighbour)
				
		
	def get_distance(self, x, y = 0):
		return abs(x - y)


	def get_neighbours(self, position):
		return [position + 1, position - 1, position + 1j, position - 1j]
	
	
	def get_square(self, pos):
		
		"""
		return is the square polygon which contains pos as defined in the paper, with segments starting 
		from right top vertex of the square moving clockwise
		"""
		pos = round(pos.real, 0) + round(pos.imag, 0) * 1j
		
		return geom.Polygon([pos + 1/2 * (1+1j), pos + 1/2 * (1-1j), pos + 1/2 * (-1-1j), pos + 1/2 * (-1+1j)])
	
	
	
	
	
	
	
	