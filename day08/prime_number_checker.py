
def prime_checker(number):
    is_prime=False
    for a in range(2,number):
        if number % a ==0:
            is_prime=True

    if is_prime==True:
        print(f"{number} is not prime number")
    else:
        print(f"{number} is a prime number")

n=int(input("enter a number to check:\n"))
prime_checker(n)
