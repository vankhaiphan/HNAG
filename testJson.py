import json

# Writing to data.json
def writeJson(data, filename="data.json"):
    with open("data.json", "w") as outfile: 
        outfile.write(json_object) 

def initJson():
    # Data to be written 
    restaurants ={
        "data":[
            {
                "name" : "Gogi", 
                "rating" : 7.6,  
                "image" : "linkanhGogi"
            }
        ]     
    } 

    # Serializing json  
    json_object = json.dumps(restaurants, indent = 4) 
    writeJson(json_object)

# Adding to JSON 
def add_json(data, filename='data.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 

def updateJson():
    with open("data.json") as json_file:
        data = json.load(json_file)
        temp = data["data"]
        dt = {
            "name" : "KFC", 
            "rating" : 8.6,  
            "image" : "linkanhKFC"
        }
        temp.append(dt)
    add_json(data)
if __name__ == "__main__":
    updateJson()
    
  
