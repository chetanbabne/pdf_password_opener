from itertools import product
import string

min_len = int(input("Enter minimum length of password: "))
max_len = int(input("Enter maximum length of password: "))
counter = 0
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

with open("wordlist.txt", 'w') as file_open:
    for i in range(min_len, max_len + 1):
        for j in product(characters, repeat=i):
            word = "".join(j)
            file_open.write(word + '\n')
            counter += 1

print("Wordlist of {} passwords created".format(counter))
