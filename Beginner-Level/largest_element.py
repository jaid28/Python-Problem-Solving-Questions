n = int(input("How many numbers: "))
largest = None
for i in range(n):
  num = int(input("Enter the numbers: "))
  if largest is None or num > largest:
    largest = num

print("The largest number from",n, "element is:",largest)

#------------- OR -------------

n = int(input("How many numbers: "))
numbers = []
for i in range(n):
  num = int(input("Enter the numbers: "))
  numbers.append(num)
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("The largest number from",n, "element is: ",largest)
