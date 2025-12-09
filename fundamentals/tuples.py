#creating a tuple - always include a comma , 
colors = ("black","white", "red")
print(colors[1])

for color in colors:
    print(color)

# tuple unpacking
person = ("Cobra", "Backend", "Python")
name, role, skill = person
print(skill)

#nested tuple
nest = ("hello", ["apples", "oranges", "pears"], ("green", "brown", "black"))
print(nest[2][1])

#converting to tuples
nums = [1,2,3,4]
nums_tuples = tuple(nums)
print(nums_tuples)
print(type(nums_tuples))
