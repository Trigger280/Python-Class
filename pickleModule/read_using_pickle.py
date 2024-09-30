import pickle

with open("data.pickle","rb") as file:
    loaded_data=pickle.load(file)
print("The data is", loaded_data)