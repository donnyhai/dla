# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:19:52 2021

@author: Tillmann Tristan Bosch

Here basic geometrical features are provided which are needed in the simulation of the line hitting aggregation. 
"""


from math import sin, cos, pi, sqrt
from cmath import phase, exp


class Segment:
	
	def __init__(self, A = 0, B = 1):
		self.A = A
		self.B = B

	def length(self):
		return abs(self.A - self.B)
		
		
class Polygon:
	
	def __init__(self, vertices = [0, 1, 1j, 1+1j]):
		self.vertices = vertices
		self.segments = self.init_segments()
		
	def init_segments(self):
		segments = []
		l = len(self.vertices)
		for k in range(l):
			segments.append(Segment(self.vertices[k], self.vertices[(k+1) % l]))
		return segments
		
	def contains_point(self, point):
		pass
		

class Line:
	
	def __init__(self, alpha = 0, p = 0):
		
		"""
		We use the following representation of points on the line: 
		
		For an angle alpha in [0,pi) we define e_alpha = (cos(alpha), sin(alpha)) and f_alpha = (-sin(alpha), cos(alpha)).
		e_alpha and f_alpha form a base of the real plane and evolve by turning the standard base (1,0), (0,1) by alpha counterclockwise.
		For any x in the real plane we can therefore write x = <x, e_alpha> * e_alpha + <x, f_alpha> * f_alpha where <.,.> is the standard 
		scalar product. The parameters <x, e_alpha> and <x, f_alpha> are unique since e_alpha and f_alpha is a base of the plane. 
		
		The line with parameters (alpha, p) shall consist of all elements x where <x, e_alpha> = p. By the above, the identification of a line
		with such a pair of parameters is unique and defines a bijection: lines <-> [0,pi) x RR. 
		"""        
		
		self.alpha = alpha
		self.p = p
		
	
	def calculate_parameters(self, segment):
		"""
		Set line parameters to the parameters of a line which contains segment
		"""
		A, B = segment.A, segment.B
		self.alpha = (phase(A - B) - pi/2) % pi
		self.p = A.real * cos(self.alpha) + A.imag * sin(self.alpha) #<A,e_alpha>
		
	
	def intersects_with_segment(self, segment):
		
		"""
		With the representation of points as described above we can determine easily whether a line intersects a segment AB or not.
		A line g intersects AB iff A lies "over" g and B "under" g or the other way around. This can be equivalently stated by:
			
		g interesects segment AB iff (<A,e_alpha> >= p and <B,e_alpha> <= p) or (<A,e_alpha> <= p and <B,e_alpha> >= p)
		"""
		
		cos_alpha = cos(self.alpha)
		sin_alpha = sin(self.alpha)
		A_alpha = segment.A.real * cos_alpha + segment.A.imag * sin_alpha # <A,e_alpha>
		B_alpha = segment.B.real * cos_alpha + segment.B.imag * sin_alpha # <B,e_alpha>
		
		if (A_alpha >= self.p and B_alpha <= self.p) or (A_alpha <= self.p and B_alpha >= self.p):
			return True
		return False

	
	def intersects_with_polygon(self, polygon):
		for segment in polygon.segments:
			if self.intersects_with_segment(segment):
				return True
		return False

	

class Circle:

	def __init__(self, center = 0, radius = 1):
		self.center = center
		self.radius = radius
		
	def intersects_with_polygon(self, polygon):
		for segment in polygon.segments:
			if self.intersects_with_segment(segment):
				return True
		return False
		
	def intersects_with_segment(self, segment):
		line = Line()
		line.calculate_parameters(segment)

		#circle is touching the line, which contains the segment
		p_center = cos(line.alpha) * self.center.real + sin(line.alpha) * self.center.imag
		condition_1 = line.p - self.radius <= p_center <= line.p + self.radius

		#circle contains one of the ends of the segments (segment.A or segment.B)
		condition_2 = abs(self.center - segment.A) <= self.radius or abs(self.center - segment.B) <= self.radius
		
		#circle is not too far from the segment, not being able to contain any point of it
		max_dist = sqrt(pow(segment.length(), 2) + pow(self.radius, 2))
		condition_3 = abs(self.center - segment.A) <= max_dist and abs(self.center - segment.B) <= max_dist

		return condition_1 and (condition_2 or condition_3)
		
	
	def get_intersection_segment(self, line):
		"""
		Circle may contain part of line, return is a segment objekt. If the circle and line are disjoint, return is False.
		"""
		p_center = cos(line.alpha) * self.center.real + sin(line.alpha) * self.center.imag
		p_delta = line.p - p_center
		
		#check whether circle and line interesect
		if abs(p_delta) > self.radius:
			return False 
			
		else:
			center_proj = self.center + p_delta * exp(line.alpha * 1j)
			x = sqrt(pow(self.radius, 2) - pow(p_delta, 2))
			
			AB = [center_proj + x * exp((line.alpha + pi/2) * 1j ), center_proj - x * exp((line.alpha + pi/2) * 1j)]
			A = round(AB[0].real, 7) + 1j * round(AB[0].imag, 7)
			B = round(AB[1].real, 7) + 1j * round(AB[1].imag, 7)
			
			return Segment(A, B)
			
			
			
		
		
		
		
		
		