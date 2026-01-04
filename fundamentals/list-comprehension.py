# string to list
word = 'python'
word_list = [ltr for ltr in word] #input for output in variable expression
print(type(word_list))
print(word_list)

# filtering string to print only vowels
word_upper = word.upper()
vowels = ["A", "E", "I", "O", "U"]
vowels_only = [ltr for ltr in word_upper if ltr in vowels]
print(vowels_only)

# generate range of numbers to list
number_list = [num for num in range(1, 20)]
print(number_list)

#filtering numbers
only_evens = [num for num in range(20) if num % 2 == 0]
print(only_evens)

# flattening 3d array 2 loops
three_dimension = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [arr for arr in three_dimension for arr in arr]
print(flatten)