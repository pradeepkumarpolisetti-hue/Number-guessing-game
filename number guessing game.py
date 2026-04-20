import random
print("Let's see your guessing ability.")
print("Choose a number between 1-50")
print("You only have 6 tries")
a = random.randint(15, 26)
for i in range(1, 7):
    b = int(input(f"Trial {i}: "))
    if b == a:
        print("Correct! Congratulations!")
        print("Your score:", (7 - i), "/6")
        break
    elif b <= 10:
        print("Too far. Go higher.")
    elif 10 < b <= 15:
        print("Getting nearer. Go higher.")
    elif 15 < b < a:
        print("Very close! Slightly higher.")
    elif a < b < 26:
        print("Very close! Slightly lower.")
    elif 25 < b < 31:
        print("Getting nearer. Go lower.")
    elif 30 < b <= 50:
        print("Too far. Go lower.")
    else:
        print("Out of range!")

    print(6 - i, "tries left")

else:
    print("Game Over! The number was", a)
