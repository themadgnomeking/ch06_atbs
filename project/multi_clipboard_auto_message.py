#! python3
#multi_clipboard_auto_message.py - a multi-clipbooard program


#step 1: program design and data structure
#   Run this prgram with a CLI short phrase like 'agree' or 'busy'
#   The message will be copied to the clipboard so it can be pasted into an email
#   This way the user can have a long, detailed message without having to retype them

TEXT = {
    'agree': """Yes, I agree. That sounds fine to me.""",
    'busy': """Sorry, can we do this later this week or next week?""",
    'upsell': """Would you consider making this a monthly donation?"""
}

#step 2: handle command line arguments
#   the cli arguments will be stored in a variable sys.argv
#   the first item in sys.argv list should always be a string containing the programs file name
#   and the second item shnould be the first cli argument
#   for this program, this argument is the key phrase of the message you want
#   since the cli argument is mandatory, you will display a usage messate to the user if they
#   forget to add it (this is, if the sys.argv list has vewer than two values in it)

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python multi_clipboard_auto_message.py[keyphrase] - copy phrase text')
    sys.exit()
keyphrase = sys.argv[1] #first command line arg is the keyphrase

#step 3: copy the right phrase
#   now that the key phrase is stored as a string in the variable [keyphrase]
#   you need to see whether it exists in the TEXT dictionary as a key
#   If so, you want to copy the key's value to the clipboard using pyperclip.copy()
#   (Since you're using the pyperclip module, you need to import it)
#   note that you don't actually need the [keyphrase] variable;
#   you could just use sys.argv[1] everywhere [keyphrase] is used in the program
#   but a var named [keyphrase] is much more readable than something cryptic like sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard')
else:
    print('There is no text for ' + keyphrase)