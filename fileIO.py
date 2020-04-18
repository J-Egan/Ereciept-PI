def getREF()
    f = open("ref.txt","r")
    refData = f.readline()
    f.close()
    return refData
