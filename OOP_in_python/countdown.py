# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1

# # Usage:
# for i in countdown(5):
#     print(i)
#     # The countdown function already uses yield, so no changes are needed.
#     # If you'd like to test it further, you can add another example:
#     print(list(countdown(3)))

#     squares = (x**2 for x in range(1, 11))
#     for square in squares:
#         print(square)


nums = [10, 20, 0, 30]

all_non_zero = all(nums)
print("All numbers are non-zero:", all_non_zero)

any_divisible_by_5 = any(num % 5 == 0 for num in nums)
print("At least one number is divisible by 5:", any_divisible_by_5)