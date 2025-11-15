string = input("Enter the string: ")

reverse_string = string[::-1]
print(reverse_string)


# -------------- OR --------------

string = input("Enter the string: ")

rev = ""
for ch in string:
    rev = ch + rev
print(rev)
