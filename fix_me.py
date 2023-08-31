def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    return total / count


nums_list = [
    10,
    15,
    20,
]
average_result = calculate_average(nums_list)
print(f"The average is: {average_result}")
