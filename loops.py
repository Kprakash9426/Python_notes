# For Loop
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

dictionary={"Name":'Guna','age':25,'course':'python'}
for key,value in dictionary.items():
    # print(dict)
    print(f"{key}: {value}")