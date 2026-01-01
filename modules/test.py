import sample #importing the entire module
print(sample.generateName("Test", "I am"))
print(sample.generateProduct(2,2))

from sample import celsiusConvert # importing specific function from module
print(celsiusConvert(1))

from sample import generateProduct as productOnly #importing specific function and renaming the module
print(productOnly(2,2))


import os #importing built-in python module for os commands / pathing
print (os.getcwd())

import sys #importing arguments from command line passed to python script
print ('Welcome {}. Enjoy {} challenge!'.format(sys.argv[1], sys.argv[2]))
print(sys.path)
print(sys.version)

from statistics import * #importing all functions from statistics modules
ages = [10,20,30,40,50]
print(mean(ages))
print(median(ages))
print(stdev(ages))

import math #importing math module
print(math.pi)
print(math.ceil(8.5))
