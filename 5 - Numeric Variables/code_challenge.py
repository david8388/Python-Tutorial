first_num = input('Enter a number ')
second_num = input('Enter a second number ')

total = int(first_num) + int(second_num)

output = f'{first_num} + {second_num} = {total}'

print(output)

# you could round the total
total = round(float(first_num) + float(second_num))

print(output)