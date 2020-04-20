def getContents(fileName):
    f = open(fileName, "r")
    data = f.readline()
    f.close()
    return data
