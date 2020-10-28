### The isX() method ###

#isalpha() returns true if string is letters only and not blank
#isalnum() returns true if string is letters and numbers only and not blank
#isdecimal() returns true if string is numeric characters and not blank
#isspace() returns true if string consist of spaces, tabs, and new lines and not blank
#is title() returns true if string consists of words with the first letter upper case and not blank

while True:
    print('Enter your age.')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')