import random

choices = ['rock','paper','scissors']
while True:
    user = input(f'choose one  from {choices} or type "quit" to exit : ')
    user =user.lower().strip()

    if user =='quit':
        print('Thanks for playing ..')
        break

    if user not in choices:
        print(f'Invalid input , Enter a valid choice between {choices} or type "quit" to exit....')
        continue
    




    computer_choice = random.choice(choices) 

    if user == computer_choice:
        print(f'Its a draw, Both users chose {user}')
    elif user == 'rock' and computer_choice == 'scissors':
        print(f'gbam your {user} crushed the {computer_choice} ... You win ')  
    elif user == 'scissors' and computer_choice == 'paper':
        print(f' your {user} sliced through  the {computer_choice} ... You win ') 
    elif user == 'paper' and computer_choice == 'rock':
        print(f'gbam your {user} covered the {computer_choice} ... You win ')     
    else:
        print(f'You Lose ..... the computer chose {computer_choice} and you chose {user} try again ')


