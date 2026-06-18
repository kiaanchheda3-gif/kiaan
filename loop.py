num = 1 
while num>=1:
    number_one = float(input("Enter a number: "))
    number_two = float(input("Enter another number: "))
    operator = input("Enter an operator: ")
    if operator =="+": print(number_one + number_two)
    elif operator =="-": print(number_one - number_two)
    elif operator =="*": print(number_one * number_two)
    elif operator =="/": print(number_one/number_two)