import random
world_list=["a","e","i","o","u","A","E","I","O","U"]
user_choice=input("enter the vowel: ")
comp_choice=random.choice(world_list)
if user_choice==comp_choice:
    print("match tie")

else:
    print("unmatched")
    print("random vowel is: ") 
    print(random.choice(world_list))
    