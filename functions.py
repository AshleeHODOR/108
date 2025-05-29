#Function
#Is a block of code which only runs when it's called
#We can pass data, known as parameters and the function can data as a result

def my_function():
    print("Hello froma  function!")

def other_function():
    print("This is another function!")

#calling function
my_function()
other_function() 

def my_function(fname):
    print(fname + "HODOR")

#python takes last parameter
#def my_function(fname):
    #print(fage + "Hello")

my_function("Ashlee")

def print_full_name(fname, flast_name):
    print(f"{fname} {flast_name}")

print_full_name(10, 15) 
#more specific
print_full_name(fname="Ashlee", flast_name="HODOR")

#functions return:
def print_full_name_two(fname, flast_name):
    return f"{fname} {flast_name}"
#call the function
#full_name = print_full_name_two("Ashlee", "HODOR")
#print(full_name) 

#return varibales from function
def add(x, y): #x=10 y=3 
    return x + y #13 

#variable is called result
#result = add(5,5) #13
#print(result) #13

#input
#allows us to interact with terminal and pass some values

#name = input("Enter your name: ") 
#print(name)
#age = input("Enter your age: ")


x = input("Enter a value: ") 
print(type(x))
y = input("Enter a second value: ")
print(type(y))
print(x+y)

x = int(input("Enter a value: "))
print(type(x))
y = int(input("Enter a second value: "))
print(type(y))
print(x+y)

print(add(x,y)) 


#print(x+y)
#concatinating {5 and 3 are strings}
#print(type(x))

#wrap everything into input method

name = "Harry"
age = 11 

print(name + str(age))
print(f"Hello I am {name}, and I am {age} years old")