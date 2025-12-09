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

