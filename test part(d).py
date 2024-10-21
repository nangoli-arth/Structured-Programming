def check_for_same_string(first_string, compared_string):
    if first_string == compared_string:
        print("The strings match.")
    else:
        print("The strings don't match.")

# Example for the above function
first_string = input("Enter the first string: ")
compared_string = input("Enter the second string to compare: ")

check_for_same_string(first_string, compared_string)
