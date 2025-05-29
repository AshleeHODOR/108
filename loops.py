def print_header(title): #variable; developer names 
    print("--------------")
    print(title)
    print("--------------")

def roll_call():
    names = ["HODOR", "Patrick", "Ivan", "Kenny"] #spaces not necessary
    print(names[0])
    print(names[1])
    print(names[2])
    print(names[3])
    print_header("loop 1")

    for student in names:
        print(student)

def get_total():
    print_header("   Prices")
    prices = [42, 17, 99, 23, 42, 5, 74, 29, 55, 10]
    total = 0 
    for price in prices:
        print(price) 
        total = total + price 

    #when for loop finishes
    print_header(total) 


def print_cheap_prices():
    print_header("   Cheap prices")
    prices = [12, 56, 21, 63, 45, 47, 12, 89, 39, 74, 23, 85, 35, 86]
    #create a for loop to print every price
    for price in prices:
        if price <50:
            print(price)


def print_expensive_prices():
    print_header(" Expensive prices") 
    prices = [12, 56, 21, 63, 45, 47, 12, 89, 39, 74, 23, 85, 35, 86]
    for price in prices:
        if price > 50:
            print(price)


def start_program():
    print_header("   HODOR") #call the function
    print("Hello from loops")
    roll_call()
    get_total()
    print_cheap_prices()
    print_expensive_prices()


# when the program starts, we call
start_program()