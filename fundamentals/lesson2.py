#LOOPS

#sum only even number in list
def evenOnly(nums):
    sum = 0;
    for n in nums:
        if n % 2 == 0:
            sum += n
    return(sum)
        
print(evenOnly([1, 8, 3, 12, 5, 18]))

#count string length
def countStrings(arr):
    count = 0
    for words in arr:
        if len(words) > 3:
            count += 1
    return count

print(countStrings(["hi", "hello", "sun", "python", "no"]))

# Find the First Number Greater Than 100
def greatestNum(arr):
    greater = 0
    for num in arr:
        if num > 100:
            greater == num
            break;
    return num

print (greatestNum([10, 50, 99, 102, 80, 150]))

# Build a New List (List Comprehension Warm-Up)
def oldList(arr):
    newList=[]
    for number in arr:
        if number >= 75:
            newList.append(number)
    return newList

print(oldList([72, 68, 90, 101, 77]))

# Fizbuzz lite
#mysolution:
def fizzbuzz(num):
    count = 0
    while count <= num:
        if count % 3 == 0:
            print("fizz")
            count += 1
        elif count % 5 == 0:
            print("buzz")
            count += 1
        else:
            print(count)
            count += 1

print(fizzbuzz(20))

#bettersolution:
# def fizzbuzz(num):
#     for count in range(1, num + 1):
#         if count % 3 == 0 and count % 5 == 0:
#             print("fizzbuzz")
#         elif count % 3 == 0:
#             print("fizz")
#         elif count % 5 == 0:
#             print("buzz")
#         else:
#             print(count)

# fizzbuzz(20)
