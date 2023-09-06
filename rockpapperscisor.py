import random
item_list=["Rock","Paper","Scissor"]
user_choice=input("Your choice=Rock,Paper,Scissor= ")
comp_choice=random.choice(item_list)
if user_choice==comp_choice:
    print("match tie")
elif user_choice=="Rock" or "rock":
    if comp_choice=="Paper":
        print("Paper cover the Rock. Computer wins")
    else:
        print("Rock smashes Scissor, You won")
elif user_choice=="Paper" or "paper":
    if comp_choice=="Scissor":
        print("Scissor cuts Paper, Computer won")
    else:
        print("Paper cover the Rock,You won")
elif user_choice=="Scissor" or "scissor":
    if comp_choice=="Rock":
        print("Rock smashes Scissor, Computer won")
    else:
        print("Scissor cuts Paper ,You won")
        