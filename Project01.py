# Snake Water Gun Game
import random

def game_win(user, comp):
    if user == comp:
        return None
    elif (user == 's' and comp == 'w') or (user == 'w' and comp == 'g') or (user == 'g' and comp == 's'):
        return True
    else:
        return False

rand_no = random.randint(1,3)

print("Enter 1 for Snake, 2 for Water and 3 for Gun")

if rand_no == 1:
    comp = 's'
elif rand_no == 2:
    comp = 'w'
else:
    comp = 'g'

user = int(input("Enter your choice: "))

if user == 1:
    user = 's'
elif user == 2:
    user = 'w'
else:
    user = 'g'

result = game_win(user, comp)

print(f"Computer chose {comp}")
print(f"You chose {user}")

if result == None:
    print("The game is a tie!")
elif result:
    print("You win!")
else:
    print("You lose!")