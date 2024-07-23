numbers = [1, 2, 3, 4, 5]
modified_numbers = [modified_numbers+10 if modified_numbers%2 == 0 else modified_numbers-1 for modified_numbers in numbers]
print(numbers,modified_numbers)