## LEVEL 1 CHALLENGES

def generateName(firstName, lastName): # generate random username
    return (f"Name: {firstName}, {lastName}")

def generateProduct(num1, num2):
    return num1 * num2

def celsiusConvert(farenheight):
    return (farenheight - 32) / 1.8

import random
import string

def random_user_id(): #creating number of ids and length of id from user input
    number_of_ids = int(input (' How many number of IDs do you need?'))
    length_of_ids = int(input (' How long do you want the user IDs?'))
    while number_of_ids > 0:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length_of_ids))
        print(random_string)        
        number_of_ids -= 1


def rgb_color_gen(): #generates rgb colors from range 0 to 255
    first_color = random.randint(0,255)
    second_color = random.randint(0,255)
    third_color = random.randint(0,255)
    print (f"rgb({first_color}, {second_color}, {third_color})")


## LEVEL 2
def list_of_hexa_colors(n): # returns x amount of hexidecimal colors in an array
    arr=[]
    for _ in range(n):
        arr.append('#' + ''.join(random.choices(string.ascii_letters[:6].lower() + string.digits, k=6)))
    print(arr)

def list_of_rgb_colors(n): # returns x amount of rgb colors in an array
    arr=[]
    for _ in range(n): 
        arr.append(random.randint(0,255))
    print(arr)

def generate_colors(): # returns a hexa or rgb values in x amount dependent on user input
    prompt = input("Would you like to generate a hexa or rgb?" + '')
    n = int(input("How many colors would you like?"))
    if prompt == 'hexa':
        arr = []
        for _ in range(n):
         arr.append('#' + ''.join(random.choices(string.ascii_letters[:6].lower() + string.digits, k=6)))
        print (arr)
    elif prompt == 'rgb':
        arr_rgb=[]
        for _ in range(n):
         arr_rgb.append(random.randint(0,255))
        print(arr_rgb)
    else:
        print ("Invalid response")