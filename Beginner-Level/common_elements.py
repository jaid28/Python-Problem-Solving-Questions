list1 = []
list2 = []
num1 = int(input("Enter the number of elements: "))

for _ in range(num1):
    val = int(input("Enter the numbers: "))
    list1.append(val)
    
num2 = int(input("Enter the number of elements: "))
for _ in range(num2):
    val = int(input("Enter the numbers: "))
    list2.append(val)
    
common = []
for x in list1:
    if x in list2:
        common.append(x)
print("The common number are: ",common)
