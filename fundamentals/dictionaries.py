#Create a dictionary for user profile
user = {
    "username":"cobraxcodes",
    "email": "testMail@test.com",
    "roles": "backend developer",
    "is_admin": True,
}
#operations
user['login_count']=1; #adding key and value
user['email']='testEmail@test.com' #updating value only
user.update({"login_count": 2}) # updating key and value
user.pop("roles") #removes key and value of specified element
del user["is_admin"] #another way to remove key and value
user.popitem() #removes last element inserted 
print(user["username"])
print(user)

#looping
for values in user:
    print(user[values]) #to loop and receive back only values

for keys in user.keys(): #to loops only through keys and receive back only keys
    print (keys)

for keys, values in user.items(): #to loops keys, values and receive both
    print(keys, values)


second_version = user.copy() #making copy of dictionary
print(second_version)



#nested loops
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"]) #printing nested element

for x, y in myfamily.items(): #printing keys and values of nested element
    print(x,y)

for keys in myfamily: #printing only keys
    print(keys)