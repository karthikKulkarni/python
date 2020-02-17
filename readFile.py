cont = ""
with open("fruits.txt") as data:
    cont = data.read()

with open("fruits.txt", "a+") as data1:
    print(cont)
    data1.write("\n"+cont)
    data1.write("\n"+cont)
