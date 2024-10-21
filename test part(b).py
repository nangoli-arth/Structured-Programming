def the_multiplication_table(number):
    i = 1
    while i <= 12:
        print(number, "x", i, "=", number * i)
        i += 1

# Example
num = int(input("Enter a number: "))
the_multiplication_table(num)
