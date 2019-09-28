first_name = 'David'
last_name = 'Wu'

print(first_name + last_name)

print('Hello, '+ first_name + ' '+ last_name)

## custom string formatting

output = 'Hello, {} {}'.format(first_name, last_name)
print(output)

output = 'Hello, {0} {1}'.format(first_name, last_name)
print(output)

## only available in Python3
output = f'Hello, {first_name} {last_name}'
print(output)