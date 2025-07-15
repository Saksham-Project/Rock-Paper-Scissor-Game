'''
Rock,Paper,Scissors Game

'''
import random

lis = ['r','p','s']



while True:
    user_choice = input('Rock Paper Scissor (r/p/s):')
    com_choice = random.choice(lis)
    if user_choice == 'r' and com_choice == 'p':
            print("you choose 🪨")
            print('computer choose 📄')
            print('You lose 😔')
            continue
    elif user_choice == 'r' and com_choice == 's':
            print("you choose 🪨")
            print('computer choose ✂️')
            print('you win 😁')
            con = input('Continue? (y/n):').lower()
            if con == 'y':
                    continue
            else:
                break
    elif user_choice == 'r' and com_choice == 'r':
            print("you choose 🪨")
            print('computer choose 🪨')
            print('Draw 🤝')
            con = input('Continue? (y/n):').lower()
            if con == 'y':
                    continue
            else:
                break
    elif user_choice == 'p' and com_choice == 'r':
            print("you choose 📄")
            print('computer choose 🪨')
            print('you win 😁')
            con = input('Continue? (y/n):').lower()
            if con == 'y':
                    continue
            else:
                break
    elif user_choice == 'p' and com_choice == 'p':
            print("you choose 📄")
            print('computer choose 📄')
            print('Draw 🤝')
            con = input('Continue? (y/n):').lower()
            if con == 'y':
                    continue
            else:
                break
    elif user_choice == 'p' and com_choice == 's':
            print("you choose 📄")
            print('computer choose ✂️')
            print('You lose 😔')
            continue
    elif user_choice == 's' and com_choice == 's':
            print("you choose ✂️")
            print('computer choose ✂️')
            print('Draw 🤝')
            con = input('Continue? (y/n):').lower()
            if con == 'y':
                    continue
            else:
                break
    elif user_choice == 's' and com_choice == 'r':
            print("you choose ✂️")
            print('computer choose 🪨')
            print('You lose 😔')
            continue
    elif user_choice == 's' and com_choice == 'p':
            print("you choose ✂️")
            print('computer choose 📄')
            print('you win 😁')
            con = input('Continue? (y/n):').lower()
            if con == 'y':
                    continue
            else:
                break
    else:
            print("Invalid Input")
    
        
            
