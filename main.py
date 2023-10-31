#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


l = []
for i in range(nr_letters):
  r = random.choice(letters)
  l.append(r)
# print(l)

s = []
for symbol in range(nr_symbols):
  sv = random.choice(symbols)
  s.append(sv)
# print(s)

n = []
for number in range(nr_numbers):
  num = random.choice(numbers)
  n.append(num)
# print(n)

nest = [l, s, n]
# print(nest)

password = []
for i in nest:
  for n in i:
    password.append(n)
# print(password)

new_pass = ""

for pas in password:
  new_pass += pas

# print(new_pass)2

### Alternate method:  USE - JOIN() 
### new_pass = "".join(password)
### print(new_pass)

#  Hard Level - Order of characters randomised:
#  e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(password)
# print(password)

hardpass = ""

for pas in password:
  hardpass += pas
# print(hardpass)
print()
print("Congratulations!!, you just got a bonus of 2 passwords!")
print()
print(f"First password is  : {new_pass}")
print(f"Second password is : {hardpass}")
