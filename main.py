def delete_extra_spaces(arr):
    s = ""
    val = []
    i = 1
    j = 0

    for k in range(len(arr)):
        if arr[k] == " " and arr[k-1] == " ":
            arr.replace(arr[k-1],"")
        else:
            s+=arr[k]

    return s

# arr = "Hello world"

#for k in range(len(arr)):
#    print(k)

# print(delete_extra_spaces(input("Enter a string: ")))