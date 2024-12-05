def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage (will return 0):
my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

# Example usage (will work correctly):
my_numbers = [10, 20, 30]
average = calculate_average(my_numbers)
print(f"The average is: {average}")
