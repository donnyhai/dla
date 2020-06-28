import pickle

def saveObject(obj, filename = "file.obj"): #format filename: "filename.obj"
    pickle.dump(obj, open(filename, "wb"))
    
def getObject(filename = ""): 
    return pickle.load(open(filename, "rb"))


