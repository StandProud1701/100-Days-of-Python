import random as rd

user_choice = int(input("Enter your choice (0 for Rock, 1 for Paper, 2 for Scissors): "))
computer_choice = rd.randint(0, 2)

choices = [
 '''_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

print(choices[user_choice])
print()
print("Computer chose:")
print(choices[computer_choice])
print()
if user_choice == computer_choice:
    print("")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")