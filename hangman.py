import random

fd = open("words", "r")
random = random.randint(0, 100)
sol = ""
solucion = list()
progreso = list()

verprog = list()
lives = 10
wrong = ""

index = 0
for line in fd:
    if index == random:
        sol = line
    index = index + 1

for i in range(len(sol)-1):
    if sol[i] == " ":
        verprog.append(" ")
    else:
        verprog.append("__")
        progreso.append("")
        solucion.append(sol[i])

print(verprog)

while True:
    letter = input("Input a letter please: ")
    indiceesp = 0
    ind = 0
    cor = False
    for char in solucion:
        if sol[indiceesp] == " ":
            indiceesp += 1
        if char == letter:
            verprog[indiceesp] = letter
            progreso[ind] = letter
            cor = True
        indiceesp = indiceesp + 1
        ind = ind+ 1
    if cor:
        print(verprog)
        print("ok you got that one correct")
        if progreso == solucion:
            print("You won the game!!!!!")
            break
    else:
        lives -= 1
        if lives == 0:
            print("GAME OVER you are dead")
            print("The word was", sol)
            break
        else:
            wrong += letter + " "
            print("Incorrect You have", lives, "lives left")
            print("letteres mistaken", wrong)
            print(verprog)
