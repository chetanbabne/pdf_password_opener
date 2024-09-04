import pikepdf
from termcolor import colored

# Open the wordlist file
file = open("wordlist.txt")

# Iterate over each password in the wordlist
for password in file:
    try:
        # Attempt to open the PDF with the current password
        with pikepdf.open("remote.pdf", password=password.strip()) as pdf:
            print(colored("Password Found: {}".format(password.strip()), 'green'))
            break  # Exit the loop if the password is found
    except pikepdf.PasswordError:
        # If the password is incorrect, print the attempt
        print(colored("Trying Password: {}".format(password.strip()), 'red'))
    continue

# Close the wordlist file
file.close()
