import random


letter = ['A','B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J',' K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

symbol = ['!', '@', '#', '$', '%', '^', '&','*', '(', ')', '_','+','=','|','\\',',']

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

total_letter = int(input("total number of letter you want?:  "))
total_symbol = int(input("total number of symbol you want?:  "))
total_number = int(input("total number of number you want?:  "))

password=[]
#letter
for _ in range(total_letter):
    L=random.choice(letter)
    password+=L

#symbol
for _ in range(total_symbol):
    S=random.choice(symbol)
    password+=S

#number
for _ in range(total_number):
    N=random.choice(number)
    password+=N

print(password)
random.shuffle(password)
Your_password=''
for _ in password:
    Your_password += _

print(Your_password)


