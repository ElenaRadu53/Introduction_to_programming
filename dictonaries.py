file = open ("textfile.txt","a")
file.write("cat,dog,rabbit,horse,cat,chicken,cat,rabbit,cow,horse,sheep,dog,chicken,cow,horse,fish,rooster,cow,sheep,fish,pig")
file.close()
file = open("textfile.txt","r")
line = file.readlines()[0]
file.close()

animals = {}
for word in line.split(","):
    print(word)
    animals[word] = animals.get(word,0) + 1
    

