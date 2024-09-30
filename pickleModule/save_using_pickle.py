import pickle

list1=[1,2,3,4,5,6]#object to be saved

filename="data.pickle"#fileName
#saving object using pickle module
fileHandle=open(filename, "wb")
pickle.dump(list1, fileHandle)
fileHandle.close()
# try:
#     with open(filename,"wb") as fileHandle:
#         pickle.dump(list1,fileHandle)
#     print("Object save successfully")
# except:
#     print("Error occured saving object")