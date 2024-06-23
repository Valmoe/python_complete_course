"""
>help
start - to start the game
stop - to stop the car
quit - to exit
"""
"""
command = input("> ")
while command == "help":
    print("start - to start the game")
    print("stop - to stop the car")
    print("quit - to exit")
    break
    command_2 = input("> ")
    while command_2 == start:
        print("Game Started...Ready to Go!")
else:
    print("Invalid entry")
"""

command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Game Started!")
    elif command == "stop":
        print("Game Stopped!")
    elif command == "help":
        print("""
        start - to start the game
        stop - to stop the car
        quit - to exit
        """)
    else:
        print("Invalid entry")