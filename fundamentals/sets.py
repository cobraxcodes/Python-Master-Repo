#creating a set
my_set = {1,2,2,3}
print(my_set)

#empty sets are this iAmEmpty=sets()

#adding items into the set
my_set.add(4)
print(my_set)

#removing items from set - note: use remove() if items needs error handling since remove wil throw error if item is not in set
my_set.remove(2)
print(my_set)

#discard - does not throw error if item is not in set
my_set.discard(4)
print(my_set)

if 2 in my_set:
    print("I am here")
else:
    print("I am not here")

    #Operations

    #union(combines sets without duplicates) (|)
    a = {1,2,2}
    b = {2,3,4}
    c = (a | b)
    print(c)

    #intersection - shows the shared values between sets (&)
    d = (a & b)
    print(d)

    #difference - shows the difference of one set to another
    e = (a - b )
    print(e)

    #symmetric difference - finds difference from both sets
    f = (a ^ b)
    print(f)