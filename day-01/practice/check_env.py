# Get the environemnt from the user and print it 

env = input() # taking input from the user

print("the environment is : ", env)

a = input("Enter first number:")
b = input("Enter second number: ")

#conditional statements
if env == "prod":
    print("don't deploy on friday")
elif env == "stg":
    print("deploy only after testing")    
else:
    print("you can deploy anytime")    

sum = int(a) + int(b)

print("the sum of a & b is:", sum)

