string = str(input("Please enter the string you want to be reversed here:"))

string2 = ('')
for i in string:
    string2 = i + string2

print("The original string was", string)
print("The reversed string was", string2)