def generateName(firstName, lastName):
    return (f"Name: {firstName}, {lastName}")

def generateProduct(num1, num2):
    return num1 * num2

def celsiusConvert(farenheight):
    return (farenheight - 32) / 1.8

import random
import string

def random_user_id():
    length = 6
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_string