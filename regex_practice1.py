import re
import pyperclip
patten_1 = re.compile(r'(\d{3})?-?(\d{3})-(\d{4})')      # with r complier treat the argument as raw string, if no r, you will have to use '//d'

match_1 = patten_1.search('hi, my phone number is 665-558-4545 and work number is 555-9898')
print(match_1.group())
print(match_1.group(1))
print(match_1.group(2))
print(match_1.group(0))
match_11 = patten_1.findall('hi, my phone number is 665-558-4545 and work number is 555-9898')
print(match_11)
areaCode, mid_3, last_4 = match_1.groups()  #noted group(s)

print(areaCode)
print(last_4)

pattern_2 = re.compile(r'Hi, my name is (john|jay|tim|scott)')
match_2 = pattern_2.search('Hi, my name is jay')
print(match_2.group)


#------------optional match---------
p_3 = re.compile(r'The (wo)?man who inspires')
m_3 = p_3.search('The woman who inspires')
print(m_3.group())


#-------------Fetch specific data ---------
p_4 = re.compile(r'\d+\s\w+')
m_4 = p_4.findall('I got 12 dollar, 4 apples, 6 pears and 1 girlfried')
print(m_4)

p_5 = re.compile(r'[^a-zA-Z\s,]')
m_5 = p_5.findall('I got 12 dollar, 4 apples, 6 pears and 1 girlfried')
print(m_5)

name_p = re.compile(r'First Name: (.*) Last Name: (.*)')
name = name_p.search('First Name: Jayjay Last Name: john')
print(name.group(0)) 
print(name.group(1)) 
print(name.group(2)) 

#----------------------Reg Substitute ---
namesRegex = re.compile(r'Agent \w+')
newLine = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(newLine)
agentNamesRegex = re.compile(r'Agent (\w)\w*')
newLine2 = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')

print(newLine2)

#--------------------regex for phone number --------------
#phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}
#(\s*(ext|x|ext.)\s*\d{2,5})?)')

phoneRegex = re.compile(r'''(    
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                     # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

#--------------------regex for phone email --------------
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)

#---------------find all phone and email in a clipboard

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[6] != '':
        phoneNum += ' ' + groups[6]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
        matches.append(groups[0])
print(matches)