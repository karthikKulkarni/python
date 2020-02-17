import time
while True:
    with open("fruits.txt") as myFile:
        print(myFile.read())
        time.sleep(3)
