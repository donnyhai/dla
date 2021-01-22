# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 17:38:03 2020

@author: Tillmann Bosch

INFO
Here we provide the code for running the aggregate process and creating images. 
"""
#systemic imports
import json

import create_data as cd
import line_hitting_aggregate as lha
import external_dla as dla
    

if __name__ == "__main__":
    
    with open("parameters.txt") as json_file:
        data = json.load(json_file)
  
    if data["aggregate"] == "lha":
        lha = lha.Line_Hitting_Aggregate()
    elif data["aggregate"] == "dla":
        dla = dla.External_DLA()
    else:
        print("Please enter \"lha\" or \"dla\"")
        
    lha.run_process(data["cluster_size"] - 1)
    cd.export_data(lha, data)