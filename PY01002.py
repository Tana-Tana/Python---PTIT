number = input()
numbers = []
numbers = number.split()
if int(numbers[0]) + int(numbers[2]) == int(numbers[4]):
    print(f"YES")
else:
    print(f"NO")
