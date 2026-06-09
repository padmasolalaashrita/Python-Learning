import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z']

symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}',
    '\\', '|',
    ';', ':',
    "'", '"',
    ',', '<', '.', '>',
    '/', '?',
    '`', '~'
]

a = int(input("How many alphabets do you want in your password?\n"))
b = int(input("How many symbols do you want in your password?\n"))
c = int(input("How many numbers do you want in your password?\n"))

chars = []

for _ in range(a):
    chars.append(letters[random.randint(0, 25)])

for _ in range(b):
    chars.append(symbols[random.randint(0, len(symbols) - 1)])

for _ in range(c):
    chars.append(str(random.randint(0, 9)))

random.shuffle(chars)

word = ''.join(chars)
print(f"Your password could be: {word}")
