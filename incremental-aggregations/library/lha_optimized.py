# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:18:52 2021

@author: Tillmann Tristan Bosch

This is a simulation of the line hitting aggregation. In the paper it is displayed why this implementation comes very close to the process original mathematical definition. 
"""

#mathematical imports
import random
from math import pi, sqrt #here log is the natural logarithm with base e
import geometry as geom
import incremental_aggregation as ia


class Line_Hitting_Aggregation_Optimized(ia.Incremental_Aggregation):
	def __init__(self):
		super().__init__()
		self.layers = {0: [0]}
		
		self.missed_counter = 0
		
		
	def run_process(self, iterations):
	
		#create layers
		self.layers[-1] = []
		for k in range(1, int(3 * sqrt(iterations))):
			self.layers[k] = []
			
		#run aggregation
		for k in range(iterations):
			
			line_hits_cluster = False
			
			while not line_hits_cluster:
				random_line = self.get_random_line()
				next_particle = self.get_next_particle(random_line)
				
				if next_particle == False: #line missed cluster
					self.missed_counter += 1
					
				else:
					line_hits_cluster = True
					
					self.particles.append(next_particle)
					
					self.actualize_boundary_set()
					self.actualize_cluster_radius()
					#self.actualize_layers()
					
					print(k)
					
		print("DONE")
		print("number of misses: " + str(self.missed_counter))
	
		
	def get_random_line(self):
		
		"""
		We choose uniform random parameters (alpha, p) in [0, pi) x [0, 20/19 * self.cluster_radius) 
		which is equivalent to choosing a B-isotropic line where B is a circle with radius 20/19 * self.cluster_radius with center 0
		and by contstruction therefore certainly contains the current cluster. 
		random.random() chooses uniformly in [0, 1.0)
		return is the parameters pair (alpha, p)
		"""
	 
		alpha = pi * random.random()
		radius = self.cluster_radius + 2 #radius of a circle which certainly surrounds the current cluster
		p = 2 * radius * random.random() - radius
		
		return geom.Line(alpha, p)
	

	def get_next_particle(self, line):
		
		"""
		Choose next particle according to the random line hitting distribution as described in the paper.
		"""
		C = geom.Circle(0, self.cluster_radius + 2)
		segment = C.get_intersection_segment(line) #segment object
		
		if segment == False:
			print("line missed cluster: no segment")
			return False
		elif segment.A == segment.B:
			print("line missed cluster: one point segment")
			return False
		
		AB = [segment.A, segment.B]
		random.shuffle(AB)
		A = AB[0]
		B = AB[1]
		
		"""
		c is a "walking" circle from A to B. When it intersects with a cluser particle, the square which contains the center 
		of the circle gets added to the cluster, if it is element of boundary_set.
		c walks with steps of size stepsize
		"""
		c = geom.Circle(A, 0.99)
		stepsize = c.radius * 0.99
		dir = (B - A) / abs(B - A) #abs = 1 
		
		while True:
			c_dist = int(abs(c.center))

			"""
			#working with particle cluster layers
			
			#for k in [current_dist, current_dist + 1]:
			for k in [c_dist - 1, c_dist, c_dist + 1]:
				for point in self.layers[k]:
					if c.intersects_with_polygon(self.get_square(point)):
						pos = c.center
						pos = round(pos.real, 0) + round(pos.imag, 0) * 1j
						
						if pos not in self.boundary_set:
							for neigh in self.get_neighbours(pos):
								if neigh in self.boundary_set:
									return neigh
						
							print("line hit diagonal")
							return False
								
						return pos
			"""
			for point in self.boundary_set:
				if c.intersects_with_polygon(self.get_square(point)):
					return point
				
			
			c.center += stepsize * dir
			
			if self.get_distance(c.center, 0) > 2 * C.radius:
				print("line missed cluster: walked by")
				return False
						
		
		
		
	def actualize_layers(self):
		new_particle = self.particles[-1]
		k = int(round(self.get_distance(new_particle, 0), 0))
		self.layers[k].append(new_particle)
		
		
		
		
