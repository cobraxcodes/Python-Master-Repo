# Filter only negative and zero from list
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_list = [number for number in numbers if number > 0]
print(filtered_list)

#flatten 3d into 1 list 
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [num for num in list_of_lists for num in num for num in num]
print(flattened_list)

# create tuple w/ multiplicative Fibonnaci 
base = 2
fltr_pow = [2 ** num for num in range(0,7)]
fltr_pow.insert(0,base)
print(fltr_pow)

# flatten list to a new sets
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten_countries = [[place for country in countries for place in country for place in place]]
print(flatten_countries)

# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_countries = [{'country': country.upper(), 'city': city.upper()} for country in countries for country, city in country]
print(dict_countries)
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates'
names_concat = ' ,'.join(" ".join(lst) for lst in names for lst in lst)
print(names_concat)

