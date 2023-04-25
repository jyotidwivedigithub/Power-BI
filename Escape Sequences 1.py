#Backslashes are used to introduce special character coding known as Escape Sequences.
#Escape sequences let us embed chaaracters in strings that cannot easily be typed on a keyboard.
#The character \, and one or more characters following it in the string literal, are replacd with a single character in the resulting string.
#e.g.,here is a 5-character string that embeds a newline and a tab:
s='a\nb\tc'
print(s)
#len function-it returns the actual number of characters in a string.
#Escape sequences is used for non printable character, it represent single character.
print(len("hello\nhi"))    #\n is count as one character.
print(len(s))
#A few escape sequences only work as advertised if you run your program directly fro the operating system and not through IDLE. The escape sequence \a is a good example.
#Escape Meaning
    #\\ Backlash (store one\) 
    #\' Single Quote (stores')
    #\" Double Quote (stores")
    #\a Bell
    #\b Backspace
    #\f Formfeed
    #\n Newline (linefeed)
    #\r Carriage return
    #\t Horizontal tab 


#\\ Backlash (store one\) 
s='a\\b'
print(s)            # return-a\b

#\' Single Quote (stores')
s='a\'b'
print(s)            # return-a'b

#\" Double Quote (stores")
s='a\"b'
print(s)            # return-a"b

#\a Bell
s='c\ab'
print(s)            # return-cb 

#\b Backspace
s='d \b c'            # return-d c
print(s)

#\f Formfeed
s='d\fc'
print(s)          

#\n Newline (linefeed)
s='a\nb'
print(s)

#\r Carriage return
s='c\nd'
print(s)

#\t Horizontal tab
s='e\tf'
print(s)



