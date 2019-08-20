import secrets as sc
import string

def generator(lst,length):
	pw = ""
	ln = len(lst)
	for i in range(0,length):
		pw += sc.choice(lst[sc.randbelow(ln)])	
	return pw

length = input("What is the length of the password? ")

try:
	length = int(length)
except ValueError:
	print("Invalid input - Password length")
	exit()

if(length < 1):
	print("Invalid input - Password length")
	exit()

spec = input("Allow special characters?(Y/N) ")

if((spec.lower() != 'y') and (spec.lower() != 'n')):
	print("Invalid input - Special characters")
	exit()

if(spec == 'y'):
	spec = True
else:
	spec = False

numbers = []
for i in range(0,9):
		numbers.append(str(i))

combo = [string.ascii_lowercase,string.ascii_uppercase,numbers]

if(spec):		
	combo.append(string.punctuation)

print("Password:", generator(combo,length))
