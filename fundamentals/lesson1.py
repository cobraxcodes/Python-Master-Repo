#Variables

x = True
if x:
    print("Hello World")

a = False
name = "Melrose"
age = "25"

print(a)
print(name)
print(age)


            # Convertions Exercise
#Print sum as an integer
a = "7"
b = 3
c = int(a) + b
print(c)

#Greet the User
name = "Kalena"
age = 27
print(f"My name is {name}, I am {age} years old")

#Adult Checks
def adultCheck(num):
    if(num <18):
        print("You are a minor")
    else:
        print("You are an adult")
adultCheck(17)

#Type Swap
x = int(10)
y = int("20")
print(x * y)

# Truthiness Test
items = []
if items:
    print("not empty")
else:
    print("empty")
