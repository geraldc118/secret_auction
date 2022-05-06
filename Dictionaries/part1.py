programming_dictionary = {
"Bug": "An error in a program that prevents the program from running as expected.", 
"Function": "A piece of code that you can easily call over and over again.",
"loop":"This action is doing something over and over"
}

# #Retrieving items from a dictionary.
# print(programming_dictionary["Bug"])

# #Adding new items to list
# programming_dictionary["Loop"] = 'The action of doing something over and over again.'
# print(programming_dictionary) 

# #Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# #Edit an item in dictionary
# programming_dictionary["Bug"]= "A moth in your brain."

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])