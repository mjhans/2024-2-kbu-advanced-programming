input_value = None
try:
    input_value = input("Enter a number: ")
    number = int(input_value)
except Exception as e:
    print(f"Error")
    exit()


if number % 2 == 0:
    print("even")
else:
    print("odd")

