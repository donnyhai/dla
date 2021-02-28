# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:15:52 2021

@author: Tillmann Tristan Bosch
"""

#systemic imports
import json, shutil, os, time


import create_data as cd
import line_hitting_aggregation as lha
import external_dla as dla
    

if __name__ == "__main__":

    #choose your pathname separator (you can find it looking at pathnames in your system)
    #separator = "\\"
    separator = "/"
    
    #copy parameters.json into the library
    current_dir = os.getcwd()
    up_dir = os.path.dirname(current_dir)
    shutil.copyfile(up_dir + separator + "parameters.json", current_dir + separator + "parameters.json")
    
    #read parameters.json    
    with open("parameters.json") as json_file:
        data = json.load(json_file)
    
    """
    For the two variables ln(radius at time n) and ln(number of particles) we will calculate the paramters (c,alpha) of a simple 
    linear regression ln(radius at time n) nearlyequal ln(c) + alpha*ln(number of particles).
    cut_particles indicates how many particles shall be cut off, that means if the cluster size will be 2000 and we set 
    cut_particles to 1000, the linear regression will only be caluclated for data pairs beginning at 1001 until 2000. 
    """
    cut_particles = data["cut_particles_for_linear_regression"]
    
    #init process
    if data["aggregation"] == "lha":
        aggregation = lha.Line_Hitting_Aggregation(cut_particles)
    elif data["aggregation"] == "dla":
        aggregation = dla.External_DLA(cut_particles)        
    
    #run process and capture running time
    begin_time = time.time()
    aggregation.run_process(data["cluster_size"] - 1)
    
    #prints
    print("running time: " + str(time.time() - begin_time) + " seconds")
    print("Linear regression parameters: " + str(aggregation.linear_regression_parameters))
    if aggregation.linear_regression_parameters["alpha"] is not None:
        print("1/alpha: " + str(round(1 / aggregation.linear_regression_parameters["alpha"], 7)))
    print("Last fractal dimension value: " + str(round(aggregation.fractal_dimension_values[-1],7)))
    #create and export data (image, information, parameters)
    cd.export_data(aggregation, data, separator)









