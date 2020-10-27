#### Working With Strings ####

#Double Quotes
spam = "This is Alice's Cat." #double quotes allows for single quotes to be used without escaping
print(spam)

#Escape Characters
spam = 'Say hi to bob\'s mother' #escape charatcer \ allows to use single quotes in a single quote comment
print(spam)

#\' - Single quote
#\" - Double quote
#\t - Tab
#\n - new line (line break)
#\\ - backslash

hello = "Hello There!\nHow are you?\nI\'m doing fine"
print(hello)

#raw strings

raw_string = r'This is Carol\'s cat.' # this will print everything, it doesn't allow for escape characters
#this can be useful for something like a windwos directory

print(raw_string)

#multiline string with triple quotes
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion. 
Sincerely, 
Bob''')