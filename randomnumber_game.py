import random


user_choice=int(input("enter any number between 1-5: "))
comp_choice= random.randint(1,5)

if user_choice>5:
    print("You cannot choose this value!")
else:
    if comp_choice>user_choice:
        print("You Lose!")
        print("Computer chose!",comp_choice)
        print("you chose!",user_choice)
    elif comp_choice<user_choice:
        print("You Win!")
        print("Computer chose!",comp_choice)
        print("you chose!",user_choice)
    else:
        print("Match Tied!")
        print("Computer chose!",comp_choice)
        print("you chose!",user_choice)

    

