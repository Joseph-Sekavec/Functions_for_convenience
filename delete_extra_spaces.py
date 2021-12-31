# This function will take in a string, then it will delete absolutely every space in between each word or character except for one. (I will later possibly add something dealing
# with spaces at the beginning and/or end of a line).

def delete_extra_spaces(arr):
    s = "" # We want an empty string that we can add to.

    for k in range(len(arr)): # I want to treat this like an index so I can deal with previous elements.
        if arr[k] == " " and arr[k-1] == " ": # If there is a space before your current space, replace that space with nothing.
            arr.replace(arr[k-1],"") # This replaces previous element with nothing.
        else:
            s+=arr[k] # If you don't have to replace a space, add the character to your string.

    return s

#print(delete_extra_spaces(input("Enter a string: ")))  # This is a test function.
