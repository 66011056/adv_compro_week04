numbers = [1, 2, 3, 4, 5]
#outputs = [item for item in numbers if item%2==0]
outputs = [item%2==0 item for item in numbers]
print(numbers, outputs)

#number = 9
#status = "Even" if number%2==0 else"Odd"
#print(status)

#listcomprehension
#numbers = [1, 2, 3, 4, 5]
#outputs = ["Even" if item%2==0 else"Odd" for item in numbers]
#print(numbers, outputs)