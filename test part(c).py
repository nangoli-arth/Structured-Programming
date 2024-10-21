def find_largest_number(numbers):
    largest = numbers[0]  # thus assumes that the first number is the largest at first
    for num in numbers:
        if num > largest:  # If the current number is larger,then update largest
            largest = num
    print("The largest number is:", largest)

# taking an example;
input_numbers = [3, 7, 2, 9, 5, 1]
find_largest_number(input_numbers)
