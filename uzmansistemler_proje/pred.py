import pickle

filename = 'finalized_model.sav'
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))

x = loaded_model.predict([[1, 10, 2]])
