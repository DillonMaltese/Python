#Printing out stuff
print('Hola Ninos')

#Variables include:
#Ints
Age = 14

#Floats
SAge = 10.9

#Strings which can use single or double quotes
Name = "Dillon"

#Booleans
agerestriction = False

#When printing a String and an int or float you have to say str() before saying the int or float
#print("Name: " + name)
#print("Age: " + str(Age))
#print("Sister's age: " + str(SAge))
#print("Is my age over twenty " + str(agerestriction))

#input
name = input("What is your name? ")
print("Hello " + name)
birth = input("What is your birth year? ")
age = 2022 - int(birth)
print("Your age is " + str(age))

