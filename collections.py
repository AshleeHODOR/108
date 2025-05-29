#Pythin Collections

#1. Lists - Used to to store multiple items in a single varibale
#and they use square brackets []
#Properties: lists are ordered, changeable, and allow duplicates


empty_list = [] #this is an emptyt list
thisisalist = ["apple", "banana", "Cherry", "Orange", 10, True] #this is a list with values by default
#                 0         1        2          3              [CONTINUED... ]
print(f"empty_list: {empty_list} | Type: {type(empty_list)}")
print(f"List: {thisisalist} | Type: {type(thisisalist)}") 
# thisisalist.insert(0, "watermelon") #index, value #insert more variables
#print(f"List Changing order: {thisisalist} | Type: {type(thisisalist)}")
#not normal to modify a list 
print(f"List Length: {len(thisisalist)}") 
print(f"Accesing Elements: {thisisalist[3]}")
print(f"Accessing Elements by Negative Indexing: {thisisalist[-2]}")
print(f"Accessing Elements by Ranges: {thisisalist[1:2]}") 
print(f"Accessing Elements by Ranges: {thisisalist[:3]}") 
print(f"Accessing Elements by Ranges: {thisisalist[2:]}") 

#adding elements to the list
#1.58 - LEO??? 4 not listed with stars, WTH???
thisisalist.append("Watermelon")
thisisalist.append("Strawberry") 
print(f"List: {thisisalist} | Type: {type(thisisalist)}") 

#remove elements from the list
#no value listed in remove, deletes last item? Everything??? 2.05
thisisalist.remove("banana") 
thisisalist.pop(0)
thisisalist.pop()
print(f"List: {thisisalist} | Type: {type(thisisalist)}") 

#delete elements from specific index

#Dictionary
#Are used to stopre data values in key: value pairs.
#properties: ordered, changeable and do not allow duplicates
#ALWAYS STRINGS
thisisadict = {
    #item equal to item
    "brand" : "Ford", 
    "model" : "Mustang",
    "year" : 1964,
    "colors" : ["red", "white", "blue", "black"]
    # "year" : 2020,
    # "year" : 2025, 
    # "model" : "Expedition" 
}
print(f"Dictionary: {thisisadict} | Type: {type(thisisadict)}")
print(f"Accesing items using keys: {thisisadict["colors"][0]}")
#Dictionaries must have an order, and takes the last value; wraps last value
print(f"Dictionary Length: {len(thisisadict)}")
print(f"Accesing items using get: {thisisadict.get('year')}")
print(f"Only print the keys: {thisisadict.keys()}")
print(f"Onlyprint the values :{thisisadict.values()}")

# thisisadict["type"] = "SUV" 
# print(f"Dictionary: {thisisadict} | Type: {type(thisisadict)}")
thisisadict.update({"year" : "2024"})
thisisadict.update({"year" : "SUV"})
print(f"Dictionary: {thisisadict} | Type: {type(thisisadict)}")
#remove items
thisisadict.pop("colors")
# thisisadict.pop() - Must have a value? LEO???
print(f"Dictionary: {thisisadict} | Type: {type(thisisadict)}")

