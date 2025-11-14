# Using Loop
n = int(input("Enter a num: ")
fact = 1
for i in range(1,n+1):
  fact = fact * i
print("The factorial of", n, "is", fact)

# --------------- OR ------------

#Using recursion
def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factorial(n-1)
#user input
n = int(input("Enter a num: "))
print("The factorial of", n, "is", fact)
