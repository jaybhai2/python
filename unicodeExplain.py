
# ASCII maps one byte(8bit) to one character, thus ASCII can represent 256 character.
# however, there are character of other language cannot be represented  ie chinese character or even emoji
# unicode code use 4,5,6 digit of hex to represent character ie U+00F8 is latin letter 'o' with stroke 
# each digit of hex in unicode represented by ASCII
# thus 4 digit unicode actually is 4x4bytes  = 16 bytes

#python 3 treats string as unicode string
myStr = 'hi \u006a\u0061\u0079'  # 'hi jay' automatically converted
print(type(myStr))                  # unicode string
print(len(myStr)) 
print(myStr)

myBytes = b'hi jay'             # if you type in byte code, it will not be automatically converted
print(type(myBytes))            #byte string
print(len(myBytes))    

print(myStr == myBytes)

myUnicode = u'hi \u006a\u0061\u0079'
print(type(myStr))                  # unicode string 
print(len(myStr)) 
print(myStr)