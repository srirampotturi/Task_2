import random
import string

def password_generator(length):
    chara=string.digits+string.punctuation+string.ascii_letters
    password=''
    for i in range(length):
        password=password+random.choice(chara)
    return password

length=int(input("Enter length of the Password: "))
password =password_generator(length)
print("The Random Password is ", password)