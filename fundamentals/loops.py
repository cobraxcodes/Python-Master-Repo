#range - print the range of numbers from 0 to number specified
for x in range(10):
    print(x)

for x in range (1, 11): #(start, end) - prints the range from start to end
    print(x)

for y in range (0,20,2): #(start, end, by 2s) - prints by 2s
    print(y)

for y in range(10,1,-1): #(start, end, -1 each time)
    print(y)

#enumerate 
for index, value in enumerate(["a","b","c"]):
    print(index, value) # prints the index of the value and the value itself

#looping both lists at the same time
nums = [1,2,3]
words = ["one","two","three"]

for x,y in zip(nums,words):
    print(x,y)