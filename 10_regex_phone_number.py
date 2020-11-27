import re

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# print(phoneNumRegex.findall('Call me 415-555-1011 tomorrow, or at 415-555-7777'))

# for group
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# will put the first number found
# print(phoneNumRegex.search('Call me 415-555-1011 tomorrow, or at 415-555-7777'))
# print(phoneNumRegex.findall('Call me 415-555-1011 tomorrow, or at 415-555-7777'))


# songs = ''' "9 Dream" - John Lennon
# "9 to 5" - Dolly Parton
# "16 Candles" - The Crests
# "25 or 6 to 4" - Chicago
# "65 Love Affair" - Paul Davis
# "99" - Toto
# "409" - Beach Boys
# "855-7019" - Bee Gees
# "1999" - Prince
# "19'th Nervous Breakdown" - Rolling Stones
# "96 Tears" - ? and The Mysterians
# "98.6" - Keith
# "1-2-3" - Len Barry '''

# songsRegex = re.compile(r'\d+\s\w+')
# print(songsRegex.findall(songs))

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food.'))

consonantsRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantsRegex.findall('Robocop eats baby food.'))
