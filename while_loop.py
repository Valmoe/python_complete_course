"""
i = 1
while i <=5:
    print(i)
    i = i + 1
print("Done")

"""
"""
i = 1
while i <=5:
    print("Fuck "*i)
    i = i + 1
print("Done")
"""

"""
Guessing game
"""
secret_number = 9
guess_count = 0
guess_times = 3
while guess_count < guess_times:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
    else:
        print("You lost!")
