num = int(input("Enter an integer: "))

# Check even or odd
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Check prime number
if num < 2:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")