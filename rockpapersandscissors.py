import random

#w=wins
userw=0
computerw=0

options=["rock","paper","scissors"]

while True:
    user_input=input('type rock/paper/scissor or q to quit: ').lower()
    if user_input=="q":
        break

    if user_input not in options:
        continue

    random_number=random.randint(0,2)
    #rock=0,paper=1,scissors=2
    computer_pick=options[random_number]
    print("computer picked",computer_pick+".")

    if user_input=="rock" and computer_pick =="scissors":
        print("u won")
        userw += 1

    elif user_input == "paper" and computer_pick =="rock":
        print("u won")
        userw += 1


    elif user_input=="scissors" and computer_pick =="paper":
        print("u won")
        userw += 1

    else:
        print("u lost")
        computerw+=1

print("u won",userw,"times")
print("computer won",computerw,"times")

print("goodbye")

