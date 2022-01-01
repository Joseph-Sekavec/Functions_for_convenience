# This code will allow you to add characters to the beginning or end of a file, or where there are extra spaces

def delete_extra_spaces(arr):
    s = "" # We want an empty string that we can add to.

    for k in range(len(arr)): # I want to treat this like an index so I can deal with previous elements.
        if arr[k] == " " and arr[k-1] == " ": # If there is a space before your current space, replace that space with nothing.
            arr.replace(arr[k-1],"") # This replaces previous element with nothing.
        else:
            s+=arr[k] # If you don't have to replace a space, add the character to your string.

    return s


def delete_extra_characters(arr,b):
    s = "" # We want an empty string that we can add to.

    for k in range(len(arr)): # I want to treat this like an index so I can deal with previous elements.
        if arr[k] == b and arr[k-1] == b: # If there is a space before your current space, replace that space with nothing.
            arr.replace(arr[k-1],"") # This replaces previous element with nothing.
        else:
            s+=arr[k] # If you don't have to replace a space, add the character to your string.

    return s



def replace_extra_spaces(arr, b): # This will replace any extra spaces with a character of your choosing.
    s = "" # We want an empty string that we can add to.

    for k in range(len(arr)): # I want to treat this like an index so I can deal with previous elements.
        if arr[k] == " " and arr[k+1] == " ": # If there is a space before your current space, put comma.
            s+=b
        else:
            s+=arr[k] # If you don't have to replace a space, add the character to your string.

    x = input("Would you like to delete any extra characters you added? ")
    if x == "y" or x == "Y" or x == "YES" or x == "Yes" or x == "yes" or x == "YEs" or x == "yEs" or x == "yES":
        return delete_extra_characters(s, b)
    else:
        return s


#######################################################################################################################
# This is a routine that takes in a string, the place you want to add something in, and the character you want to add
# add_char(string, where to add a character, character you want to add)
def add_char(string_name, position, char_name): 
    if position == "front_and_back":
        s = char_name
        for k in string_name:
            s+= k
        s+= char_name
        return s

    if position == "front":
        s = char_name
        for k in string_name:
            s+= k
        return s

    if position == "back":
        s =""
        for k in string_name:
            s+= k
        s+=char_name


    if position == "spaces":
        s=""
        for k in string_name:
            if k ==" ":
                s+=char_name
            else:
                s+=k
        return s

    if position == "extra_spaces" or position == "extra_space":
        return replace_extra_spaces(string_name, char_name)

    
    
    
    
def rem_char(string_name, a, b, char_name): # You must enter rem_char(string, what number of desired characters must appear before we start removing, stop after this many, character you want to remove)
    position_flag = 0
    target_index = 0;
    s=""
    for k in string_name:
        position_flag+=1
        if k == char_name and target_index<a:
            target_index+=1
            print(k)
        if target_index==a:
            break    
    for k in range(len(string_name)):
        if string_name[k] == char_name and k>=position_flag and target_index>=a and target_index<b:
            target_index+=1
            s+=""
        else:
            s+=string_name[k]
    print(s)
    print(target_index)
    return s



#print(replace_extra_spaces("Hello   world",","))
#print(replace_extra_spaces("Hello   world",":"))
#print(add_char("Hello world", "front_and_back", "\"")) # works
#print(add_char("Hello world", "front_and_back", ".")) # works
#print(add_char("Hello world", "front", ".")) # works
#print(add_char("Hello world", "spaces", ".")) # works
#print(add_char("Hello  world", "extra_spaces", ".")) # works

#print(add_char(input("Input a string: "), input("Where to add character?"), input("What character? "))) # works
print(rem_char("Hello world llll hello", 3,7, "l"))
