num = int(input("Enter the number: "))

if num <= 1:
  print("Enter the prime no. ")
else:
  is_prime =True
  i= 2

  while i*i <=num:
    if num%i == 0:
      is_prime = False
    i+=1

  if is_prime:
    print("Number is prime")
  else:
    print("Number is not prime")
