# input exception
try:
    name = input ("Enter Your Name: ")
    age = int(input("Enter your age: "))
    def adult(age):
        if age >= 18:
            return ("you're an adult")
        else:
            return ("you're a minor!")            
    is_adult = adult(age)
    print(f"Nice to meet you, {name}. You're {age}? That means {is_adult} ")

    # print(f"Error occured here: {e}")
except TypeError:
    print("Type error has occured") #this error occures for incompatible operands, calling non-callables, incorrect indexing, non-iterable objecxts, wrong function arguments
except ValueError:
    print("Please enter the correct values. Value error has occured") #incorrect data type entered in input
except: #catch all clause
    print("Something went wrong")
