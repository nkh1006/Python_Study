phrase = "Giraffe Academy"

print("Giraffe Academy")
print("Giraffe\nAcademy")
print(phrase)
print(phrase + " is cool")

# length
print(len(phrase))

# is upper return true or false
print(phrase.isupper())

# upper is convert string to uppercase
print(phrase.upper().isupper())

# G
print(phrase[0])

# 0
print(phrase.index("G"))

# error
print(phrase.index("z"))

# error
print(phrase.replace("Giraffe", "Elephant"))
