def main():
    print("This program illustrates a chaotic function")
    
    # Get two numbers from the user
    x1 = eval(input("Enter the first number between 0 and 1: "))
    x2 = eval(input("Enter the second number between 0 and 1: "))
    
    print("\nIteration\tValue 1\t\tValue 2")
    print("-" * 40)
    
    for i in range(10):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print(f"{i+1}\t\t{x1:.6f}\t{x2:.6f}")

main()
