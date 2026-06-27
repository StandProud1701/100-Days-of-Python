import random as rd

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','^','&','*','(',')']
numbers = ['1','2','3','4','5','6','7','8','9','0']

print('Welcome to the PyPassword Generator!')

choice1 = int(input('How many letters would you like in your password?'))
choice2 = int(input('How many symbols would you like?'))
choice3 = int(input('How many numbers would you like?'))

passwordlist = []
password = ''
if (choice2>choice1) or (choice3>choice1) or (choice2>10) or (choice3>10) or ((choice1-choice2-choice3)>26):
    print('Wrong input. Please try again')
else:
    for i in range(0, choice2 + 1):
        number = rd.randint(0,len(symbols)-1)
        passwordlist.append(symbols[number])
        del symbols[number]

    for i in range(0,choice3 + 1):
        number = rd.randint(0,len(numbers)-1)
        passwordlist.append(numbers[number])
        del numbers[number]

    for i in range(0,choice1-choice2-choice3):
        number = rd.randint(0,len(alphabets)-1)
        passwordlist.append(alphabets[number])
        del alphabets[number]

    rd.shuffle(passwordlist)
    for i in passwordlist:
        password += i
    print(password)