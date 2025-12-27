# for i in range(5):
#     env = input() # taking input from the user

#     print("the environment is : ", env)

#     a = input("Enter first number:")
#     b = input("Enter second number: ")

#     #conditional statements
#     if env == "prod":
#         print("don't deploy on friday")
#     elif env == "stg":
#         print("deploy only after testing")    
#     else:
#         print("you can deploy anytime")    
#     sum = int(a) + int(b)

#     print("the sum of a & b is:", sum)


num = int(input("Enter a number: "))

#string formatting
for i in range(10):
    print(f"{num} x {i + 1} = { num * (i +1)}") #here f is used for formatting the string


choice = input("Do you want to continue? (yes/no):")

while choice.lower() == "yes":
    num = int(input("Enter a number: "))
    for i in range(10):
        print(f"{num} x {i + 1} = { num * (i +1)}")
    choice = input("Do you want to continue? (yes/no):")