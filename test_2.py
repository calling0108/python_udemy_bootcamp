level = "hard"

if level == "hard":
    print("You have 5 attempts remaining to guess the number.")
    life = 5

def lose_life():
    global life
    life -= 1

lose_life()

print(life)