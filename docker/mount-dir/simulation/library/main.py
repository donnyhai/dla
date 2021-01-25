# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:15:52 2021

@author: Tillmann Tristan Bosch
"""

#systemic imports
import json, shutil, os, time


import create_data as cd
import line_hitting_aggregate as lha
import external_dla as dla
    

if __name__ == "__main__":
    
    #copy parameters.json into the library
    current_dir = os.getcwd()
    up_dir = os.path.dirname(current_dir)
    shutil.copyfile(up_dir + "\\parameters.json", current_dir + "\\parameters.json")
    
    #read parameters.json    
    with open("parameters.json") as json_file:
        data = json.load(json_file)
    
    #init process
    if data["aggregate"] == "lha":
        aggregate = lha.Line_Hitting_Aggregate()
    elif data["aggregate"] == "dla":
        aggregate = dla.External_DLA()        
    
    #run process and capture running time
    begin_time = time.time()
    aggregate.run_process(data["cluster_size"] - 1)
    print("running time: " + str(time.time() - begin_time) + " seconds")
    
    #create and export data (image, information, parameters)
    cd.export_data(aggregate, data)









