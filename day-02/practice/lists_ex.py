a = [10,20,300,True,40.5,"himanshu"]

print(type(a))

clouds = list()

clouds.append("aws")
clouds.append("azure")
clouds.append("gcp")

print(clouds)

print(len(clouds))

print(clouds[0])

print(dir(clouds))   #List of all the methods related to list data type

print(clouds.extend.__doc__) #.extend method documentation the method

for i in clouds:
    print(i)