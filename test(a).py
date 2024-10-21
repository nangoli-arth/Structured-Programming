def pick_even_numbers(numbers):
    # Filter out even numbers using list comprehension
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

# Example
list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = pick_even_numbers(list_of_integers)
print("Even numbers:", even_numbers)


