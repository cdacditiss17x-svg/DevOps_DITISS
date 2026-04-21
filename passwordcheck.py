#password checker

password=input("Enter the password")
check_upp=0
check_low=0
check_dig=0
check_spl=0
spl=["@","#","*",]

for char in password:
    if char.isupper():
        check_upp += 1
    if char.islower():
        check_low += 1
    if char.isdigit():
        check_dig += 1
    if char in spl:
        check_spl +=1