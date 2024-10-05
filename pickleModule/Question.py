#WAP to save list object into a file and read that save file and recover as a list without using pickle module
filepath='listdata.txt'
data=[1,2,3,4]

with open(filepath, "w") as fileHandle:
    fileHandle.write(str(data))

with open(filepath,"r") as fileHandle:
    readData=fileHandle.read()
    print(f"data read is {readData}\n its type is {type(readData)} and \nlength is {len(readData)}")
    tempvar=readData[1:len(readData)-1].replace(" ",'')
    print(tempvar)
    listplaceholder=tempvar.split(",")
    recoveredList=listplaceholder
    print(f"Recovered list is{recoveredList}\n its type is {type(recoveredList)}")
