string1 = input("Enter you string :")
string2 = ("")
for i in string1:
    string2 = i + string2
print("Your original string was ", string1)
print("The reversal of the string is", string2)