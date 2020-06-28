# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 02:49:29 2020

@author: donnykong
"""

    
    #atom walk with noise reduction
    def doAtomWalk(self, position, bogoya = False):
        init_position = position
        isnear_counter = 0
        noise_counter = self.multiple_steps 
        move_direction = (0,0)
        aggregate_cond = True #decides whether neighbouring atom will be added to the cluster (in case of sticking probabilites like in bogoya MR2212061)
        bogoya_power = 2
        while True:
            if self.isTouching(position):
                if bogoya:
                    if random.random() < pow(self.numberOfNeighboursWithParticles(position) / len(self.getNeighbours(position)), bogoya_power):
                        aggregate_cond = True
                    else:
                        aggregate_cond = False
                
                if aggregate_cond:
                    self.addAtom(position)
                    break
                else:
                    position = self.calculateRandomStartPosition()
            
            if isnear_counter == 10:
                if not self.isNear(position):
                    position = self.calculateRandomStartPosition()
                isnear_counter = 0
            isnear_counter += 1
            
            if noise_counter == self.multiple_steps:
                new_position = random.choice(self.getNeighbours(position))
                move_direction = (new_position[0] - position[0], new_position[1] - position[1])
                position = new_position
                noise_counter = 0
            else:
                position = (position[0] + move_direction[0], position[1] + move_direction[1])
                noise_counter += 1
    
    
