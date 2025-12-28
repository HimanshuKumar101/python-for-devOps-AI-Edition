info = {
    "name": "Himanshu",
    "city":"Noida",
   "age" : 24,
   "salary": 50000,
   "married": False


}   # dictionary are data types in python which store data in key value pair


print("I live in the", info.get("city"))

info.update({"email": "himanshukumar.connect@gmail.com"})

print(info)

for i in info:
    print(i)

print(info.keys())

#iterate through keys and values

for key, value in info.items():
    print(f"(key: {key}, value: {value})")
    