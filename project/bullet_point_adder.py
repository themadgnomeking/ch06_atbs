#! python3
# bulletPointPadder.py - Adds Wikipedia bullet points to start

#### Adding Bullets To Wiki Markup ####

#1. Past text from a clipboard
#2. Do something to it
#3. Copy the new text to the clipboard


import pyperclip

text = pyperclip.paste()

#seperate lines and add stars
lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]  #add star to each string in "lines" list

text = '\n'.join(lines)

pyperclip.copy(text)