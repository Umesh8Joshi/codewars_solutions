import random

print("Welcome to the password generator")
in_char = input("Enter the characters you want in your password\n")
in_pas_num = input("Enter the number of passwords you want\n")
in_pas_len = input("Enter the length of passwords\n")

for a in range(int(in_pas_num)):
    c = ''
    for b in range(int(in_pas_len)):
        c += random.choice(in_char)
    print(c)
