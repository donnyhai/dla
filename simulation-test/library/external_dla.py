# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 00:50:43 2020

@author: donnykong
"""
import cmath
import random
from math import log, pi


class External_DLA:

    def __init__(self):
        self.particles = [0]  # particles will be presented as complex numbers

        self.cluster_radius = 0
        self.fractal_dimension_values = [1.5] #start with one neutral value to have equal sizes of particles and fractal_dimension_values

        self.init_surround_circle()
        self.isnotnear_counter = 0

    def run_process(self, iterations):
        for i in range(iterations):
            new_position = self.do_particle_walk(self.get_random_start_position())

            self.particles.append(new_position)
            self.actualize_cluster_radius(new_position)

            self.add_fractal_dimension_value()
            self.actualize_surround_circle()

            print(i)
        print("number of notnear: " + str(self.isnotnear_counter))

    # particle walk with noise reduction

    def do_particle_walk(self, position):
        isnear_counter = 0
        while True:
            if self.is_touching(position):
                return position
            else:
                position = random.choice(self.get_neighbours(position))

            if isnear_counter == 30:
                if not self.isNear(position):
                    position = self.get_random_start_position()
                    self.isnotnear_counter += 1
                isnear_counter = 0
            else:
                isnear_counter += 1

    def actualize_cluster_radius(self, position):
        new_radius = self.get_distance(position, 0)
        if new_radius > self.cluster_radius:
            self.cluster_radius = new_radius

    def get_distance(self, x, y):
        return abs(x - y)

    def add_fractal_dimension_value(self):
        radius = max(self.cluster_radius, 2)
        '''
        as long as the cluster is as small that the radius is equal to one, log(1) is zero and therefore creating a problem in the division below, 
        therefore taking this max here avoids this problem for the short beginning of the process
        '''
        value = log(len(self.particles))/log(radius)
        self.fractal_dimension_values.append(value)

    # start position of the next random walk
    def get_random_start_position(self):
        radius = self.surroundCircle["radius"]
        startpos = cmath.rect(radius, random.random() * 2 * pi)
        return int(startpos.real) + int(startpos.imag) * 1j

    def init_surround_circle(self):
        self.minX, self.maxX = 0, 0
        self.minY, self.maxY = 0, 0

        # how far shall be the surroundCircle be away of the outest particles?
        self.helpSpaceDelta = 2
        # this a circle closely around the cluster
        self.surroundCircle = {
            "middlePoint": self.particles[0], "radius": self.helpSpaceDelta}

    def actualize_surround_circle(self):
        x, y = self.particles[-1].real, self.particles[-1].imag
        self.minX, self.maxX = min(self.minX, x), max(self.maxX, x)
        self.minY, self.maxY = min(self.minY, y), max(self.maxY, y)

        self.surroundCircle["middlePoint"] = (
            (self.minX + self.maxX) / 2) + ((self.minY + self.maxY) / 2) * 1j
        dx, dy = self.maxX - self.minX, self.maxY - self.minY
        self.surroundCircle["radius"] = abs(
            dx + dy * 1j) / 2 + self.helpSpaceDelta

    def isNear(self, pos):
        return abs(pos) < self.surroundCircle["radius"] + 10

    def get_neighbours(self, position):
        return [position + 1, position - 1, position + 1j, position - 1j]

    def is_touching(self, particle):
        for neighbour in self.get_neighbours(particle):
            if neighbour in self.particles:
                return True
        return False
