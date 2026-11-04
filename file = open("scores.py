file = open("scores.txt", "w")
file.write("Player One: 1200\n")
file.write("Player Two: 950\n")
file.close()

file = open("scores.txt", "a")
file = write("Player Three: 1100")
file.close()

file = open("scores.txt", "r")
contents = file.read()
print(contents)
file.close()

with open("scores.txt", "w") as file:
    file.wite("Player One: 1200/n")