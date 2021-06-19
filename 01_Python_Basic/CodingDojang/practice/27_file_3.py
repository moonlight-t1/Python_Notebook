import pickle

name = "james"
age = 17
address = "서울시 서초구 반포동"
scores = {"korean": 90, "english": 95, "mathematics": 85, "science": 82}

with open("james.info", "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)


with open("james.info", "rb") as file:
    na = pickle.load(file)
    ag = pickle.load(file)
    ad = pickle.load(file)
    sc = pickle.load(file)

print(na)
print(ag)
print(ad)
print(sc)

