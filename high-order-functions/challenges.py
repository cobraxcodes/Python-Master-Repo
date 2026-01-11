#map countries to all upper()
def countries():
    countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
    res = list(map(str.upper, countries))
    print(res)

countries()

#alternative using lambda
def countries_lambda():
    countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
    alt_res = list(map(lambda x: x.upper(), countries))
    print(alt_res)

countries_lambda()

#use map create new list square each number
def square():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squared = list(map(lambda x: x ** 2, numbers))
    print(squared)
square()

#PYTHON
# filter out countries that contain "land"
countries_filter = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def filter_countries(x):
    return 'land' not in x
filter_res = list(filter(filter_countries, countries_filter))
print(filter_res)

filter_res_idiomatic = [x for x in countries_filter if 'land' not in x]
print(filter_res_idiomatic)

# filter countries that only contains 7 characters
def char_count(x):
    if len(x) == 7:
        return True
    return False
char_count_filter = list(filter(char_count, countries_filter))
print(char_count_filter)

idio_filter_countries = [x for x in countries_filter if len(x) == 7]
print(idio_filter_countries)

# Use filter to filter out countries having exactly six characters.
def filter_char(x):
    if len(x) == 6:
        return False
    return True
char_count = list(filter(filter_char, countries_filter))
print(char_count)

idio_char_count = [country for country in countries_filter if not len(country) == 6]
print(idio_char_count)