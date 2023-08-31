print('#### Welcome to the calculator ####')

while True:
    first_number = int(input('Please enter the first number: '))
    second_number = int(input('Please enter the second number: '))
    operator = input('Now please enter the operator\n'
                     '+ - Addition\n'
                     '- - Subtraction\n'
                     '* - Multiplication\n'
                     '/ - Division\n')
    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    elif operator == '/':
        result = first_number / second_number
    else:
        print('The operator is not valid!')
        continue

    print(f'Result: {first_number} {operator} {second_number} = {result}')

    another_operation = input('Do you want to do another calculation (y / n)?\n').lower()
    if another_operation != 'y':
        break