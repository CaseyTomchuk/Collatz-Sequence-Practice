def collatz(number):
    if number == 0:
        print("You can't enter 0!")
        return
    if number != 1:
        if number % 2 == 0: #If # is even, divide by 2
            number = number // 2
            print(number)
        elif number % 2 == 1: #If # is odd, do this sequence
            number = 3 * number + 1
            print(number)
    elif number == 1:
        return # Exit the loop
        
    collatz(number) # Call the function recursively

while True:
    try:
        value = int(input("Input: "))
        collatz(value)
    except ValueError:
        print("Enter a valid integer instead")