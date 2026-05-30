squares = [x**2 for x in range(1,11)]
print("squares: ",squares)

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Create a new list with only even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

print("even numbers: ",even_numbers)

# List of strings
words = ["hello", "world", "pyThOn"]

# convert all string to lowercase
lowercase_words = [word.lower() for word in words]

print("lower words:", lowercase_words)