text = input("enter a string: ")

reverse_text = text[::-1]

print("reverse string:",reverse_text)

if text == reverse_text:
    print("palindrome")
else:
    print("not palindrome")