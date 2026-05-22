fruits = "apple,banana,grapes"
fruits_list = fruits.split(",")

print("split list:",fruits_list)

words = ["python", "is", "awesome"]
sentence = " ".join(words)

print("Joined Sentence:", sentence)

# Multiline string
text = """Hello
Welcome
Python"""

# Split lines
lines = text.splitlines()

print("Lines:")
for line in lines:
    print(line)

