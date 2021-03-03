
import json, shutil, os, time


import create_data as cd
#import line_hitting_aggregate as lha
#import external_dla as dla
    

if __name__ == "__main__":

    #choose your pathname separator (you can find it looking at pathnames in your system)
    #separator = "\\"
    separator = "/"
    
    with open("particles.json") as json_file:
        data = json.load(json_file)
        
    with open("new_colors.json") as json_file:
        colors = json.load(json_file)
        
    with open("parameters.json") as json_file:
        parameters = json.load(json_file)
        
    data.update(colors)
    data.update(parameters)
    
    #create and export data (image, information, parameters)
    cd.export_data(None, data, separator)









