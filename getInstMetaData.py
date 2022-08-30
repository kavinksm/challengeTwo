import requests
import json


def query(query):
    url = "http://169.254.169.254/latest/"
    response = requests.get(url + query)
    if response.status_code == 200:
        return response.content
    else:
        return ""

def checkKeyContains(key):
    result = (key[-1] == "/")
    return result

def dynamicLoop(currentPath, inputList):
    odict = {}
    for newPath in inputList:
        updatedPath = currentPath + newPath
        response = query(updatedPath)
        if checkKeyContains(newPath):
            tempList = response.splitlines()
            odict[newPath[:-1]] = dynamicLoop(updatedPath, tempList)
        else:
            odict[newPath] = response
    return odict

def getMetadata():
    olist = ["meta-data/"]
    metadata = dynamicLoop("", olist)
    return metadata

if __name__ == '__main__':
    print(json.dumps(getMetadata()))
