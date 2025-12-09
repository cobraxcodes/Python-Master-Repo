#capitalize
a = "hello"
b = a.capitalize()
print(b)

#casefold
c = "HELLO"
d = c.casefold()
print(d)

#center - prints strings with assigned space
 # string.center(number of spaces here)
f = a.center(20)
print(f)

#count -counts how many characters are in strings
g = a.count("l")
print(g)

#encode - turns string into machine language
h = a.encode()
print(h)

#endswith - checks if string ends with a certain character
i = a.endswith("o")
print(i)

#expandtabs() - to create specific spacing w/ tabs
j = "h\te\tl\tl\tl\to"
k = j.expandtabs(20)
print(k)

#find - looks for specific character and returns the index of character
l  = a.find("h")
print(l)


#--------SLICING---------
z = "Hello World"
print(z[:4]) # : <-- signifies start , 4 <--- ends before the 4th character
print(z[5:]) # starts from 5th character through end of string
print(z[-7:-3]) 