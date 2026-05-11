

a = input("Enter first boolean value (True/False): ")
b = input("Enter second boolean value (True/False): ")

# Convert string input into boolean
a = a == "True"
b = b == "True"

print("\nLogical AND :", a and b)

print("Logical OR  :", a or b)

print("Logical NOT of first value :", not a)
print("Logical NOT of second value:", not b)