'''
todo: (sessior, paper, rock)
get input from user 1((s/p/R)
get input from user 2(s/p/R)

if user1 input and user2 input is equal print tie
if user1 input is 's' and user2 is 'R' , print user2 wins
if user1 is 's' and user2 is 'P', print user1 win
if user1 is 'r' and user2 is 

🪨 📄 ✂️

'''
import random 

com_choice = ["r","p","s"]
choice_list = {'r': '🪨','p':'📄','s': '✂️'}
user_win = 0
com_win = 0
print('\n')
print('Welcome to Rock Paper Scissor Game.\n')
print('This is going to be the best of 3 rounds. \n')
print('Whoever win 2 rounds first will win the game. \n')
print('Best of luck.\n')

while True:
    user = input('Rock paper scissor(r/p/s)?').lower()
    computer = random.choice(com_choice)

    if user not in com_choice:
        print('Invalid character. Please enter (r/p/s).')
        continue
    
    if user == 'r':
        print(f'You chose: {choice_list['r']}')
    elif user == 'p':
        print(f'You chose: {choice_list['p']}')
    elif user == 's':
        print(f'You chose: {choice_list['s']}')
    
    if computer == 'r':
        print(f'computer chose : {choice_list['r']}')
    elif computer == 'p':
        print(f'computer chose: {choice_list['p']}')
    elif computer == 's':
        print(f'computer chose: {choice_list['s']}')

    if (
        (user == 'r' and computer == 's') or 
        (user == 'p' and computer == 'r') or
        (user == 's' and computer == 'p')):
        print('You win this round 😊')
        user_win += 1
        if user_win == 2 :
            print('Congratulation, You win both rounds🏆')
            user_will = input('Do you like to contiue(y/n)? ')
            if user_will == 'y':
                continue
            else:
                break
    elif user == computer:
        print('Draw')
        continue

        
    else:
        print('computer win this round ')
        com_win += 1
        if com_win == 2:
            print('You lose the game 😔. Computer win both rounds.')
            user_will = input('Do you like to contiue(y/n)? ')
            if user_will == 'y': 
                continue
            else:
                break
