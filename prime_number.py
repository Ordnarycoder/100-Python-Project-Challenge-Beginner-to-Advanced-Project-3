def check_prime():
    number = int(input("Please enter a number:\n"))
    i =2
    if number == 0:
       return print("0 is not a prime number")
    elif number < 0:
       return print("Please enter a positive number")
    elif number == 1:
       return print("1 is not a prime number")
    while i < number:
      if number % i == 0:
        print("It's not a prime number")
        return
      i +=1
    print("It's a prime number")
check_prime()