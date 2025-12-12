#---- LISTS -------#
# 1️⃣ Sum only odd numbers in a list
# sum_odds([1,2,3,4,5]) ➝ 9

def sumOdds(nums):
    sum = 0
    for num in nums:
        if not num % 2 == 0:
            sum += num
    return sum

print(sumOdds([1,2,3,4,5]))
# 2️⃣ Count how many strings start with the letter "p"
# count_p(["python","dog","pizza"]) ➝ 2

def countStrings(arr):
    newArr = []
    total = 0
    for words in arr:
      if words[0] == "p":
          newArr.append(words)
          total = len(newArr)
    return total

print(countStrings(["python","dog","pizza"]))
          

# 3️⃣ Return the largest number in a list without using max()
# largest([3, 7, 2, 9, 5]) ➝ 9

def largestNum(numbers):
    largest = 0
    for number in numbers:
        if number > largest:
            largest = number
    return largest

print(largestNum([3, 7, 2, 9, 5]))


# 4️⃣ Create a new list with all numbers multiplied by 10 using a list comprehension
# mult_ten([1,2,3]) ➝ [10,20,30]
mult_ten = [1,2,3]

newList=[x * 10 for x in mult_ten]

print(newList)

# 5️⃣ Print every number between 25 and 1 using a while loop
count = 25
while count >= 1:
    print(f"count is: {count}")
    count -= 1
# (reverse countdown)
#------------------------------------------------------#

# SETS
## create a set and loop through to elemets and check if "apples" is in set
fruits = {"apples", "oranges", "kiwis", "bananas"}
print(fruits)
if "apples" in fruits:
    print("yes")
else:
    print("no")
##create a set from list
nums = [1, 2, 2, 3, 4, 4, 4, 5]
set_nums = set(nums)
print(set_nums)

##add two elements in nums set
new_nums = (6,7)
set_nums.update(new_nums)
print(set_nums)
set_nums.remove(7)
print(set_nums)

#set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
##union 
c = (a | b)
print(c)
##intersection
d = (a & b)
print(d)
##difference
e = (a - b)
print(e)
## symmetric difference
f = (a ^ b)
print(f)

#-------- LOOPS -----
## print all numbers from 10 to 0 backwards
for x in range (10,-1, -1):
    print(x)

## loop through both index and value
colors = ["red", "blue", "green"]
for x, y in enumerate(colors):
    print(x,y)

## remove values less than 50 from list
nums = [10, 80, 22, 100, 65, 30]
for x in nums[:]:
    if x < 50:
        nums.remove(x)
print (nums)

## loop throught two items at the same time
ids = [101, 102, 103]
names = ["alex", "sam", "taylor"]

for x,y in zip(ids,names):
    print(x,y)

## flatten nested list
data = [[4,5], [10,11,12]]
flat_list = []
for x in data:
    for y in x:
        flat_list.append(y)
print(flat_list)