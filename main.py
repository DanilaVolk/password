import random 
simvols="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long=int(input("какова длина пароля"))
password=""
for  i in range (long):
    password += random.choice(simvols)
print(password)
